from functools import cached_property
from enum import IntEnum

class CustomMode(IntEnum):
    """The custom server-side mod based modes."""
    VANILLA = 0
    RELAX = 1
    AUTOPILOT = 2
    
    @cached_property
    def db_suffix(self) -> str:
        """The MySQL and Redis database suffixes for the mode."""
        
        return _CMODE_DB_SUFFIXES[self]
    
    @cached_property
    def short_name(self) -> str:
        return _CMODE_SHORT_NAMES[self]
    
class Mode(IntEnum):
    """In-game modes."""
    
    STANDARD = 0
    TAIKO = 1
    CATCH = 2
    MANIA = 3
    
    @cached_property
    def db_name(self) -> str:
        """The string used to represent the mode within the database."""
        
        return _MODE_DB_NAME[self]

    @cached_property
    def name(self) -> str:
        return _MODE_NAME[self]
        
_CMODE_DB_SUFFIXES = {
    CustomMode.VANILLA: "",
    CustomMode.RELAX: "_relax",
    CustomMode.AUTOPILOT: "_ap",
}

# TODO: Probably rename?
_CMODE_SHORT_NAMES = {
    CustomMode.VANILLA: "vn",
    CustomMode.RELAX: "rx",
    CustomMode.AUTOPILOT: "ap",
}

_MODE_DB_NAME = {
    Mode.STANDARD: "std",
    Mode.TAIKO: "taiko",
    Mode.CATCH: "ctb",
    Mode.MANIA: "mania",
}

# I could probably use Mode.title (or something like that) however it
# is possible we may change these later.
_MODE_NAME = {
    Mode.STANDARD: "standard",
    Mode.TAIKO: "taiko",
    Mode.CATCH: "catch",
    Mode.MANIA: "mania",
}
