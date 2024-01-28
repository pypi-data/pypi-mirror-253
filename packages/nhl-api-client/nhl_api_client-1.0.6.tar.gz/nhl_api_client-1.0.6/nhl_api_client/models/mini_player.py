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


T = TypeVar("T", bound="MiniPlayer")


@_attrs_define
class MiniPlayer:
    """
    Attributes:
        player_id (Union[Unset, int]):
        first_initial (Union[Unset, LanguageString]):
        last_name (Union[Unset, LanguageString]):
    """

    player_id: Union[Unset, int] = UNSET
    first_initial: Union[Unset, "LanguageString"] = UNSET
    last_name: Union[Unset, "LanguageString"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id
        first_initial: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first_initial, Unset):
            first_initial = self.first_initial.to_dict()

        last_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_name, Unset):
            last_name = self.last_name.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if first_initial is not UNSET:
            field_dict["firstInitial"] = first_initial
        if last_name is not UNSET:
            field_dict["lastName"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        player_id = d.pop("playerId", UNSET)

        _first_initial = d.pop("firstInitial", UNSET)
        first_initial: Union[Unset, LanguageString]
        if isinstance(_first_initial, Unset):
            first_initial = UNSET
        else:
            first_initial = LanguageString.from_dict(_first_initial)

        _last_name = d.pop("lastName", UNSET)
        last_name: Union[Unset, LanguageString]
        if isinstance(_last_name, Unset):
            last_name = UNSET
        else:
            last_name = LanguageString.from_dict(_last_name)

        mini_player = cls(
            player_id=player_id,
            first_initial=first_initial,
            last_name=last_name,
        )

        mini_player.additional_properties = d
        return mini_player

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
