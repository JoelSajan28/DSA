from enum import Enum
from dataclasses import dataclass
from typing import List
from abc import ABC, abstractmethod 
from datetime import datetime

class VehicleType(Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"

@dataclass
class Vehicle:
    license_plate: str
    vehicle_type: VehicleType

@dataclass
class Spot:
    def __init__(self, id:int, type: VehicleType):
        self.spot_id = id
        self.type = type
        self.is_available = False

@dataclass
class Floor:
    def __init__(self, id, spots: List[Spot]):
        self.floor_id = id
        self.spots = spots


@dataclass
class Ticket:
    def __init__(self, id, spot, vehicle_type, license_number):
        self.id = id 
        self.spot = spot 
        self.vehicle_type = vehicle_type
        self.license_number = license_number
    
    def set_entry_time(self, time):
        if self.entry_time:
            raise ValueError("Entry time already exist")
        self.entry_time = datetime.now()
    
    def set_exit_time(self, time):
        if self.exit_time:
            raise ValueError("Ticket had already been closed")
        self.exit_time = datetime.now()


class PaymentStatergy(ABC):
    @abstractmethod
    def calculate_fee(self, ticket: Ticket) -> float:
        pass

class HourlyPaymentStatergy(PaymentStatergy):
    vehicle_charges = {
        VehicleType.BIKE: 5.0,
        VehicleType.CAR: 10.0,
        VehicleType.TRUCK: 20.0,
    }

    def calculate_fee(self, ticket):
        if ticket.exit_time is None:
            raise ValueError("Cannot close a ticket with no value")
        duration_seconds = (ticket.entry_time - ticket.exit_time).total_seconds()
        hours = max(1, int((duration_seconds + 3599) // 3600))
        rate = self.RATES[ticket.vehicle.vehicle_type]
        return hours * rate


class ParkingLot():
    def __init__(self,floors: List[Floor]):
        self.floors = floors
    

    def get_spot(vehicle: Vehicle):
        pass



    