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


T = TypeVar("T", bound="ScoreDetailsGamesItemHomeTeam")


@_attrs_define
class ScoreDetailsGamesItemHomeTeam:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, LanguageString]):
        abbrev (Union[Unset, str]):
        score (Union[Unset, None, int]):
        sog (Union[Unset, None, int]):
        logo (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, "LanguageString"] = UNSET
    abbrev: Union[Unset, str] = UNSET
    score: Union[Unset, None, int] = UNSET
    sog: Union[Unset, None, int] = UNSET
    logo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        abbrev = self.abbrev
        score = self.score
        sog = self.sog
        logo = self.logo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if abbrev is not UNSET:
            field_dict["abbrev"] = abbrev
        if score is not UNSET:
            field_dict["score"] = score
        if sog is not UNSET:
            field_dict["sog"] = sog
        if logo is not UNSET:
            field_dict["logo"] = logo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, LanguageString]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = LanguageString.from_dict(_name)

        abbrev = d.pop("abbrev", UNSET)

        score = d.pop("score", UNSET)

        sog = d.pop("sog", UNSET)

        logo = d.pop("logo", UNSET)

        score_details_games_item_home_team = cls(
            id=id,
            name=name,
            abbrev=abbrev,
            score=score,
            sog=sog,
            logo=logo,
        )

        score_details_games_item_home_team.additional_properties = d
        return score_details_games_item_home_team

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
