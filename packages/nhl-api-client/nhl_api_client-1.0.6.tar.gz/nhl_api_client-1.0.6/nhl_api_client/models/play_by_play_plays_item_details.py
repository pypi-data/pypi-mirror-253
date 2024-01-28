from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union


T = TypeVar("T", bound="PlayByPlayPlaysItemDetails")


@_attrs_define
class PlayByPlayPlaysItemDetails:
    """
    Attributes:
        event_owner_team_id (Union[Unset, None, int]):
        losing_player_id (Union[Unset, None, int]):
        winning_player_id (Union[Unset, None, int]):
        x_coord (Union[Unset, None, int]):
        y_coord (Union[Unset, None, int]):
        zone_code (Union[Unset, None, str]):
        reason (Union[Unset, None, str]):
        scoring_player_id (Union[Unset, None, int]):
        scoring_player_total (Union[Unset, None, int]):
        assist_1_player_id (Union[Unset, None, int]):
        assist_1_player_total (Union[Unset, None, int]):
        assist_2_player_id (Union[Unset, None, int]):
        assist_2_player_total (Union[Unset, None, int]):
        goalie_in_net_id (Union[Unset, None, int]):
        away_score (Union[Unset, None, int]):
        duration (Union[Unset, None, int]):
        committed_by_player_id (Union[Unset, None, int]):
        served_by_player_id (Union[Unset, None, int]):
        drawn_by_player_id (Union[Unset, None, int]):
        home_score (Union[Unset, None, int]):
        shot_type (Union[Unset, None, str]):
        desc_key (Union[Unset, None, str]):
        type_code (Union[Unset, None, str]):
    """

    event_owner_team_id: Union[Unset, None, int] = UNSET
    losing_player_id: Union[Unset, None, int] = UNSET
    winning_player_id: Union[Unset, None, int] = UNSET
    x_coord: Union[Unset, None, int] = UNSET
    y_coord: Union[Unset, None, int] = UNSET
    zone_code: Union[Unset, None, str] = UNSET
    reason: Union[Unset, None, str] = UNSET
    scoring_player_id: Union[Unset, None, int] = UNSET
    scoring_player_total: Union[Unset, None, int] = UNSET
    assist_1_player_id: Union[Unset, None, int] = UNSET
    assist_1_player_total: Union[Unset, None, int] = UNSET
    assist_2_player_id: Union[Unset, None, int] = UNSET
    assist_2_player_total: Union[Unset, None, int] = UNSET
    goalie_in_net_id: Union[Unset, None, int] = UNSET
    away_score: Union[Unset, None, int] = UNSET
    duration: Union[Unset, None, int] = UNSET
    committed_by_player_id: Union[Unset, None, int] = UNSET
    served_by_player_id: Union[Unset, None, int] = UNSET
    drawn_by_player_id: Union[Unset, None, int] = UNSET
    home_score: Union[Unset, None, int] = UNSET
    shot_type: Union[Unset, None, str] = UNSET
    desc_key: Union[Unset, None, str] = UNSET
    type_code: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_owner_team_id = self.event_owner_team_id
        losing_player_id = self.losing_player_id
        winning_player_id = self.winning_player_id
        x_coord = self.x_coord
        y_coord = self.y_coord
        zone_code = self.zone_code
        reason = self.reason
        scoring_player_id = self.scoring_player_id
        scoring_player_total = self.scoring_player_total
        assist_1_player_id = self.assist_1_player_id
        assist_1_player_total = self.assist_1_player_total
        assist_2_player_id = self.assist_2_player_id
        assist_2_player_total = self.assist_2_player_total
        goalie_in_net_id = self.goalie_in_net_id
        away_score = self.away_score
        duration = self.duration
        committed_by_player_id = self.committed_by_player_id
        served_by_player_id = self.served_by_player_id
        drawn_by_player_id = self.drawn_by_player_id
        home_score = self.home_score
        shot_type = self.shot_type
        desc_key = self.desc_key
        type_code = self.type_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_owner_team_id is not UNSET:
            field_dict["eventOwnerTeamId"] = event_owner_team_id
        if losing_player_id is not UNSET:
            field_dict["losingPlayerId"] = losing_player_id
        if winning_player_id is not UNSET:
            field_dict["winningPlayerId"] = winning_player_id
        if x_coord is not UNSET:
            field_dict["xCoord"] = x_coord
        if y_coord is not UNSET:
            field_dict["yCoord"] = y_coord
        if zone_code is not UNSET:
            field_dict["zoneCode"] = zone_code
        if reason is not UNSET:
            field_dict["reason"] = reason
        if scoring_player_id is not UNSET:
            field_dict["scoringPlayerId"] = scoring_player_id
        if scoring_player_total is not UNSET:
            field_dict["scoringPlayerTotal"] = scoring_player_total
        if assist_1_player_id is not UNSET:
            field_dict["assist1PlayerId"] = assist_1_player_id
        if assist_1_player_total is not UNSET:
            field_dict["assist1PlayerTotal"] = assist_1_player_total
        if assist_2_player_id is not UNSET:
            field_dict["assist2PlayerId"] = assist_2_player_id
        if assist_2_player_total is not UNSET:
            field_dict["assist2PlayerTotal"] = assist_2_player_total
        if goalie_in_net_id is not UNSET:
            field_dict["goalieInNetId"] = goalie_in_net_id
        if away_score is not UNSET:
            field_dict["awayScore"] = away_score
        if duration is not UNSET:
            field_dict["duration"] = duration
        if committed_by_player_id is not UNSET:
            field_dict["committedByPlayerId"] = committed_by_player_id
        if served_by_player_id is not UNSET:
            field_dict["servedByPlayerId"] = served_by_player_id
        if drawn_by_player_id is not UNSET:
            field_dict["drawnByPlayerId"] = drawn_by_player_id
        if home_score is not UNSET:
            field_dict["homeScore"] = home_score
        if shot_type is not UNSET:
            field_dict["shotType"] = shot_type
        if desc_key is not UNSET:
            field_dict["descKey"] = desc_key
        if type_code is not UNSET:
            field_dict["typeCode"] = type_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_owner_team_id = d.pop("eventOwnerTeamId", UNSET)

        losing_player_id = d.pop("losingPlayerId", UNSET)

        winning_player_id = d.pop("winningPlayerId", UNSET)

        x_coord = d.pop("xCoord", UNSET)

        y_coord = d.pop("yCoord", UNSET)

        zone_code = d.pop("zoneCode", UNSET)

        reason = d.pop("reason", UNSET)

        scoring_player_id = d.pop("scoringPlayerId", UNSET)

        scoring_player_total = d.pop("scoringPlayerTotal", UNSET)

        assist_1_player_id = d.pop("assist1PlayerId", UNSET)

        assist_1_player_total = d.pop("assist1PlayerTotal", UNSET)

        assist_2_player_id = d.pop("assist2PlayerId", UNSET)

        assist_2_player_total = d.pop("assist2PlayerTotal", UNSET)

        goalie_in_net_id = d.pop("goalieInNetId", UNSET)

        away_score = d.pop("awayScore", UNSET)

        duration = d.pop("duration", UNSET)

        committed_by_player_id = d.pop("committedByPlayerId", UNSET)

        served_by_player_id = d.pop("servedByPlayerId", UNSET)

        drawn_by_player_id = d.pop("drawnByPlayerId", UNSET)

        home_score = d.pop("homeScore", UNSET)

        shot_type = d.pop("shotType", UNSET)

        desc_key = d.pop("descKey", UNSET)

        type_code = d.pop("typeCode", UNSET)

        play_by_play_plays_item_details = cls(
            event_owner_team_id=event_owner_team_id,
            losing_player_id=losing_player_id,
            winning_player_id=winning_player_id,
            x_coord=x_coord,
            y_coord=y_coord,
            zone_code=zone_code,
            reason=reason,
            scoring_player_id=scoring_player_id,
            scoring_player_total=scoring_player_total,
            assist_1_player_id=assist_1_player_id,
            assist_1_player_total=assist_1_player_total,
            assist_2_player_id=assist_2_player_id,
            assist_2_player_total=assist_2_player_total,
            goalie_in_net_id=goalie_in_net_id,
            away_score=away_score,
            duration=duration,
            committed_by_player_id=committed_by_player_id,
            served_by_player_id=served_by_player_id,
            drawn_by_player_id=drawn_by_player_id,
            home_score=home_score,
            shot_type=shot_type,
            desc_key=desc_key,
            type_code=type_code,
        )

        play_by_play_plays_item_details.additional_properties = d
        return play_by_play_plays_item_details

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
