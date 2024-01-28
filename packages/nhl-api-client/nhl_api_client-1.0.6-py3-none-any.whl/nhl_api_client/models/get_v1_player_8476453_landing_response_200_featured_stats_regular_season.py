from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import Dict

if TYPE_CHECKING:
    from ..models.get_v1_player_8476453_landing_response_200_featured_stats_regular_season_career import (
        GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonCareer,
    )
    from ..models.get_v1_player_8476453_landing_response_200_featured_stats_regular_season_sub_season import (
        GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonSubSeason,
    )


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200FeaturedStatsRegularSeason")


@_attrs_define
class GetV1Player8476453LandingResponse200FeaturedStatsRegularSeason:
    """
    Attributes:
        sub_season (GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonSubSeason):
        career (GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonCareer):
    """

    sub_season: "GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonSubSeason"
    career: "GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonCareer"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_season = self.sub_season.to_dict()

        career = self.career.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subSeason": sub_season,
                "career": career,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_v1_player_8476453_landing_response_200_featured_stats_regular_season_career import (
            GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonCareer,
        )
        from ..models.get_v1_player_8476453_landing_response_200_featured_stats_regular_season_sub_season import (
            GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonSubSeason,
        )

        d = src_dict.copy()
        sub_season = GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonSubSeason.from_dict(
            d.pop("subSeason")
        )

        career = GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonCareer.from_dict(d.pop("career"))

        get_v1_player_8476453_landing_response_200_featured_stats_regular_season = cls(
            sub_season=sub_season,
            career=career,
        )

        get_v1_player_8476453_landing_response_200_featured_stats_regular_season.additional_properties = d
        return get_v1_player_8476453_landing_response_200_featured_stats_regular_season

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
