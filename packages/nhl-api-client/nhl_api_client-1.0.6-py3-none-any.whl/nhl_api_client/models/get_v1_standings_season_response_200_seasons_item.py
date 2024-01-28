from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="GetV1StandingsSeasonResponse200SeasonsItem")


@_attrs_define
class GetV1StandingsSeasonResponse200SeasonsItem:
    """
    Attributes:
        id (int):
        conferences_in_use (bool):
        divisions_in_use (bool):
        point_for_o_tloss_in_use (bool):
        regulation_wins_in_use (bool):
        row_in_use (bool):
        standings_end (str):
        standings_start (str):
        ties_in_use (bool):
        wildcard_in_use (bool):
    """

    id: int
    conferences_in_use: bool
    divisions_in_use: bool
    point_for_o_tloss_in_use: bool
    regulation_wins_in_use: bool
    row_in_use: bool
    standings_end: str
    standings_start: str
    ties_in_use: bool
    wildcard_in_use: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        conferences_in_use = self.conferences_in_use
        divisions_in_use = self.divisions_in_use
        point_for_o_tloss_in_use = self.point_for_o_tloss_in_use
        regulation_wins_in_use = self.regulation_wins_in_use
        row_in_use = self.row_in_use
        standings_end = self.standings_end
        standings_start = self.standings_start
        ties_in_use = self.ties_in_use
        wildcard_in_use = self.wildcard_in_use

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "conferencesInUse": conferences_in_use,
                "divisionsInUse": divisions_in_use,
                "pointForOTlossInUse": point_for_o_tloss_in_use,
                "regulationWinsInUse": regulation_wins_in_use,
                "rowInUse": row_in_use,
                "standingsEnd": standings_end,
                "standingsStart": standings_start,
                "tiesInUse": ties_in_use,
                "wildcardInUse": wildcard_in_use,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        conferences_in_use = d.pop("conferencesInUse")

        divisions_in_use = d.pop("divisionsInUse")

        point_for_o_tloss_in_use = d.pop("pointForOTlossInUse")

        regulation_wins_in_use = d.pop("regulationWinsInUse")

        row_in_use = d.pop("rowInUse")

        standings_end = d.pop("standingsEnd")

        standings_start = d.pop("standingsStart")

        ties_in_use = d.pop("tiesInUse")

        wildcard_in_use = d.pop("wildcardInUse")

        get_v1_standings_season_response_200_seasons_item = cls(
            id=id,
            conferences_in_use=conferences_in_use,
            divisions_in_use=divisions_in_use,
            point_for_o_tloss_in_use=point_for_o_tloss_in_use,
            regulation_wins_in_use=regulation_wins_in_use,
            row_in_use=row_in_use,
            standings_end=standings_end,
            standings_start=standings_start,
            ties_in_use=ties_in_use,
            wildcard_in_use=wildcard_in_use,
        )

        get_v1_standings_season_response_200_seasons_item.additional_properties = d
        return get_v1_standings_season_response_200_seasons_item

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
