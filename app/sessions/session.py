from dataclasses import dataclass

@dataclass
class UserSession:
    id: int
    name: str
    privileges: int
    expiry: int
