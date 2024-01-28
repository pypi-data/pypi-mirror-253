from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import List
from typing import Dict
from dateutil.parser import isoparse
import datetime

if TYPE_CHECKING:
    from ..models.tv_broadcast import TVBroadcast
    from ..models.team import Team
    from ..models.language_string import LanguageString
    from ..models.game_clock import GameClock
    from ..models.mini_player import MiniPlayer
    from ..models.game_game_outcome import GameGameOutcome
    from ..models.game_period_descriptor import GamePeriodDescriptor


T = TypeVar("T", bound="Game")


@_attrs_define
class Game:
    """
    Attributes:
        id (Union[Unset, int]):
        season (Union[Unset, int]):
        game_type (Union[Unset, int]):
        game_date (Union[Unset, datetime.date]):
        venue (Union[Unset, LanguageString]):
        neutral_site (Union[Unset, bool]):
        start_time_utc (Union[Unset, datetime.datetime]):
        eastern_utc_offset (Union[Unset, str]):
        venue_utc_offset (Union[Unset, str]):
        venue_timezone (Union[Unset, str]):
        game_state (Union[Unset, str]):
        game_schedule_state (Union[Unset, str]):
        tv_broadcasts (Union[Unset, List['TVBroadcast']]):
        away_team (Union[Unset, Team]):
        home_team (Union[Unset, Team]):
        period_descriptor (Union[Unset, GamePeriodDescriptor]):
        game_outcome (Union[Unset, GameGameOutcome]):
        winning_goalie (Union[Unset, MiniPlayer]):
        winning_goal_scorer (Union[Unset, MiniPlayer]):
        game_center_link (Union[Unset, str]):
        clock (Union[Unset, None, GameClock]):
    """

    id: Union[Unset, int] = UNSET
    season: Union[Unset, int] = UNSET
    game_type: Union[Unset, int] = UNSET
    game_date: Union[Unset, datetime.date] = UNSET
    venue: Union[Unset, "LanguageString"] = UNSET
    neutral_site: Union[Unset, bool] = UNSET
    start_time_utc: Union[Unset, datetime.datetime] = UNSET
    eastern_utc_offset: Union[Unset, str] = UNSET
    venue_utc_offset: Union[Unset, str] = UNSET
    venue_timezone: Union[Unset, str] = UNSET
    game_state: Union[Unset, str] = UNSET
    game_schedule_state: Union[Unset, str] = UNSET
    tv_broadcasts: Union[Unset, List["TVBroadcast"]] = UNSET
    away_team: Union[Unset, "Team"] = UNSET
    home_team: Union[Unset, "Team"] = UNSET
    period_descriptor: Union[Unset, "GamePeriodDescriptor"] = UNSET
    game_outcome: Union[Unset, "GameGameOutcome"] = UNSET
    winning_goalie: Union[Unset, "MiniPlayer"] = UNSET
    winning_goal_scorer: Union[Unset, "MiniPlayer"] = UNSET
    game_center_link: Union[Unset, str] = UNSET
    clock: Union[Unset, None, "GameClock"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        season = self.season
        game_type = self.game_type
        game_date: Union[Unset, str] = UNSET
        if not isinstance(self.game_date, Unset):
            game_date = self.game_date.isoformat()

        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        neutral_site = self.neutral_site
        start_time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.start_time_utc, Unset):
            start_time_utc = self.start_time_utc.isoformat()

        eastern_utc_offset = self.eastern_utc_offset
        venue_utc_offset = self.venue_utc_offset
        venue_timezone = self.venue_timezone
        game_state = self.game_state
        game_schedule_state = self.game_schedule_state
        tv_broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tv_broadcasts, Unset):
            tv_broadcasts = []
            for tv_broadcasts_item_data in self.tv_broadcasts:
                tv_broadcasts_item = tv_broadcasts_item_data.to_dict()

                tv_broadcasts.append(tv_broadcasts_item)

        away_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.away_team, Unset):
            away_team = self.away_team.to_dict()

        home_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_team, Unset):
            home_team = self.home_team.to_dict()

        period_descriptor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period_descriptor, Unset):
            period_descriptor = self.period_descriptor.to_dict()

        game_outcome: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.game_outcome, Unset):
            game_outcome = self.game_outcome.to_dict()

        winning_goalie: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.winning_goalie, Unset):
            winning_goalie = self.winning_goalie.to_dict()

        winning_goal_scorer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.winning_goal_scorer, Unset):
            winning_goal_scorer = self.winning_goal_scorer.to_dict()

        game_center_link = self.game_center_link
        clock: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict() if self.clock else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if season is not UNSET:
            field_dict["season"] = season
        if game_type is not UNSET:
            field_dict["gameType"] = game_type
        if game_date is not UNSET:
            field_dict["gameDate"] = game_date
        if venue is not UNSET:
            field_dict["venue"] = venue
        if neutral_site is not UNSET:
            field_dict["neutralSite"] = neutral_site
        if start_time_utc is not UNSET:
            field_dict["startTimeUTC"] = start_time_utc
        if eastern_utc_offset is not UNSET:
            field_dict["easternUTCOffset"] = eastern_utc_offset
        if venue_utc_offset is not UNSET:
            field_dict["venueUTCOffset"] = venue_utc_offset
        if venue_timezone is not UNSET:
            field_dict["venueTimezone"] = venue_timezone
        if game_state is not UNSET:
            field_dict["gameState"] = game_state
        if game_schedule_state is not UNSET:
            field_dict["gameScheduleState"] = game_schedule_state
        if tv_broadcasts is not UNSET:
            field_dict["tvBroadcasts"] = tv_broadcasts
        if away_team is not UNSET:
            field_dict["awayTeam"] = away_team
        if home_team is not UNSET:
            field_dict["homeTeam"] = home_team
        if period_descriptor is not UNSET:
            field_dict["periodDescriptor"] = period_descriptor
        if game_outcome is not UNSET:
            field_dict["gameOutcome"] = game_outcome
        if winning_goalie is not UNSET:
            field_dict["winningGoalie"] = winning_goalie
        if winning_goal_scorer is not UNSET:
            field_dict["winningGoalScorer"] = winning_goal_scorer
        if game_center_link is not UNSET:
            field_dict["gameCenterLink"] = game_center_link
        if clock is not UNSET:
            field_dict["clock"] = clock

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tv_broadcast import TVBroadcast
        from ..models.team import Team
        from ..models.language_string import LanguageString
        from ..models.game_clock import GameClock
        from ..models.mini_player import MiniPlayer
        from ..models.game_game_outcome import GameGameOutcome
        from ..models.game_period_descriptor import GamePeriodDescriptor

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        season = d.pop("season", UNSET)

        game_type = d.pop("gameType", UNSET)

        _game_date = d.pop("gameDate", UNSET)
        game_date: Union[Unset, datetime.date]
        if isinstance(_game_date, Unset):
            game_date = UNSET
        else:
            game_date = isoparse(_game_date).date()

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, LanguageString]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = LanguageString.from_dict(_venue)

        neutral_site = d.pop("neutralSite", UNSET)

        _start_time_utc = d.pop("startTimeUTC", UNSET)
        start_time_utc: Union[Unset, datetime.datetime]
        if isinstance(_start_time_utc, Unset):
            start_time_utc = UNSET
        else:
            start_time_utc = isoparse(_start_time_utc)

        eastern_utc_offset = d.pop("easternUTCOffset", UNSET)

        venue_utc_offset = d.pop("venueUTCOffset", UNSET)

        venue_timezone = d.pop("venueTimezone", UNSET)

        game_state = d.pop("gameState", UNSET)

        game_schedule_state = d.pop("gameScheduleState", UNSET)

        tv_broadcasts = []
        _tv_broadcasts = d.pop("tvBroadcasts", UNSET)
        for tv_broadcasts_item_data in _tv_broadcasts or []:
            tv_broadcasts_item = TVBroadcast.from_dict(tv_broadcasts_item_data)

            tv_broadcasts.append(tv_broadcasts_item)

        _away_team = d.pop("awayTeam", UNSET)
        away_team: Union[Unset, Team]
        if isinstance(_away_team, Unset):
            away_team = UNSET
        else:
            away_team = Team.from_dict(_away_team)

        _home_team = d.pop("homeTeam", UNSET)
        home_team: Union[Unset, Team]
        if isinstance(_home_team, Unset):
            home_team = UNSET
        else:
            home_team = Team.from_dict(_home_team)

        _period_descriptor = d.pop("periodDescriptor", UNSET)
        period_descriptor: Union[Unset, GamePeriodDescriptor]
        if isinstance(_period_descriptor, Unset):
            period_descriptor = UNSET
        else:
            period_descriptor = GamePeriodDescriptor.from_dict(_period_descriptor)

        _game_outcome = d.pop("gameOutcome", UNSET)
        game_outcome: Union[Unset, GameGameOutcome]
        if isinstance(_game_outcome, Unset):
            game_outcome = UNSET
        else:
            game_outcome = GameGameOutcome.from_dict(_game_outcome)

        _winning_goalie = d.pop("winningGoalie", UNSET)
        winning_goalie: Union[Unset, MiniPlayer]
        if isinstance(_winning_goalie, Unset):
            winning_goalie = UNSET
        else:
            winning_goalie = MiniPlayer.from_dict(_winning_goalie)

        _winning_goal_scorer = d.pop("winningGoalScorer", UNSET)
        winning_goal_scorer: Union[Unset, MiniPlayer]
        if isinstance(_winning_goal_scorer, Unset):
            winning_goal_scorer = UNSET
        else:
            winning_goal_scorer = MiniPlayer.from_dict(_winning_goal_scorer)

        game_center_link = d.pop("gameCenterLink", UNSET)

        _clock = d.pop("clock", UNSET)
        clock: Union[Unset, None, GameClock]
        if _clock is None:
            clock = None
        elif isinstance(_clock, Unset):
            clock = UNSET
        else:
            clock = GameClock.from_dict(_clock)

        game = cls(
            id=id,
            season=season,
            game_type=game_type,
            game_date=game_date,
            venue=venue,
            neutral_site=neutral_site,
            start_time_utc=start_time_utc,
            eastern_utc_offset=eastern_utc_offset,
            venue_utc_offset=venue_utc_offset,
            venue_timezone=venue_timezone,
            game_state=game_state,
            game_schedule_state=game_schedule_state,
            tv_broadcasts=tv_broadcasts,
            away_team=away_team,
            home_team=home_team,
            period_descriptor=period_descriptor,
            game_outcome=game_outcome,
            winning_goalie=winning_goalie,
            winning_goal_scorer=winning_goal_scorer,
            game_center_link=game_center_link,
            clock=clock,
        )

        game.additional_properties = d
        return game

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
