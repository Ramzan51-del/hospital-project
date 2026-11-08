from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Protocol, runtime_checkable


@runtime_checkable
class Identifiable(Protocol):
    

    @property
    def id(self) -> str: ...


@runtime_checkable
class Schedulable(Protocol):
    

    def is_available(self, start: datetime, end: datetime) -> bool: ...


@dataclass
class Patient:
    

    patient_id: str
    name: str
    contact_information: str = ""

    @property
    def id(self) -> str:
        return self.patient_id


@dataclass
class Doctor:
    

    doctor_id: str
    name: str
    specialty: str
    availability: list[tuple[datetime, datetime]] = field(default_factory=list)

    @property
    def id(self) -> str:
        return self.doctor_id

    def is_available(self, start: datetime, end: datetime) -> bool:
        return any(window_start <= start and end <= window_end
                   for window_start, window_end in self.availability)
    


@dataclass
class Room:

    room_id: str
    room_type: str
    availability: list[tuple[datetime, datetime]] = field(default_factory=list)

    @property
    def id(self) -> str:
        return self.room_id

    def is_available(self, start: datetime, end: datetime) -> bool:
        return any(window_start <= start and end <= window_end
                   for window_start, window_end in self.availability)


@dataclass
class Appointment:

    appointment_id: str
    patient: Patient
    doctor: Doctor
    room: Room
    start: datetime
    end: datetime

    @property
    def id(self) -> str:
        return self.appointment_id