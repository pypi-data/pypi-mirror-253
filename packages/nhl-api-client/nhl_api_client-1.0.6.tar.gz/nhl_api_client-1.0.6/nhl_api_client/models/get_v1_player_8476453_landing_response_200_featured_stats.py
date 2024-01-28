from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import Dict

if TYPE_CHECKING:
    from ..models.get_v1_player_8476453_landing_response_200_featured_stats_regular_season import (
        GetV1Player8476453LandingResponse200FeaturedStatsRegularSeason,
    )


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200FeaturedStats")


@_attrs_define
class GetV1Player8476453LandingResponse200FeaturedStats:
    """
    Attributes:
        season (int):
        regular_season (GetV1Player8476453LandingResponse200FeaturedStatsRegularSeason):
    """

    season: int
    regular_season: "GetV1Player8476453LandingResponse200FeaturedStatsRegularSeason"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season = self.season
        regular_season = self.regular_season.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "season": season,
                "regularSeason": regular_season,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_v1_player_8476453_landing_response_200_featured_stats_regular_season import (
            GetV1Player8476453LandingResponse200FeaturedStatsRegularSeason,
        )

        d = src_dict.copy()
        season = d.pop("season")

        regular_season = GetV1Player8476453LandingResponse200FeaturedStatsRegularSeason.from_dict(
            d.pop("regularSeason")
        )

        get_v1_player_8476453_landing_response_200_featured_stats = cls(
            season=season,
            regular_season=regular_season,
        )

        get_v1_player_8476453_landing_response_200_featured_stats.additional_properties = d
        return get_v1_player_8476453_landing_response_200_featured_stats

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
