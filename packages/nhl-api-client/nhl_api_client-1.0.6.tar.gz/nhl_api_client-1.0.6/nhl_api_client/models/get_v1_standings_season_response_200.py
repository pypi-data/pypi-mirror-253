from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import List
from typing import Dict

if TYPE_CHECKING:
    from ..models.get_v1_standings_season_response_200_seasons_item import GetV1StandingsSeasonResponse200SeasonsItem


T = TypeVar("T", bound="GetV1StandingsSeasonResponse200")


@_attrs_define
class GetV1StandingsSeasonResponse200:
    """
    Attributes:
        current_date (str):
        seasons (List['GetV1StandingsSeasonResponse200SeasonsItem']):
    """

    current_date: str
    seasons: List["GetV1StandingsSeasonResponse200SeasonsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_date = self.current_date
        seasons = []
        for seasons_item_data in self.seasons:
            seasons_item = seasons_item_data.to_dict()

            seasons.append(seasons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentDate": current_date,
                "seasons": seasons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_v1_standings_season_response_200_seasons_item import (
            GetV1StandingsSeasonResponse200SeasonsItem,
        )

        d = src_dict.copy()
        current_date = d.pop("currentDate")

        seasons = []
        _seasons = d.pop("seasons")
        for seasons_item_data in _seasons:
            seasons_item = GetV1StandingsSeasonResponse200SeasonsItem.from_dict(seasons_item_data)

            seasons.append(seasons_item)

        get_v1_standings_season_response_200 = cls(
            current_date=current_date,
            seasons=seasons,
        )

        get_v1_standings_season_response_200.additional_properties = d
        return get_v1_standings_season_response_200

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
