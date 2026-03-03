from dataclasses import dataclass
from enum import Enum
from typing import Dict, List


class VendingError(Exception): pass
class InvalidSelection(VendingError): pass
class OutOfStock(VendingError): pass
class InsufficientFunds(VendingError): pass
class CannotMakeChange(VendingError): pass


@dataclass(frozen=True)
class Product:
    id: str
    name: str
    price_cents: int


class Denomination(Enum):
    # Keep it simple; easily extend with more denominations later
    CENT_10 = 10
    CENT_20 = 20
    CENT_50 = 50
    EUR_1 = 100
    EUR_2 = 200
    EUR_5 = 500


class Inventory:
    def __init__(self) -> None:
        self._products: Dict[str, Product] = {}
        self._stock: Dict[str, int] = {}

    def add_product(self, product: Product, quantity: int) -> None:
        self._products[product.id] = product
        self._stock[product.id] = self._stock.get(product.id, 0) + quantity

    def get_product(self, product_id: str) -> Product:
        if product_id not in self._products:
            raise InvalidSelection(f"Unknown product id: {product_id}")
        return self._products[product_id]

    def in_stock(self, product_id: str) -> bool:
        return self._stock.get(product_id, 0) > 0

    def decrement(self, product_id: str) -> None:
        if not self.in_stock(product_id):
            raise OutOfStock(f"Product {product_id} is out of stock")
        self._stock[product_id] -= 1


class CashRegister:
    """
    Tracks inserted money and can compute change using available denominations.
    In a real system you'd also track how many coins of each type exist.
    """
    def __init__(self) -> None:
        self._balance_cents = 0

    @property
    def balance_cents(self) -> int:
        return self._balance_cents

    def insert(self, denom: Denomination) -> None:
        self._balance_cents += denom.value

    def refund(self) -> int:
        amount = self._balance_cents
        self._balance_cents = 0
        return amount

    def take_payment(self, price_cents: int) -> int:
        if self._balance_cents < price_cents:
            raise InsufficientFunds(
                f"Need {price_cents}, have {self._balance_cents}"
            )
        self._balance_cents -= price_cents
        change = self._balance_cents
        self._balance_cents = 0
        return change

    def make_change(self, change_cents: int) -> List[Denomination]:
        # Greedy works for typical euro denominations; keep it simple for interview.
        result: List[Denomination] = []
        remaining = change_cents
        denoms = sorted([d.value for d in Denomination], reverse=True)

        for v in denoms:
            while remaining >= v:
                remaining -= v
                result.append(Denomination(v))

        if remaining != 0:
            raise CannotMakeChange(f"Cannot make exact change: remaining={remaining}")
        return result


class MachineState(Enum):
    IDLE = "idle"
    HAS_MONEY = "has_money"


class VendingMachine:
    def __init__(self, inventory: Inventory, register: CashRegister) -> None:
        self._inventory = inventory
        self._register = register
        self._state = MachineState.IDLE

    @property
    def state(self) -> MachineState:
        return self._state

    @property
    def balance_cents(self) -> int:
        return self._register.balance_cents

    def insert_money(self, denom: Denomination) -> None:
        self._register.insert(denom)
        self._state = MachineState.HAS_MONEY

    def cancel(self) -> int:
        refunded = self._register.refund()
        self._state = MachineState.IDLE
        return refunded

    def select_product(self, product_id: str) -> dict:
        product = self._inventory.get_product(product_id)

        if not self._inventory.in_stock(product_id):
            raise OutOfStock(f"{product.name} is out of stock")

        # verify payment first
        if self._register.balance_cents < product.price_cents:
            raise InsufficientFunds(
                f"{product.name} costs {product.price_cents}, balance {self._register.balance_cents}"
            )

        # dispense
        self._inventory.decrement(product_id)
        change_cents = self._register.take_payment(product.price_cents)
        change = self._register.make_change(change_cents)

        self._state = MachineState.IDLE
        return {
            "dispensed": product.name,
            "change": [d.name for d in change],
            "change_cents": change_cents,
        }