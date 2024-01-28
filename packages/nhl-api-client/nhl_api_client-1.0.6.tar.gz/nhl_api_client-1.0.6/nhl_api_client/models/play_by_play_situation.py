from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import Dict

if TYPE_CHECKING:
    from ..models.play_by_play_situation_away_team import PlayByPlaySituationAwayTeam
    from ..models.play_by_play_situation_home_team import PlayByPlaySituationHomeTeam


T = TypeVar("T", bound="PlayByPlaySituation")


@_attrs_define
class PlayByPlaySituation:
    """
    Attributes:
        home_team (Union[Unset, PlayByPlaySituationHomeTeam]):
        away_team (Union[Unset, PlayByPlaySituationAwayTeam]):
    """

    home_team: Union[Unset, "PlayByPlaySituationHomeTeam"] = UNSET
    away_team: Union[Unset, "PlayByPlaySituationAwayTeam"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        home_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_team, Unset):
            home_team = self.home_team.to_dict()

        away_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.away_team, Unset):
            away_team = self.away_team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if home_team is not UNSET:
            field_dict["homeTeam"] = home_team
        if away_team is not UNSET:
            field_dict["awayTeam"] = away_team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.play_by_play_situation_away_team import PlayByPlaySituationAwayTeam
        from ..models.play_by_play_situation_home_team import PlayByPlaySituationHomeTeam

        d = src_dict.copy()
        _home_team = d.pop("homeTeam", UNSET)
        home_team: Union[Unset, PlayByPlaySituationHomeTeam]
        if isinstance(_home_team, Unset):
            home_team = UNSET
        else:
            home_team = PlayByPlaySituationHomeTeam.from_dict(_home_team)

        _away_team = d.pop("awayTeam", UNSET)
        away_team: Union[Unset, PlayByPlaySituationAwayTeam]
        if isinstance(_away_team, Unset):
            away_team = UNSET
        else:
            away_team = PlayByPlaySituationAwayTeam.from_dict(_away_team)

        play_by_play_situation = cls(
            home_team=home_team,
            away_team=away_team,
        )

        play_by_play_situation.additional_properties = d
        return play_by_play_situation

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
