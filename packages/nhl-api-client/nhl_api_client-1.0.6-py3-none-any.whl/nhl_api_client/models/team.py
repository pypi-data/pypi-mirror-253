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


T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        id (Union[Unset, int]):
        place_name (Union[Unset, LanguageString]):
        name (Union[Unset, LanguageString]):
        abbrev (Union[Unset, str]):
        logo (Union[Unset, str]):
        dark_logo (Union[Unset, str]):
        score (Union[Unset, int]):
        away_team_split (Union[Unset, None, bool]): Only available from certain endpoints, and when the team is away
        home_team_split (Union[Unset, None, bool]): Only available from certain endpoints, and when the team is home
    """

    id: Union[Unset, int] = UNSET
    place_name: Union[Unset, "LanguageString"] = UNSET
    name: Union[Unset, "LanguageString"] = UNSET
    abbrev: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    dark_logo: Union[Unset, str] = UNSET
    score: Union[Unset, int] = UNSET
    away_team_split: Union[Unset, None, bool] = UNSET
    home_team_split: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        place_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.place_name, Unset):
            place_name = self.place_name.to_dict()

        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        abbrev = self.abbrev
        logo = self.logo
        dark_logo = self.dark_logo
        score = self.score
        away_team_split = self.away_team_split
        home_team_split = self.home_team_split

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if place_name is not UNSET:
            field_dict["placeName"] = place_name
        if name is not UNSET:
            field_dict["name"] = name
        if abbrev is not UNSET:
            field_dict["abbrev"] = abbrev
        if logo is not UNSET:
            field_dict["logo"] = logo
        if dark_logo is not UNSET:
            field_dict["darkLogo"] = dark_logo
        if score is not UNSET:
            field_dict["score"] = score
        if away_team_split is not UNSET:
            field_dict["awayTeamSplit"] = away_team_split
        if home_team_split is not UNSET:
            field_dict["homeTeamSplit"] = home_team_split

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _place_name = d.pop("placeName", UNSET)
        place_name: Union[Unset, LanguageString]
        if isinstance(_place_name, Unset):
            place_name = UNSET
        else:
            place_name = LanguageString.from_dict(_place_name)

        _name = d.pop("name", UNSET)
        name: Union[Unset, LanguageString]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = LanguageString.from_dict(_name)

        abbrev = d.pop("abbrev", UNSET)

        logo = d.pop("logo", UNSET)

        dark_logo = d.pop("darkLogo", UNSET)

        score = d.pop("score", UNSET)

        away_team_split = d.pop("awayTeamSplit", UNSET)

        home_team_split = d.pop("homeTeamSplit", UNSET)

        team = cls(
            id=id,
            place_name=place_name,
            name=name,
            abbrev=abbrev,
            logo=logo,
            dark_logo=dark_logo,
            score=score,
            away_team_split=away_team_split,
            home_team_split=home_team_split,
        )

        team.additional_properties = d
        return team

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
