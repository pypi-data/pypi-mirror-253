from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200DraftDetails")


@_attrs_define
class GetV1Player8476453LandingResponse200DraftDetails:
    """
    Attributes:
        year (int):
        team_abbrev (str):
        round_ (int):
        pick_in_round (int):
        overall_pick (int):
    """

    year: int
    team_abbrev: str
    round_: int
    pick_in_round: int
    overall_pick: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year
        team_abbrev = self.team_abbrev
        round_ = self.round_
        pick_in_round = self.pick_in_round
        overall_pick = self.overall_pick

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "teamAbbrev": team_abbrev,
                "round": round_,
                "pickInRound": pick_in_round,
                "overallPick": overall_pick,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year")

        team_abbrev = d.pop("teamAbbrev")

        round_ = d.pop("round")

        pick_in_round = d.pop("pickInRound")

        overall_pick = d.pop("overallPick")

        get_v1_player_8476453_landing_response_200_draft_details = cls(
            year=year,
            team_abbrev=team_abbrev,
            round_=round_,
            pick_in_round=pick_in_round,
            overall_pick=overall_pick,
        )

        get_v1_player_8476453_landing_response_200_draft_details.additional_properties = d
        return get_v1_player_8476453_landing_response_200_draft_details

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
