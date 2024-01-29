# These "XxxxxResponseObjects" are simply wrappers for dictionaries that
# have some fields parsed out as properties to make working with responses
# easier and user code more readable.

import datetime
from argparse import Namespace
from mlb.statsapi.models import ExtendedDictionary

class WeatherResponseObject(ExtendedDictionary):
    '''
    An extended dictionary that gives easy access to commonly accessed
    properties from the sports endpoint response
    '''
    # pylint: disable=missing-function-docstring, multiple-statements
    
    class Segment(ExtendedDictionary):
        
        @property
        def trajectory(self): 
            return Namespace(
                polynomials = Namespace(
                    x = self.get("trajectoryData.trajectoryPolynomialX"),
                    y = self.get("trajectoryData.trajectoryPolynomialX"),
                    z = self.get("trajectoryData.trajectoryPolynomialX"),
                ),
                confidence = self.get("trajectoryData.trajectoryConfidence.value"),
                location = Namespace(
                    x = self.get("trajectoryData.location.x"),
                    y = self.get("trajectoryData.location.y"),
                    z = self.get("trajectoryData.location.z"),
                ),
                wind_speed = Namespace(
                    side = self.get("trajectoryData.wind_speed.side"),
                    tail = self.get("trajectoryData.wind_speed.tail"),
                    vertical = self.get("trajectoryData.wind_speed.vertical"),
                ),
                apex = self.get("trajectoryData.apex"),
            )
        
        @property
        def landing(self): 
            return Namespace(
                time = self.get("landingData.time"),
                position = Namespace(
                    x = self.get("landingData.position.x"),
                    y = self.get("landingData.position.y"),
                    z = self.get("landingData.position.z"),
                ),
                distance = self.get("landingData.distance"),
                offset_spin = self.get("landingData.offsetSpin"),
                offset_wind = self.get("landingData.offsetWind"),
            )
        
        @property
        def conditions(self): 
            return Namespace(
                pressure = self.get("conditions.pressure"),
                temperature = self.get("conditions.temperature"),
                relative_humidity = self.get("conditions.relativeHumidity"),
                wind_speed = self.get("conditions.wind.speed"),
                wind_direction = self.get("conditions.wind.direction"),
            )
            
        @property
        def timestamp(self): return datetime.datetime.fromisoformat(self.get("conditions.timeStamp"))
        
    @property
    def hit_segment(self):
        return Namespace(
            actual = self.Segment(self.get("hitSegmentActual", {})),
            indoor = self.Segment(self.get("hitSegmentIndoor", {})),
            calm = self.Segment(self.get("hitSegmentCalm", {})),
        )
        
    @property
    def pitch_segment(self):
        return Namespace(
            actual = self.Segment(self.get("pitchSegmentActual", {})),
            indoor = self.Segment(self.get("pitchSegmentIndoor", {})),
            calm = self.Segment(self.get("pitchSegmentCalm", {})),
        )
        
    def get_hit_segment(self, segment): 
        return self.Segment(self.get(f"hitSegment{segment.lower().capitalize()}", {}))
        
    def get_pitch_segment(self, segment): 
        return self.Segment(self.get(f"pitchSegment{segment.lower().capitalize()}", {}))
    