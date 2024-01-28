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
    from ..models.game import Game


T = TypeVar("T", bound="WeekSchedule")


@_attrs_define
class WeekSchedule:
    """
    Attributes:
        previous_start_date (Union[Unset, datetime.date]):
        current_start_date (Union[Unset, datetime.date]):
        club_timezone (Union[Unset, str]):
        club_utc_offset (Union[Unset, str]):
        games (Union[Unset, List['Game']]):
    """

    previous_start_date: Union[Unset, datetime.date] = UNSET
    current_start_date: Union[Unset, datetime.date] = UNSET
    club_timezone: Union[Unset, str] = UNSET
    club_utc_offset: Union[Unset, str] = UNSET
    games: Union[Unset, List["Game"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        previous_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.previous_start_date, Unset):
            previous_start_date = self.previous_start_date.isoformat()

        current_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.current_start_date, Unset):
            current_start_date = self.current_start_date.isoformat()

        club_timezone = self.club_timezone
        club_utc_offset = self.club_utc_offset
        games: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.games, Unset):
            games = []
            for games_item_data in self.games:
                games_item = games_item_data.to_dict()

                games.append(games_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if previous_start_date is not UNSET:
            field_dict["previousStartDate"] = previous_start_date
        if current_start_date is not UNSET:
            field_dict["currentStartDate"] = current_start_date
        if club_timezone is not UNSET:
            field_dict["clubTimezone"] = club_timezone
        if club_utc_offset is not UNSET:
            field_dict["clubUTCOffset"] = club_utc_offset
        if games is not UNSET:
            field_dict["games"] = games

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.game import Game

        d = src_dict.copy()
        _previous_start_date = d.pop("previousStartDate", UNSET)
        previous_start_date: Union[Unset, datetime.date]
        if isinstance(_previous_start_date, Unset):
            previous_start_date = UNSET
        else:
            previous_start_date = isoparse(_previous_start_date).date()

        _current_start_date = d.pop("currentStartDate", UNSET)
        current_start_date: Union[Unset, datetime.date]
        if isinstance(_current_start_date, Unset):
            current_start_date = UNSET
        else:
            current_start_date = isoparse(_current_start_date).date()

        club_timezone = d.pop("clubTimezone", UNSET)

        club_utc_offset = d.pop("clubUTCOffset", UNSET)

        games = []
        _games = d.pop("games", UNSET)
        for games_item_data in _games or []:
            games_item = Game.from_dict(games_item_data)

            games.append(games_item)

        week_schedule = cls(
            previous_start_date=previous_start_date,
            current_start_date=current_start_date,
            club_timezone=club_timezone,
            club_utc_offset=club_utc_offset,
            games=games,
        )

        week_schedule.additional_properties = d
        return week_schedule

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
