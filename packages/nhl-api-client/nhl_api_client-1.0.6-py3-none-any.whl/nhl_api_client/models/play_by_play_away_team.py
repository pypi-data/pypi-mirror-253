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
    from ..models.play_by_play_away_team_on_ice_item import PlayByPlayAwayTeamOnIceItem
    from ..models.language_string import LanguageString


T = TypeVar("T", bound="PlayByPlayAwayTeam")


@_attrs_define
class PlayByPlayAwayTeam:
    """
    Attributes:
        id (Union[Unset, int]):
        abbrev (Union[Unset, str]):
        logo (Union[Unset, str]):
        dark_logo (Union[Unset, str]):
        radio_link (Union[Unset, str]):
        name (Union[Unset, LanguageString]):
        score (Union[Unset, int]):
        sog (Union[Unset, None, int]):
        on_ice (Union[Unset, List['PlayByPlayAwayTeamOnIceItem']]):
    """

    id: Union[Unset, int] = UNSET
    abbrev: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    dark_logo: Union[Unset, str] = UNSET
    radio_link: Union[Unset, str] = UNSET
    name: Union[Unset, "LanguageString"] = UNSET
    score: Union[Unset, int] = UNSET
    sog: Union[Unset, None, int] = UNSET
    on_ice: Union[Unset, List["PlayByPlayAwayTeamOnIceItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        abbrev = self.abbrev
        logo = self.logo
        dark_logo = self.dark_logo
        radio_link = self.radio_link
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        score = self.score
        sog = self.sog
        on_ice: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.on_ice, Unset):
            on_ice = []
            for on_ice_item_data in self.on_ice:
                on_ice_item = on_ice_item_data.to_dict()

                on_ice.append(on_ice_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if abbrev is not UNSET:
            field_dict["abbrev"] = abbrev
        if logo is not UNSET:
            field_dict["logo"] = logo
        if dark_logo is not UNSET:
            field_dict["darkLogo"] = dark_logo
        if radio_link is not UNSET:
            field_dict["radioLink"] = radio_link
        if name is not UNSET:
            field_dict["name"] = name
        if score is not UNSET:
            field_dict["score"] = score
        if sog is not UNSET:
            field_dict["sog"] = sog
        if on_ice is not UNSET:
            field_dict["onIce"] = on_ice

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.play_by_play_away_team_on_ice_item import PlayByPlayAwayTeamOnIceItem
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        abbrev = d.pop("abbrev", UNSET)

        logo = d.pop("logo", UNSET)

        dark_logo = d.pop("darkLogo", UNSET)

        radio_link = d.pop("radioLink", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, LanguageString]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = LanguageString.from_dict(_name)

        score = d.pop("score", UNSET)

        sog = d.pop("sog", UNSET)

        on_ice = []
        _on_ice = d.pop("onIce", UNSET)
        for on_ice_item_data in _on_ice or []:
            on_ice_item = PlayByPlayAwayTeamOnIceItem.from_dict(on_ice_item_data)

            on_ice.append(on_ice_item)

        play_by_play_away_team = cls(
            id=id,
            abbrev=abbrev,
            logo=logo,
            dark_logo=dark_logo,
            radio_link=radio_link,
            name=name,
            score=score,
            sog=sog,
            on_ice=on_ice,
        )

        play_by_play_away_team.additional_properties = d
        return play_by_play_away_team

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
