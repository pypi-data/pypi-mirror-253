'''Module defining all the statsapi endpoints'''

from argparse import Namespace
from mlb.statsapi.settings import BASE_URL
from mlb.statsapi.models import endpoint_factory
import mlb.statsapi.models as models

# The endpoints are organized into Namespaces that map to the statsapi
# endpoints from the documentation. For example, the boxscore endpoint:
#
# endpoint: /api/v1/game/{{game_pk}}/boxscore
# function: statsapi.game.boxscore(game_pk=...)
#
# Note that all parameters passed to any of these functions need to be
# keyword arguments, they can't be positional args.

# statsapi.attendance(teamId=..., date=...)
attendance = endpoint_factory(
    f"{BASE_URL}/v1/attendance", 
    section="records"
)

bat_tracking = Namespace(

    # statsapi.game.analytics.biomechanics(game_pk=..., play_id=...)
    game = endpoint_factory(
        f"{BASE_URL}/v1/batTracking/game/{{game_pk}}/{{play_id}}"
    ),
)

# statsapi.conferences()
conferences = endpoint_factory(
    f"{BASE_URL}/v1/conferences", 
    section="conferences"
)

# statsapi.divisions()
divisions = endpoint_factory(
    f"{BASE_URL}/v1/divisions", 
    section="divisions"
)

# statsapi.draft(year=...)
draft = endpoint_factory(
    f"{BASE_URL}/v1/draft/{{year}}", 
    section="drafts"
)

game = Namespace(

    # statsapi.game.analytics.biomechanics(game_pk=..., play_id=..., position_id=...)
    analytics = Namespace(
        biomechanics = endpoint_factory(
            f"{BASE_URL}/v1/game/{{game_pk}}/{{play_id}}"
            "/analytics/biomechanics/{{position_id}}"
        ),
    ),

    # statsapi.game.boxscore(game_pk=...)
    boxscore = endpoint_factory(
        f"{BASE_URL}/v1/game/{{game_pk}}/boxscore"
    ),

    # statsapi.game.changes(game_pk=...)
    changes = endpoint_factory(
        f"{BASE_URL}/v1/game/{{game_pk}}/changes"
    ),

    # statsapi.game.context_metrics(game_pk=...)
    context_metrics = endpoint_factory(
        f"{BASE_URL}/v1/game/{{game_pk}}/contextMetrics"
    ),

    feed = Namespace(

        # statsapi.game.feed.live(game_pk=...)
        live = endpoint_factory(
            f"{BASE_URL}/v1.1/game/{{game_pk}}/feed/live"
        ),

        # statsapi.game.feed.color(game_pk=...)
        color = endpoint_factory(
            f"{BASE_URL}/v1/game/{{game_pk}}/feed/color"
        ),
    ),

    # statsapi.game.guids(game_pk=...)
    guids = endpoint_factory(
        f"{BASE_URL}/v1/game/{{game_pk}}/guids",
        section="games",
        return_object_type=models.game.GuidsResponseObject
    ),

    # statsapi.game.linescore(game_pk=...)
    linescore = endpoint_factory(
        f"{BASE_URL}/v1/game/{{game_pk}}/linescore"
    ),

    # statsapi.game.play_by_play(game_pk=...)
    play_by_play = endpoint_factory(
        f"{BASE_URL}/v1/game/{{game_pk}}/playByPlay"
    ),

    # statsapi.game.win_probability(game_pk=...)
    win_probability = endpoint_factory(
        f"{BASE_URL}/v1/game/{{game_pk}}/winProbability"
    ),

    # statsapi.game.with_metrics(game_pk=...)
    with_metrics = endpoint_factory(
        f"{BASE_URL}/v1/game/{{game_pk}}/withMetrics"
    ),
)

# statsapi.game_pace(season=...)
game_pace = endpoint_factory(
    f"{BASE_URL}/v1/game_pace", 
    section="sports"
)

# statsapi.leagues(...)
leagues = endpoint_factory(
    f"{BASE_URL}/v1/leagues", 
    section="leagues"
)

# statsapi.prospects(year=...)
prospects = endpoint_factory(
    f"{BASE_URL}/v1/draft/prospects/{{year}}", 
    section="prospects"
)

# statsapi.schedule(game_pk=...)
schedule = endpoint_factory(
    f"{BASE_URL}/v1/schedule",
    section = "dates",
    return_object_type=models.schedule.ScheduleResponseObject,
)

# statsapi.sports()
sports = endpoint_factory(
    f"{BASE_URL}/v1/sports",
    section="sports"
)

# statsapi.sports()
teams = endpoint_factory(
    f"{BASE_URL}/v1/teams",
    section="teams"
)

weather = Namespace(

    # statsapi.weather.game(game_pk=..., play_id=...)
    game = endpoint_factory(
        f"{BASE_URL}/v1/weather/game/{{game_pk}}/{{play_id}}",
        section = "data",
        return_object_type = models.weather.WeatherResponseObject,
    ),

    # statsapi.weather.game(game_pk=..., roof_type=...)
    forecast = endpoint_factory(
        f"{BASE_URL}/v1/weather/game/{{game_pk}}/forecast/{{roof_type}}"
    ),
)
