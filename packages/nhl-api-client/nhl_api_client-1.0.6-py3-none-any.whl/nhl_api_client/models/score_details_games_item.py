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
    from ..models.score_details_games_item_home_team import ScoreDetailsGamesItemHomeTeam
    from ..models.score_details_games_item_period_descriptor import ScoreDetailsGamesItemPeriodDescriptor
    from ..models.score_details_games_item_clock import ScoreDetailsGamesItemClock
    from ..models.language_string import LanguageString
    from ..models.score_details_games_item_game_outcome import ScoreDetailsGamesItemGameOutcome
    from ..models.score_details_games_item_away_team import ScoreDetailsGamesItemAwayTeam
    from ..models.score_details_games_item_goals_item import ScoreDetailsGamesItemGoalsItem
    from ..models.score_details_games_item_tv_broadcasts_item import ScoreDetailsGamesItemTvBroadcastsItem


T = TypeVar("T", bound="ScoreDetailsGamesItem")


@_attrs_define
class ScoreDetailsGamesItem:
    """
    Attributes:
        id (Union[Unset, int]):
        season (Union[Unset, int]):
        game_type (Union[Unset, int]):
        game_date (Union[Unset, datetime.date]):
        venue (Union[Unset, LanguageString]):
        start_time_utc (Union[Unset, datetime.datetime]):
        eastern_utc_offset (Union[Unset, str]):
        venue_utc_offset (Union[Unset, str]):
        tv_broadcasts (Union[Unset, List['ScoreDetailsGamesItemTvBroadcastsItem']]):
        game_state (Union[Unset, str]):
        game_schedule_state (Union[Unset, str]):
        away_team (Union[Unset, ScoreDetailsGamesItemAwayTeam]):
        home_team (Union[Unset, ScoreDetailsGamesItemHomeTeam]):
        game_center_link (Union[Unset, str]):
        three_min_recap (Union[Unset, str]):
        three_min_recap_fr (Union[Unset, str]):
        clock (Union[Unset, None, ScoreDetailsGamesItemClock]):
        neutral_site (Union[Unset, bool]):
        venue_timezone (Union[Unset, str]):
        period (Union[Unset, int]):
        period_descriptor (Union[Unset, ScoreDetailsGamesItemPeriodDescriptor]):
        game_outcome (Union[Unset, ScoreDetailsGamesItemGameOutcome]):
        goals (Union[Unset, List['ScoreDetailsGamesItemGoalsItem']]):
    """

    id: Union[Unset, int] = UNSET
    season: Union[Unset, int] = UNSET
    game_type: Union[Unset, int] = UNSET
    game_date: Union[Unset, datetime.date] = UNSET
    venue: Union[Unset, "LanguageString"] = UNSET
    start_time_utc: Union[Unset, datetime.datetime] = UNSET
    eastern_utc_offset: Union[Unset, str] = UNSET
    venue_utc_offset: Union[Unset, str] = UNSET
    tv_broadcasts: Union[Unset, List["ScoreDetailsGamesItemTvBroadcastsItem"]] = UNSET
    game_state: Union[Unset, str] = UNSET
    game_schedule_state: Union[Unset, str] = UNSET
    away_team: Union[Unset, "ScoreDetailsGamesItemAwayTeam"] = UNSET
    home_team: Union[Unset, "ScoreDetailsGamesItemHomeTeam"] = UNSET
    game_center_link: Union[Unset, str] = UNSET
    three_min_recap: Union[Unset, str] = UNSET
    three_min_recap_fr: Union[Unset, str] = UNSET
    clock: Union[Unset, None, "ScoreDetailsGamesItemClock"] = UNSET
    neutral_site: Union[Unset, bool] = UNSET
    venue_timezone: Union[Unset, str] = UNSET
    period: Union[Unset, int] = UNSET
    period_descriptor: Union[Unset, "ScoreDetailsGamesItemPeriodDescriptor"] = UNSET
    game_outcome: Union[Unset, "ScoreDetailsGamesItemGameOutcome"] = UNSET
    goals: Union[Unset, List["ScoreDetailsGamesItemGoalsItem"]] = UNSET
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

        start_time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.start_time_utc, Unset):
            start_time_utc = self.start_time_utc.isoformat()

        eastern_utc_offset = self.eastern_utc_offset
        venue_utc_offset = self.venue_utc_offset
        tv_broadcasts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tv_broadcasts, Unset):
            tv_broadcasts = []
            for tv_broadcasts_item_data in self.tv_broadcasts:
                tv_broadcasts_item = tv_broadcasts_item_data.to_dict()

                tv_broadcasts.append(tv_broadcasts_item)

        game_state = self.game_state
        game_schedule_state = self.game_schedule_state
        away_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.away_team, Unset):
            away_team = self.away_team.to_dict()

        home_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_team, Unset):
            home_team = self.home_team.to_dict()

        game_center_link = self.game_center_link
        three_min_recap = self.three_min_recap
        three_min_recap_fr = self.three_min_recap_fr
        clock: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict() if self.clock else None

        neutral_site = self.neutral_site
        venue_timezone = self.venue_timezone
        period = self.period
        period_descriptor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period_descriptor, Unset):
            period_descriptor = self.period_descriptor.to_dict()

        game_outcome: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.game_outcome, Unset):
            game_outcome = self.game_outcome.to_dict()

        goals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.goals, Unset):
            goals = []
            for goals_item_data in self.goals:
                goals_item = goals_item_data.to_dict()

                goals.append(goals_item)

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
        if start_time_utc is not UNSET:
            field_dict["startTimeUTC"] = start_time_utc
        if eastern_utc_offset is not UNSET:
            field_dict["easternUTCOffset"] = eastern_utc_offset
        if venue_utc_offset is not UNSET:
            field_dict["venueUTCOffset"] = venue_utc_offset
        if tv_broadcasts is not UNSET:
            field_dict["tvBroadcasts"] = tv_broadcasts
        if game_state is not UNSET:
            field_dict["gameState"] = game_state
        if game_schedule_state is not UNSET:
            field_dict["gameScheduleState"] = game_schedule_state
        if away_team is not UNSET:
            field_dict["awayTeam"] = away_team
        if home_team is not UNSET:
            field_dict["homeTeam"] = home_team
        if game_center_link is not UNSET:
            field_dict["gameCenterLink"] = game_center_link
        if three_min_recap is not UNSET:
            field_dict["threeMinRecap"] = three_min_recap
        if three_min_recap_fr is not UNSET:
            field_dict["threeMinRecapFr"] = three_min_recap_fr
        if clock is not UNSET:
            field_dict["clock"] = clock
        if neutral_site is not UNSET:
            field_dict["neutralSite"] = neutral_site
        if venue_timezone is not UNSET:
            field_dict["venueTimezone"] = venue_timezone
        if period is not UNSET:
            field_dict["period"] = period
        if period_descriptor is not UNSET:
            field_dict["periodDescriptor"] = period_descriptor
        if game_outcome is not UNSET:
            field_dict["gameOutcome"] = game_outcome
        if goals is not UNSET:
            field_dict["goals"] = goals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.score_details_games_item_home_team import ScoreDetailsGamesItemHomeTeam
        from ..models.score_details_games_item_period_descriptor import ScoreDetailsGamesItemPeriodDescriptor
        from ..models.score_details_games_item_clock import ScoreDetailsGamesItemClock
        from ..models.language_string import LanguageString
        from ..models.score_details_games_item_game_outcome import ScoreDetailsGamesItemGameOutcome
        from ..models.score_details_games_item_away_team import ScoreDetailsGamesItemAwayTeam
        from ..models.score_details_games_item_goals_item import ScoreDetailsGamesItemGoalsItem
        from ..models.score_details_games_item_tv_broadcasts_item import ScoreDetailsGamesItemTvBroadcastsItem

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

        _start_time_utc = d.pop("startTimeUTC", UNSET)
        start_time_utc: Union[Unset, datetime.datetime]
        if isinstance(_start_time_utc, Unset):
            start_time_utc = UNSET
        else:
            start_time_utc = isoparse(_start_time_utc)

        eastern_utc_offset = d.pop("easternUTCOffset", UNSET)

        venue_utc_offset = d.pop("venueUTCOffset", UNSET)

        tv_broadcasts = []
        _tv_broadcasts = d.pop("tvBroadcasts", UNSET)
        for tv_broadcasts_item_data in _tv_broadcasts or []:
            tv_broadcasts_item = ScoreDetailsGamesItemTvBroadcastsItem.from_dict(tv_broadcasts_item_data)

            tv_broadcasts.append(tv_broadcasts_item)

        game_state = d.pop("gameState", UNSET)

        game_schedule_state = d.pop("gameScheduleState", UNSET)

        _away_team = d.pop("awayTeam", UNSET)
        away_team: Union[Unset, ScoreDetailsGamesItemAwayTeam]
        if isinstance(_away_team, Unset):
            away_team = UNSET
        else:
            away_team = ScoreDetailsGamesItemAwayTeam.from_dict(_away_team)

        _home_team = d.pop("homeTeam", UNSET)
        home_team: Union[Unset, ScoreDetailsGamesItemHomeTeam]
        if isinstance(_home_team, Unset):
            home_team = UNSET
        else:
            home_team = ScoreDetailsGamesItemHomeTeam.from_dict(_home_team)

        game_center_link = d.pop("gameCenterLink", UNSET)

        three_min_recap = d.pop("threeMinRecap", UNSET)

        three_min_recap_fr = d.pop("threeMinRecapFr", UNSET)

        _clock = d.pop("clock", UNSET)
        clock: Union[Unset, None, ScoreDetailsGamesItemClock]
        if _clock is None:
            clock = None
        elif isinstance(_clock, Unset):
            clock = UNSET
        else:
            clock = ScoreDetailsGamesItemClock.from_dict(_clock)

        neutral_site = d.pop("neutralSite", UNSET)

        venue_timezone = d.pop("venueTimezone", UNSET)

        period = d.pop("period", UNSET)

        _period_descriptor = d.pop("periodDescriptor", UNSET)
        period_descriptor: Union[Unset, ScoreDetailsGamesItemPeriodDescriptor]
        if isinstance(_period_descriptor, Unset):
            period_descriptor = UNSET
        else:
            period_descriptor = ScoreDetailsGamesItemPeriodDescriptor.from_dict(_period_descriptor)

        _game_outcome = d.pop("gameOutcome", UNSET)
        game_outcome: Union[Unset, ScoreDetailsGamesItemGameOutcome]
        if isinstance(_game_outcome, Unset):
            game_outcome = UNSET
        else:
            game_outcome = ScoreDetailsGamesItemGameOutcome.from_dict(_game_outcome)

        goals = []
        _goals = d.pop("goals", UNSET)
        for goals_item_data in _goals or []:
            goals_item = ScoreDetailsGamesItemGoalsItem.from_dict(goals_item_data)

            goals.append(goals_item)

        score_details_games_item = cls(
            id=id,
            season=season,
            game_type=game_type,
            game_date=game_date,
            venue=venue,
            start_time_utc=start_time_utc,
            eastern_utc_offset=eastern_utc_offset,
            venue_utc_offset=venue_utc_offset,
            tv_broadcasts=tv_broadcasts,
            game_state=game_state,
            game_schedule_state=game_schedule_state,
            away_team=away_team,
            home_team=home_team,
            game_center_link=game_center_link,
            three_min_recap=three_min_recap,
            three_min_recap_fr=three_min_recap_fr,
            clock=clock,
            neutral_site=neutral_site,
            venue_timezone=venue_timezone,
            period=period,
            period_descriptor=period_descriptor,
            game_outcome=game_outcome,
            goals=goals,
        )

        score_details_games_item.additional_properties = d
        return score_details_games_item

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
