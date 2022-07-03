from enum import IntEnum

class RankedStatus(IntEnum):
    """Beatmap ranked statuses"""
    
    NOT_SUBMITTED = -1
    PENDING = 0
    UPDATE_AVAILABLE = 1
    RANKED = 2
    APPROVED = 3
    QUALIFIED = 4
    LOVED = 5
