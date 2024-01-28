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
    from ..models.play_by_play_plays_item import PlayByPlayPlaysItem
    from ..models.play_by_play_period_descriptor import PlayByPlayPeriodDescriptor
    from ..models.play_by_play_away_team import PlayByPlayAwayTeam
    from ..models.play_by_play_game_outcome import PlayByPlayGameOutcome
    from ..models.language_string import LanguageString
    from ..models.play_by_play_roster_spots_item import PlayByPlayRosterSpotsItem
    from ..models.play_by_play_home_team import PlayByPlayHomeTeam
    from ..models.play_by_play_tv_broadcasts_item import PlayByPlayTvBroadcastsItem
    from ..models.play_by_play_clock import PlayByPlayClock
    from ..models.play_by_play_situation import PlayByPlaySituation


T = TypeVar("T", bound="PlayByPlay")


@_attrs_define
class PlayByPlay:
    """
    Attributes:
        id (Union[Unset, int]):
        season (Union[Unset, int]):
        game_type (Union[Unset, int]):
        neutral_site (Union[Unset, bool]):
        game_date (Union[Unset, datetime.date]):
        start_time_utc (Union[Unset, datetime.datetime]):
        eastern_utc_offset (Union[Unset, str]):
        venue_utc_offset (Union[Unset, str]):
        venue_timezone (Union[Unset, str]):
        game_state (Union[Unset, str]):
        game_schedule_state (Union[Unset, str]):
        tickets_link (Union[Unset, str]):
        game_center_link (Union[Unset, str]):
        venue (Union[Unset, LanguageString]):
        tv_broadcasts (Union[Unset, List['PlayByPlayTvBroadcastsItem']]):
        away_team (Union[Unset, PlayByPlayAwayTeam]):
        home_team (Union[Unset, PlayByPlayHomeTeam]):
        period_descriptor (Union[Unset, None, PlayByPlayPeriodDescriptor]):
        game_outcome (Union[Unset, None, PlayByPlayGameOutcome]): If the period ended in regulation or overtime (only
            available in past games)
        clock (Union[Unset, None, PlayByPlayClock]):
        situation (Union[Unset, None, PlayByPlaySituation]):
        situation_code (Union[Unset, str]):
        time_remaining (Union[Unset, str]):
        seconds_remaining (Union[Unset, int]):
        roster_spots (Union[Unset, List['PlayByPlayRosterSpotsItem']]):
        display_period (Union[Unset, str]):
        plays (Union[Unset, List['PlayByPlayPlaysItem']]):
    """

    id: Union[Unset, int] = UNSET
    season: Union[Unset, int] = UNSET
    game_type: Union[Unset, int] = UNSET
    neutral_site: Union[Unset, bool] = UNSET
    game_date: Union[Unset, datetime.date] = UNSET
    start_time_utc: Union[Unset, datetime.datetime] = UNSET
    eastern_utc_offset: Union[Unset, str] = UNSET
    venue_utc_offset: Union[Unset, str] = UNSET
    venue_timezone: Union[Unset, str] = UNSET
    game_state: Union[Unset, str] = UNSET
    game_schedule_state: Union[Unset, str] = UNSET
    tickets_link: Union[Unset, str] = UNSET
    game_center_link: Union[Unset, str] = UNSET
    venue: Union[Unset, "LanguageString"] = UNSET
    tv_broadcasts: Union[Unset, List["PlayByPlayTvBroadcastsItem"]] = UNSET
    away_team: Union[Unset, "PlayByPlayAwayTeam"] = UNSET
    home_team: Union[Unset, "PlayByPlayHomeTeam"] = UNSET
    period_descriptor: Union[Unset, None, "PlayByPlayPeriodDescriptor"] = UNSET
    game_outcome: Union[Unset, None, "PlayByPlayGameOutcome"] = UNSET
    clock: Union[Unset, None, "PlayByPlayClock"] = UNSET
    situation: Union[Unset, None, "PlayByPlaySituation"] = UNSET
    situation_code: Union[Unset, str] = UNSET
    time_remaining: Union[Unset, str] = UNSET
    seconds_remaining: Union[Unset, int] = UNSET
    roster_spots: Union[Unset, List["PlayByPlayRosterSpotsItem"]] = UNSET
    display_period: Union[Unset, str] = UNSET
    plays: Union[Unset, List["PlayByPlayPlaysItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        season = self.season
        game_type = self.game_type
        neutral_site = self.neutral_site
        game_date: Union[Unset, str] = UNSET
        if not isinstance(self.game_date, Unset):
            game_date = self.game_date.isoformat()

        start_time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.start_time_utc, Unset):
            start_time_utc = self.start_time_utc.isoformat()

        eastern_utc_offset = self.eastern_utc_offset
        venue_utc_offset = self.venue_utc_offset
        venue_timezone = self.venue_timezone
        game_state = self.game_state
        game_schedule_state = self.game_schedule_state
        tickets_link = self.tickets_link
        game_center_link = self.game_center_link
        venue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

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

        period_descriptor: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.period_descriptor, Unset):
            period_descriptor = self.period_descriptor.to_dict() if self.period_descriptor else None

        game_outcome: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.game_outcome, Unset):
            game_outcome = self.game_outcome.to_dict() if self.game_outcome else None

        clock: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict() if self.clock else None

        situation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.situation, Unset):
            situation = self.situation.to_dict() if self.situation else None

        situation_code = self.situation_code
        time_remaining = self.time_remaining
        seconds_remaining = self.seconds_remaining
        roster_spots: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roster_spots, Unset):
            roster_spots = []
            for roster_spots_item_data in self.roster_spots:
                roster_spots_item = roster_spots_item_data.to_dict()

                roster_spots.append(roster_spots_item)

        display_period = self.display_period
        plays: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.plays, Unset):
            plays = []
            for plays_item_data in self.plays:
                plays_item = plays_item_data.to_dict()

                plays.append(plays_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if season is not UNSET:
            field_dict["season"] = season
        if game_type is not UNSET:
            field_dict["gameType"] = game_type
        if neutral_site is not UNSET:
            field_dict["neutralSite"] = neutral_site
        if game_date is not UNSET:
            field_dict["gameDate"] = game_date
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
        if tickets_link is not UNSET:
            field_dict["ticketsLink"] = tickets_link
        if game_center_link is not UNSET:
            field_dict["gameCenterLink"] = game_center_link
        if venue is not UNSET:
            field_dict["venue"] = venue
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
        if clock is not UNSET:
            field_dict["clock"] = clock
        if situation is not UNSET:
            field_dict["situation"] = situation
        if situation_code is not UNSET:
            field_dict["situationCode"] = situation_code
        if time_remaining is not UNSET:
            field_dict["timeRemaining"] = time_remaining
        if seconds_remaining is not UNSET:
            field_dict["secondsRemaining"] = seconds_remaining
        if roster_spots is not UNSET:
            field_dict["rosterSpots"] = roster_spots
        if display_period is not UNSET:
            field_dict["displayPeriod"] = display_period
        if plays is not UNSET:
            field_dict["plays"] = plays

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.play_by_play_plays_item import PlayByPlayPlaysItem
        from ..models.play_by_play_period_descriptor import PlayByPlayPeriodDescriptor
        from ..models.play_by_play_away_team import PlayByPlayAwayTeam
        from ..models.play_by_play_game_outcome import PlayByPlayGameOutcome
        from ..models.language_string import LanguageString
        from ..models.play_by_play_roster_spots_item import PlayByPlayRosterSpotsItem
        from ..models.play_by_play_home_team import PlayByPlayHomeTeam
        from ..models.play_by_play_tv_broadcasts_item import PlayByPlayTvBroadcastsItem
        from ..models.play_by_play_clock import PlayByPlayClock
        from ..models.play_by_play_situation import PlayByPlaySituation

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        season = d.pop("season", UNSET)

        game_type = d.pop("gameType", UNSET)

        neutral_site = d.pop("neutralSite", UNSET)

        _game_date = d.pop("gameDate", UNSET)
        game_date: Union[Unset, datetime.date]
        if isinstance(_game_date, Unset):
            game_date = UNSET
        else:
            game_date = isoparse(_game_date).date()

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

        tickets_link = d.pop("ticketsLink", UNSET)

        game_center_link = d.pop("gameCenterLink", UNSET)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, LanguageString]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = LanguageString.from_dict(_venue)

        tv_broadcasts = []
        _tv_broadcasts = d.pop("tvBroadcasts", UNSET)
        for tv_broadcasts_item_data in _tv_broadcasts or []:
            tv_broadcasts_item = PlayByPlayTvBroadcastsItem.from_dict(tv_broadcasts_item_data)

            tv_broadcasts.append(tv_broadcasts_item)

        _away_team = d.pop("awayTeam", UNSET)
        away_team: Union[Unset, PlayByPlayAwayTeam]
        if isinstance(_away_team, Unset):
            away_team = UNSET
        else:
            away_team = PlayByPlayAwayTeam.from_dict(_away_team)

        _home_team = d.pop("homeTeam", UNSET)
        home_team: Union[Unset, PlayByPlayHomeTeam]
        if isinstance(_home_team, Unset):
            home_team = UNSET
        else:
            home_team = PlayByPlayHomeTeam.from_dict(_home_team)

        _period_descriptor = d.pop("periodDescriptor", UNSET)
        period_descriptor: Union[Unset, None, PlayByPlayPeriodDescriptor]
        if _period_descriptor is None:
            period_descriptor = None
        elif isinstance(_period_descriptor, Unset):
            period_descriptor = UNSET
        else:
            period_descriptor = PlayByPlayPeriodDescriptor.from_dict(_period_descriptor)

        _game_outcome = d.pop("gameOutcome", UNSET)
        game_outcome: Union[Unset, None, PlayByPlayGameOutcome]
        if _game_outcome is None:
            game_outcome = None
        elif isinstance(_game_outcome, Unset):
            game_outcome = UNSET
        else:
            game_outcome = PlayByPlayGameOutcome.from_dict(_game_outcome)

        _clock = d.pop("clock", UNSET)
        clock: Union[Unset, None, PlayByPlayClock]
        if _clock is None:
            clock = None
        elif isinstance(_clock, Unset):
            clock = UNSET
        else:
            clock = PlayByPlayClock.from_dict(_clock)

        _situation = d.pop("situation", UNSET)
        situation: Union[Unset, None, PlayByPlaySituation]
        if _situation is None:
            situation = None
        elif isinstance(_situation, Unset):
            situation = UNSET
        else:
            situation = PlayByPlaySituation.from_dict(_situation)

        situation_code = d.pop("situationCode", UNSET)

        time_remaining = d.pop("timeRemaining", UNSET)

        seconds_remaining = d.pop("secondsRemaining", UNSET)

        roster_spots = []
        _roster_spots = d.pop("rosterSpots", UNSET)
        for roster_spots_item_data in _roster_spots or []:
            roster_spots_item = PlayByPlayRosterSpotsItem.from_dict(roster_spots_item_data)

            roster_spots.append(roster_spots_item)

        display_period = d.pop("displayPeriod", UNSET)

        plays = []
        _plays = d.pop("plays", UNSET)
        for plays_item_data in _plays or []:
            plays_item = PlayByPlayPlaysItem.from_dict(plays_item_data)

            plays.append(plays_item)

        play_by_play = cls(
            id=id,
            season=season,
            game_type=game_type,
            neutral_site=neutral_site,
            game_date=game_date,
            start_time_utc=start_time_utc,
            eastern_utc_offset=eastern_utc_offset,
            venue_utc_offset=venue_utc_offset,
            venue_timezone=venue_timezone,
            game_state=game_state,
            game_schedule_state=game_schedule_state,
            tickets_link=tickets_link,
            game_center_link=game_center_link,
            venue=venue,
            tv_broadcasts=tv_broadcasts,
            away_team=away_team,
            home_team=home_team,
            period_descriptor=period_descriptor,
            game_outcome=game_outcome,
            clock=clock,
            situation=situation,
            situation_code=situation_code,
            time_remaining=time_remaining,
            seconds_remaining=seconds_remaining,
            roster_spots=roster_spots,
            display_period=display_period,
            plays=plays,
        )

        play_by_play.additional_properties = d
        return play_by_play

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
