from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import Dict

if TYPE_CHECKING:
    from ..models.get_v1_player_8476453_landing_response_200_career_totals_regular_season import (
        GetV1Player8476453LandingResponse200CareerTotalsRegularSeason,
    )
    from ..models.get_v1_player_8476453_landing_response_200_career_totals_playoffs import (
        GetV1Player8476453LandingResponse200CareerTotalsPlayoffs,
    )


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200CareerTotals")


@_attrs_define
class GetV1Player8476453LandingResponse200CareerTotals:
    """
    Attributes:
        regular_season (GetV1Player8476453LandingResponse200CareerTotalsRegularSeason):
        playoffs (GetV1Player8476453LandingResponse200CareerTotalsPlayoffs):
    """

    regular_season: "GetV1Player8476453LandingResponse200CareerTotalsRegularSeason"
    playoffs: "GetV1Player8476453LandingResponse200CareerTotalsPlayoffs"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        regular_season = self.regular_season.to_dict()

        playoffs = self.playoffs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regularSeason": regular_season,
                "playoffs": playoffs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_v1_player_8476453_landing_response_200_career_totals_regular_season import (
            GetV1Player8476453LandingResponse200CareerTotalsRegularSeason,
        )
        from ..models.get_v1_player_8476453_landing_response_200_career_totals_playoffs import (
            GetV1Player8476453LandingResponse200CareerTotalsPlayoffs,
        )

        d = src_dict.copy()
        regular_season = GetV1Player8476453LandingResponse200CareerTotalsRegularSeason.from_dict(d.pop("regularSeason"))

        playoffs = GetV1Player8476453LandingResponse200CareerTotalsPlayoffs.from_dict(d.pop("playoffs"))

        get_v1_player_8476453_landing_response_200_career_totals = cls(
            regular_season=regular_season,
            playoffs=playoffs,
        )

        get_v1_player_8476453_landing_response_200_career_totals.additional_properties = d
        return get_v1_player_8476453_landing_response_200_career_totals

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
