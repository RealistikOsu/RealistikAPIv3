from pydantic import BaseModel

class ClanData(BaseModel):
    """Model for basic clan data."""

    id: int
    tag: str
    name: str
    icon_url: str
    
class FullClanData(BaseModel):
    ...
