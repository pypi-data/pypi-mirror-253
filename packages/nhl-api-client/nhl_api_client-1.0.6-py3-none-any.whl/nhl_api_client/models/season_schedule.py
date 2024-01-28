from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from ..models.game import Game


T = TypeVar("T", bound="SeasonSchedule")


@_attrs_define
class SeasonSchedule:
    """
    Attributes:
        previous_season (Union[Unset, str]):
        current_season (Union[Unset, str]):
        club_timezone (Union[Unset, str]):
        club_utc_offset (Union[Unset, str]):
        games (Union[Unset, List['Game']]):
    """

    previous_season: Union[Unset, str] = UNSET
    current_season: Union[Unset, str] = UNSET
    club_timezone: Union[Unset, str] = UNSET
    club_utc_offset: Union[Unset, str] = UNSET
    games: Union[Unset, List["Game"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        previous_season = self.previous_season
        current_season = self.current_season
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
        if previous_season is not UNSET:
            field_dict["previousSeason"] = previous_season
        if current_season is not UNSET:
            field_dict["currentSeason"] = current_season
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
        previous_season = d.pop("previousSeason", UNSET)

        current_season = d.pop("currentSeason", UNSET)

        club_timezone = d.pop("clubTimezone", UNSET)

        club_utc_offset = d.pop("clubUTCOffset", UNSET)

        games = []
        _games = d.pop("games", UNSET)
        for games_item_data in _games or []:
            games_item = Game.from_dict(games_item_data)

            games.append(games_item)

        season_schedule = cls(
            previous_season=previous_season,
            current_season=current_season,
            club_timezone=club_timezone,
            club_utc_offset=club_utc_offset,
            games=games,
        )

        season_schedule.additional_properties = d
        return season_schedule

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
