# These "XxxxxResponseObjects" are simply wrappers for dictionaries that
# have some fields parsed out as properties to make working with responses
# easier and user code more readable.

from mlb.statsapi.models import ExtendedDictionary

class GuidsResponseObject(ExtendedDictionary):
    '''
    An extended dictionary that gives easy access to commonly accessed
    properties from the sports endpoint response
    '''
    # pylint: disable=missing-function-docstring, multiple-statements
    
    @property
    def at_bat_number(self): return self.get("atBatNumber")

    @property
    def game_date(self): return self.get("gameDate")

    @property
    def game_mode(self): return self.get("gameMode.id")

    @property
    def game_pk(self): return self.get("gamePk")

    @property
    def guid(self): return self.get("guid")

    @property
    def inning_number(self): return self.get("inning")

    @property
    def inning_half(self): return "top" if self.get("isTopInning") else "bottom"

    @property
    def is_hit(self): return self.get("isHit")

    @property
    def is_pickoff(self): return self.get("isPickoff")

    @property
    def is_pitch(self): return self.get("isPitch")

    @property
    def pitch_number(self): return self.get("pitchNumber")

    @property
    def pickoff_number(self): return self.get("pickoffNumber")

    @property
    def timestamp(self): return self.get("time")
