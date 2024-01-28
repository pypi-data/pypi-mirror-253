from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from dateutil.parser import isoparse
import datetime


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200Last5GamesItem")


@_attrs_define
class GetV1Player8476453LandingResponse200Last5GamesItem:
    """
    Attributes:
        game_id (int):
        game_type_id (int):
        team_abbrev (str):
        home_road_flag (str):
        game_date (datetime.date):
        goals (int):
        assists (int):
        points (int):
        plus_minus (int):
        power_play_goals (int):
        shots (int):
        shifts (int):
        shorthanded_goals (int):
        pim (int):
        opponent_abbrev (str):
        toi (str):
    """

    game_id: int
    game_type_id: int
    team_abbrev: str
    home_road_flag: str
    game_date: datetime.date
    goals: int
    assists: int
    points: int
    plus_minus: int
    power_play_goals: int
    shots: int
    shifts: int
    shorthanded_goals: int
    pim: int
    opponent_abbrev: str
    toi: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        game_id = self.game_id
        game_type_id = self.game_type_id
        team_abbrev = self.team_abbrev
        home_road_flag = self.home_road_flag
        game_date = self.game_date.isoformat()
        goals = self.goals
        assists = self.assists
        points = self.points
        plus_minus = self.plus_minus
        power_play_goals = self.power_play_goals
        shots = self.shots
        shifts = self.shifts
        shorthanded_goals = self.shorthanded_goals
        pim = self.pim
        opponent_abbrev = self.opponent_abbrev
        toi = self.toi

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gameId": game_id,
                "gameTypeId": game_type_id,
                "teamAbbrev": team_abbrev,
                "homeRoadFlag": home_road_flag,
                "gameDate": game_date,
                "goals": goals,
                "assists": assists,
                "points": points,
                "plusMinus": plus_minus,
                "powerPlayGoals": power_play_goals,
                "shots": shots,
                "shifts": shifts,
                "shorthandedGoals": shorthanded_goals,
                "pim": pim,
                "opponentAbbrev": opponent_abbrev,
                "toi": toi,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        game_id = d.pop("gameId")

        game_type_id = d.pop("gameTypeId")

        team_abbrev = d.pop("teamAbbrev")

        home_road_flag = d.pop("homeRoadFlag")

        game_date = isoparse(d.pop("gameDate")).date()

        goals = d.pop("goals")

        assists = d.pop("assists")

        points = d.pop("points")

        plus_minus = d.pop("plusMinus")

        power_play_goals = d.pop("powerPlayGoals")

        shots = d.pop("shots")

        shifts = d.pop("shifts")

        shorthanded_goals = d.pop("shorthandedGoals")

        pim = d.pop("pim")

        opponent_abbrev = d.pop("opponentAbbrev")

        toi = d.pop("toi")

        get_v1_player_8476453_landing_response_200_last_5_games_item = cls(
            game_id=game_id,
            game_type_id=game_type_id,
            team_abbrev=team_abbrev,
            home_road_flag=home_road_flag,
            game_date=game_date,
            goals=goals,
            assists=assists,
            points=points,
            plus_minus=plus_minus,
            power_play_goals=power_play_goals,
            shots=shots,
            shifts=shifts,
            shorthanded_goals=shorthanded_goals,
            pim=pim,
            opponent_abbrev=opponent_abbrev,
            toi=toi,
        )

        get_v1_player_8476453_landing_response_200_last_5_games_item.additional_properties = d
        return get_v1_player_8476453_landing_response_200_last_5_games_item

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
