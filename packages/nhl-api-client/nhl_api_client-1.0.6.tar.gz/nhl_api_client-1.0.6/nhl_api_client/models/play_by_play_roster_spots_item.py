from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import Dict

if TYPE_CHECKING:
    from ..models.language_string import LanguageString


T = TypeVar("T", bound="PlayByPlayRosterSpotsItem")


@_attrs_define
class PlayByPlayRosterSpotsItem:
    """
    Attributes:
        team_id (Union[Unset, int]):
        player_id (Union[Unset, int]):
        first_name (Union[Unset, LanguageString]):
        last_name (Union[Unset, LanguageString]):
        sweater_number (Union[Unset, int]):
        position_code (Union[Unset, str]):
        headshot (Union[Unset, str]):
    """

    team_id: Union[Unset, int] = UNSET
    player_id: Union[Unset, int] = UNSET
    first_name: Union[Unset, "LanguageString"] = UNSET
    last_name: Union[Unset, "LanguageString"] = UNSET
    sweater_number: Union[Unset, int] = UNSET
    position_code: Union[Unset, str] = UNSET
    headshot: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        player_id = self.player_id
        first_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first_name, Unset):
            first_name = self.first_name.to_dict()

        last_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_name, Unset):
            last_name = self.last_name.to_dict()

        sweater_number = self.sweater_number
        position_code = self.position_code
        headshot = self.headshot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if sweater_number is not UNSET:
            field_dict["sweaterNumber"] = sweater_number
        if position_code is not UNSET:
            field_dict["positionCode"] = position_code
        if headshot is not UNSET:
            field_dict["headshot"] = headshot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        team_id = d.pop("teamId", UNSET)

        player_id = d.pop("playerId", UNSET)

        _first_name = d.pop("firstName", UNSET)
        first_name: Union[Unset, LanguageString]
        if isinstance(_first_name, Unset):
            first_name = UNSET
        else:
            first_name = LanguageString.from_dict(_first_name)

        _last_name = d.pop("lastName", UNSET)
        last_name: Union[Unset, LanguageString]
        if isinstance(_last_name, Unset):
            last_name = UNSET
        else:
            last_name = LanguageString.from_dict(_last_name)

        sweater_number = d.pop("sweaterNumber", UNSET)

        position_code = d.pop("positionCode", UNSET)

        headshot = d.pop("headshot", UNSET)

        play_by_play_roster_spots_item = cls(
            team_id=team_id,
            player_id=player_id,
            first_name=first_name,
            last_name=last_name,
            sweater_number=sweater_number,
            position_code=position_code,
            headshot=headshot,
        )

        play_by_play_roster_spots_item.additional_properties = d
        return play_by_play_roster_spots_item

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
