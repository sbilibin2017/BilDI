from dataclasses import dataclass
from typing import Protocol, TypeVar, NewType

Interface = NewType("Interface", Protocol)
Implementation = NewType("Implementation", object)
RegistrationKey= NewType("RegistrationKey", str) 

@dataclass(frozen=True)
class RegistrationDTO:
    interface: Interface
    implementation: Implementation
    
__all__ = [
    "Interface",
    "Implementation",
    "RegistrationKey",
    "RegistrationDTO",
]