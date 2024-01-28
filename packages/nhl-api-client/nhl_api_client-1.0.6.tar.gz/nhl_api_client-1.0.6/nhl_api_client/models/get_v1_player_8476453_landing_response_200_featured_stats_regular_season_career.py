from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonCareer")


@_attrs_define
class GetV1Player8476453LandingResponse200FeaturedStatsRegularSeasonCareer:
    """
    Attributes:
        games_played (int):
        goals (int):
        assists (int):
        points (int):
        plus_minus (int):
        pim (int):
        game_winning_goals (int):
        ot_goals (int):
        shots (int):
        shooting_pctg (float):
        shorhanded_points (int):
        power_play_goals (int):
        power_play_points (int):
        shorthanded_goals (int):
    """

    games_played: int
    goals: int
    assists: int
    points: int
    plus_minus: int
    pim: int
    game_winning_goals: int
    ot_goals: int
    shots: int
    shooting_pctg: float
    shorhanded_points: int
    power_play_goals: int
    power_play_points: int
    shorthanded_goals: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        games_played = self.games_played
        goals = self.goals
        assists = self.assists
        points = self.points
        plus_minus = self.plus_minus
        pim = self.pim
        game_winning_goals = self.game_winning_goals
        ot_goals = self.ot_goals
        shots = self.shots
        shooting_pctg = self.shooting_pctg
        shorhanded_points = self.shorhanded_points
        power_play_goals = self.power_play_goals
        power_play_points = self.power_play_points
        shorthanded_goals = self.shorthanded_goals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gamesPlayed": games_played,
                "goals": goals,
                "assists": assists,
                "points": points,
                "plusMinus": plus_minus,
                "pim": pim,
                "gameWinningGoals": game_winning_goals,
                "otGoals": ot_goals,
                "shots": shots,
                "shootingPctg": shooting_pctg,
                "shorhandedPoints": shorhanded_points,
                "powerPlayGoals": power_play_goals,
                "powerPlayPoints": power_play_points,
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

        points = d.pop("points")

        plus_minus = d.pop("plusMinus")

        pim = d.pop("pim")

        game_winning_goals = d.pop("gameWinningGoals")

        ot_goals = d.pop("otGoals")

        shots = d.pop("shots")

        shooting_pctg = d.pop("shootingPctg")

        shorhanded_points = d.pop("shorhandedPoints")

        power_play_goals = d.pop("powerPlayGoals")

        power_play_points = d.pop("powerPlayPoints")

        shorthanded_goals = d.pop("shorthandedGoals")

        get_v1_player_8476453_landing_response_200_featured_stats_regular_season_career = cls(
            games_played=games_played,
            goals=goals,
            assists=assists,
            points=points,
            plus_minus=plus_minus,
            pim=pim,
            game_winning_goals=game_winning_goals,
            ot_goals=ot_goals,
            shots=shots,
            shooting_pctg=shooting_pctg,
            shorhanded_points=shorhanded_points,
            power_play_goals=power_play_goals,
            power_play_points=power_play_points,
            shorthanded_goals=shorthanded_goals,
        )

        get_v1_player_8476453_landing_response_200_featured_stats_regular_season_career.additional_properties = d
        return get_v1_player_8476453_landing_response_200_featured_stats_regular_season_career

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
