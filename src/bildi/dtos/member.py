from dataclasses import dataclass

@dataclass(frozen=True)
class MemberDTO:
    name: str
    signature: str   
    
__all__ = [
    "MemberDTO",
]
    
