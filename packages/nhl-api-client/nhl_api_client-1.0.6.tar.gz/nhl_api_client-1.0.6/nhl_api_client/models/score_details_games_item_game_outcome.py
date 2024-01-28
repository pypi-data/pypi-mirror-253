from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union


T = TypeVar("T", bound="ScoreDetailsGamesItemGameOutcome")


@_attrs_define
class ScoreDetailsGamesItemGameOutcome:
    """
    Attributes:
        last_period_type (Union[Unset, str]):
        ot_periods (Union[Unset, int]):
    """

    last_period_type: Union[Unset, str] = UNSET
    ot_periods: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_period_type = self.last_period_type
        ot_periods = self.ot_periods

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_period_type is not UNSET:
            field_dict["lastPeriodType"] = last_period_type
        if ot_periods is not UNSET:
            field_dict["otPeriods"] = ot_periods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_period_type = d.pop("lastPeriodType", UNSET)

        ot_periods = d.pop("otPeriods", UNSET)

        score_details_games_item_game_outcome = cls(
            last_period_type=last_period_type,
            ot_periods=ot_periods,
        )

        score_details_games_item_game_outcome.additional_properties = d
        return score_details_games_item_game_outcome

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
