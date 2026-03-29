from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional


class VehicleType(Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"


class SpotType(Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"


class TicketStatus(Enum):
    ACTIVE = "active"
    CLOSED = "closed"


@dataclass
class Vehicle:
    license_plate: str
    vehicle_type: VehicleType


@dataclass
class ParkingSpot:
    spot_id: str
    spot_type: SpotType
    parked_vehicle: Optional[Vehicle] = None

    def is_free(self) -> bool:
        return self.parked_vehicle is None

    def can_fit(self, vehicle: Vehicle) -> bool:
        return self.spot_type.value == vehicle.vehicle_type.value

    def assign_vehicle(self, vehicle: Vehicle) -> None:
        if not self.is_free():
            raise ValueError(f"Spot {self.spot_id} is already occupied.")
        if not self.can_fit(vehicle):
            raise ValueError(
                f"Vehicle type {vehicle.vehicle_type.value} cannot fit in spot type {self.spot_type.value}."
            )
        self.parked_vehicle = vehicle

    def remove_vehicle(self) -> None:
        if self.is_free():
            raise ValueError(f"Spot {self.spot_id} is already empty.")
        self.parked_vehicle = None


@dataclass
class Ticket:
    ticket_id: str
    vehicle: Vehicle
    spot: ParkingSpot
    entry_time: datetime = field(default_factory=datetime.now)
    exit_time: Optional[datetime] = None
    status: TicketStatus = TicketStatus.ACTIVE

    def close(self) -> None:
        if self.status == TicketStatus.CLOSED:
            raise ValueError("Ticket is already closed.")
        self.exit_time = datetime.now()
        self.status = TicketStatus.CLOSED


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, ticket: Ticket) -> float:
        pass


class HourlyPricingStrategy(PricingStrategy):
    """
    Simple pricing:
    - Charges per started hour
    - Different rates by vehicle type
    """

    RATES = {
        VehicleType.BIKE: 5.0,
        VehicleType.CAR: 10.0,
        VehicleType.TRUCK: 20.0,
    }

    def calculate_fee(self, ticket: Ticket) -> float:
        if ticket.exit_time is None:
            raise ValueError("Cannot calculate fee before ticket is closed.")

        duration_seconds = (ticket.exit_time - ticket.entry_time).total_seconds()
        hours = max(1, int((duration_seconds + 3599) // 3600))  # round up
        rate = self.RATES[ticket.vehicle.vehicle_type]
        return hours * rate


@dataclass
class ParkingFloor:
    floor_number: int
    spots: List[ParkingSpot]

    def find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        for spot in self.spots:
            if spot.is_free() and spot.can_fit(vehicle):
                return spot
        return None


class ParkingLot:
    def __init__(self, name: str, floors: List[ParkingFloor], pricing_strategy: PricingStrategy):
        self.name = name
        self.floors = floors
        self.pricing_strategy = pricing_strategy
        self.active_tickets: dict[str, Ticket] = {}
        self.ticket_counter = 1

    def _generate_ticket_id(self) -> str:
        ticket_id = f"TICKET-{self.ticket_counter}"
        self.ticket_counter += 1
        return ticket_id

    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                spot.assign_vehicle(vehicle)
                ticket = Ticket(
                    ticket_id=self._generate_ticket_id(),
                    vehicle=vehicle,
                    spot=spot,
                )
                self.active_tickets[ticket.ticket_id] = ticket
                return ticket

        raise ValueError("No available compatible parking spot found.")

    def exit_vehicle(self, ticket_id: str) -> float:
        if ticket_id not in self.active_tickets:
            raise ValueError(f"Ticket {ticket_id} not found or already closed.")

        ticket = self.active_tickets[ticket_id]
        ticket.close()
        fee = self.pricing_strategy.calculate_fee(ticket)
        ticket.spot.remove_vehicle()
        del self.active_tickets[ticket_id]
        return fee

    def display_availability(self) -> None:
        print(f"\nParking Lot: {self.name}")
        for floor in self.floors:
            print(f"  Floor {floor.floor_number}:")
            for spot in floor.spots:
                status = "FREE" if spot.is_free() else f"OCCUPIED by {spot.parked_vehicle.license_plate}"
                print(f"    Spot {spot.spot_id} ({spot.spot_type.value}) -> {status}")


def build_sample_parking_lot() -> ParkingLot:
    floor_1 = ParkingFloor(
        floor_number=1,
        spots=[
            ParkingSpot("F1-S1", SpotType.BIKE),
            ParkingSpot("F1-S2", SpotType.CAR),
            ParkingSpot("F1-S3", SpotType.CAR),
        ],
    )

    floor_2 = ParkingFloor(
        floor_number=2,
        spots=[
            ParkingSpot("F2-S1", SpotType.TRUCK),
            ParkingSpot("F2-S2", SpotType.CAR),
            ParkingSpot("F2-S3", SpotType.BIKE),
        ],
    )

    pricing_strategy = HourlyPricingStrategy()
    return ParkingLot("Microsoft Parking Lot", [floor_1, floor_2], pricing_strategy)


if __name__ == "__main__":
    parking_lot = build_sample_parking_lot()

    bike = Vehicle("BIKE-101", VehicleType.BIKE)
    car = Vehicle("CAR-202", VehicleType.CAR)
    truck = Vehicle("TRUCK-303", VehicleType.TRUCK)

    parking_lot.display_availability()

    print("\n--- Parking Vehicles ---")
    bike_ticket = parking_lot.park_vehicle(bike)
    print(f"Bike parked. Ticket ID: {bike_ticket.ticket_id}, Spot: {bike_ticket.spot.spot_id}")

    car_ticket = parking_lot.park_vehicle(car)
    print(f"Car parked. Ticket ID: {car_ticket.ticket_id}, Spot: {car_ticket.spot.spot_id}")

    truck_ticket = parking_lot.park_vehicle(truck)
    print(f"Truck parked. Ticket ID: {truck_ticket.ticket_id}, Spot: {truck_ticket.spot.spot_id}")

    parking_lot.display_availability()

    print("\n--- Exiting Vehicles ---")
    car_fee = parking_lot.exit_vehicle(car_ticket.ticket_id)
    print(f"Car exited. Fee: {car_fee}")

    bike_fee = parking_lot.exit_vehicle(bike_ticket.ticket_id)
    print(f"Bike exited. Fee: {bike_fee}")

    parking_lot.display_availability()