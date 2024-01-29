# These "XxxxxResponseObjects" are simply wrappers for dictionaries that
# have some fields parsed out as properties to make working with responses
# easier and user code more readable.

from argparse import Namespace
from mlb.statsapi.models import ExtendedDictionary

class ScheduleResponseObject(list):
    '''
    An extended dictionary that gives easy access to commonly accessed
    properties from the sports endpoint response
    '''
    # pylint: disable=missing-function-docstring, multiple-statements
    
    class GameResponseObject(ExtendedDictionary):

        @property
        def game_date(self): return self.get("gameDate")

        @property
        def game_pk(self): return self.get("gamePk")

        @property
        def guid(self): return self.get("gameGuid")

        @property
        def teams(self):
            return Namespace(
                away = self.get("teams.away.team.id"),
                home = self.get("teams.home.team.id"),
            )
            
        @property
        def rule_settings(self): return self.get("ruleSettings")
        
        @property
        def season(self): return self.get("season")
        
        @property
        def status(self): return self.get("status.detailedState")        

        @property
        def timestamp(self): return self.get("time")
        
    @property
    def games(self): 
        games = []
        for date in self:
            games += date.get("games", [])
        return [self.GameResponseObject(game) for game in games]
