from typing import List, Dict
from dataclasses import dataclass
from datetime import date, time


@dataclass
class Table:
    def __init__(self, id:int, capacity:int):
        self.id = id
        self.capacity = capacity

@dataclass   
class Reservation:
    def __init__(self, date:date, start_time:time, end_time: time):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
    
    def overlap(self, date, start_time, end_time):
        if date == self.date:
            return self.start_time < end_time and start_time < self.end_time
        return False

class ReservationLot:
    def __init__(self, tables: List[Table]):
        self.tables = tables
        self.table_capacity : Dict[int, List[Table]] = {}
        self.reservations : Dict[int, List[Reservation]] = {}
        self.populate_table_map()

    
    def populate_table_map(self):
        for table in self.tables:
            if table.capacity not in self.table_capacity:
                self.table_capacity[table.capacity] = []
            self.table_capacity[table.capacity].append(table)
        return self.table_capacity
    
    def is_table_available(self, table:Table, date, start, end):
        if table.id not in self.reservations:
            self.reservations[table.id] = []
        for reservation in self.reservations[table.id]:
            if reservation.overlap(date,start,end):
                return False
        self.reservations[table.id].append(Reservation(date, start, end))
        return True
                    
    def add_reservation(self, capacity:int, date:date, start:time, end:time):
        for table in self.table_capacity[capacity]:
            if self.is_table_available(table, date, start, end):
                return True
        return False
    

table_1 = Table(1, 2)
table_2 = Table(1, 3)
table_3 = Table(1, 4)
table_4 = Table(1, 5)
table_5 = Table(1, 6)

reservation_lot = ReservationLot([table_1,table_2, table_3, table_4, table_5])

print(reservation_lot.add_reservation(4, date(2026, 1, 21), time(18,30), time(19,30)))

print(reservation_lot.add_reservation(4, date(2026, 1, 21), time(18,30), time(19,30)))


    
    
