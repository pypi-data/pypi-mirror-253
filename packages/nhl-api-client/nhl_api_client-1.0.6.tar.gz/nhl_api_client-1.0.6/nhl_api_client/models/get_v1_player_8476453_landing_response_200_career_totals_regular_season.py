from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200CareerTotalsRegularSeason")


@_attrs_define
class GetV1Player8476453LandingResponse200CareerTotalsRegularSeason:
    """
    Attributes:
        games_played (int):
        goals (int):
        assists (int):
        pim (int):
        points (int):
        plus_minus (int):
        power_play_goals (int):
        power_play_points (int):
        shorthanded_points (int):
        game_winning_goals (int):
        ot_goals (int):
        shots (int):
        shooting_pctg (float):
        faceoff_winning_pctg (float):
        avg_toi (str):
        shorthanded_goals (int):
    """

    games_played: int
    goals: int
    assists: int
    pim: int
    points: int
    plus_minus: int
    power_play_goals: int
    power_play_points: int
    shorthanded_points: int
    game_winning_goals: int
    ot_goals: int
    shots: int
    shooting_pctg: float
    faceoff_winning_pctg: float
    avg_toi: str
    shorthanded_goals: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        games_played = self.games_played
        goals = self.goals
        assists = self.assists
        pim = self.pim
        points = self.points
        plus_minus = self.plus_minus
        power_play_goals = self.power_play_goals
        power_play_points = self.power_play_points
        shorthanded_points = self.shorthanded_points
        game_winning_goals = self.game_winning_goals
        ot_goals = self.ot_goals
        shots = self.shots
        shooting_pctg = self.shooting_pctg
        faceoff_winning_pctg = self.faceoff_winning_pctg
        avg_toi = self.avg_toi
        shorthanded_goals = self.shorthanded_goals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gamesPlayed": games_played,
                "goals": goals,
                "assists": assists,
                "pim": pim,
                "points": points,
                "plusMinus": plus_minus,
                "powerPlayGoals": power_play_goals,
                "powerPlayPoints": power_play_points,
                "shorthandedPoints": shorthanded_points,
                "gameWinningGoals": game_winning_goals,
                "otGoals": ot_goals,
                "shots": shots,
                "shootingPctg": shooting_pctg,
                "faceoffWinningPctg": faceoff_winning_pctg,
                "avgToi": avg_toi,
                "shorthandedGoals": shorthanded_goals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        games_played = d.pop("gamesPlayed")

        goals = d.pop("goals")

        assists = d.pop("assists")

        pim = d.pop("pim")

        points = d.pop("points")

        plus_minus = d.pop("plusMinus")

        power_play_goals = d.pop("powerPlayGoals")

        power_play_points = d.pop("powerPlayPoints")

        shorthanded_points = d.pop("shorthandedPoints")

        game_winning_goals = d.pop("gameWinningGoals")

        ot_goals = d.pop("otGoals")

        shots = d.pop("shots")

        shooting_pctg = d.pop("shootingPctg")

        faceoff_winning_pctg = d.pop("faceoffWinningPctg")

        avg_toi = d.pop("avgToi")

        shorthanded_goals = d.pop("shorthandedGoals")

        get_v1_player_8476453_landing_response_200_career_totals_regular_season = cls(
            games_played=games_played,
            goals=goals,
            assists=assists,
            pim=pim,
            points=points,
            plus_minus=plus_minus,
            power_play_goals=power_play_goals,
            power_play_points=power_play_points,
            shorthanded_points=shorthanded_points,
            game_winning_goals=game_winning_goals,
            ot_goals=ot_goals,
            shots=shots,
            shooting_pctg=shooting_pctg,
            faceoff_winning_pctg=faceoff_winning_pctg,
            avg_toi=avg_toi,
            shorthanded_goals=shorthanded_goals,
        )

        get_v1_player_8476453_landing_response_200_career_totals_regular_season.additional_properties = d
        return get_v1_player_8476453_landing_response_200_career_totals_regular_season

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
