"""
SOLID: each “variable” explained (S, O, L, I, D)
S — Single Responsibility Principle

A class should have one reason to change.

Bad: one class does parsing + validation + DB + emailing.
Good: split responsibilities.

Typical example:

InvoiceCalculator (computes totals)

InvoiceRepository (saves/loads)

InvoiceMailer (sends)

Why: Easier testing, fewer side effects, smaller blast radius.

O — Open/Closed Principle

Open for extension, closed for modification.

Meaning: you should be able to add new behavior without editing existing stable code constantly.

Example: adding a new PaymentProvider should not require editing checkout().

Bad:

def checkout(provider_name, amount):
    if provider_name == "stripe": ...
    elif provider_name == "adyen": ...

Good: use polymorphism (Strategy pattern):

def checkout(provider: PaymentProvider, amount: int):
    return provider.charge(amount)
L — Liskov Substitution Principle

If S is a subtype of T, then objects of type T should be replaceable with objects of type S without breaking correctness.

In plain terms:

Subclass must honor the base class contract (inputs/outputs/behavior).

Don’t strengthen preconditions.

Don’t weaken postconditions.

Don’t throw new unexpected exceptions.

Classic violation: Square inheriting Rectangle when setting width breaks height assumptions.

Practical violation example:
Base says: “withdraw(x) works for any x <= balance”
Subclass introduces “withdraw only multiples of 10” → breaks substitution.

I — Interface Segregation Principle

Clients should not be forced to depend on methods they don’t use.

Meaning: don’t make huge “fat” interfaces.

Bad:

class Worker(ABC):
    @abstractmethod
    def work(self): ...
    @abstractmethod
    def eat(self): ...

Robots don’t eat → forced to implement meaningless methods.

Good: split:

class Workable(ABC):
    @abstractmethod
    def work(self): ...

class Eatable(ABC):
    @abstractmethod
    def eat(self): ...
D — Dependency Inversion Principle

Depend on abstractions, not concretions.

High-level code shouldn’t instantiate or depend directly on low-level details.

Bad:

class UserService:
    def __init__(self):
        self.repo = PostgresUserRepo()   # hard-coded dependency

Good:

class UserRepo(ABC):
    @abstractmethod
    def get_user(self, user_id: int): ...

class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

Now you can inject PostgresUserRepo, InMemoryUserRepo, MockRepo easily.
"""