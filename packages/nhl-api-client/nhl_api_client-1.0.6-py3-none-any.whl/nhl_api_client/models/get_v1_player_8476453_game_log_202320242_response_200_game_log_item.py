from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from dateutil.parser import isoparse
from typing import Dict
import datetime

if TYPE_CHECKING:
    from ..models.language_string import LanguageString


T = TypeVar("T", bound="GetV1Player8476453GameLog202320242Response200GameLogItem")


@_attrs_define
class GetV1Player8476453GameLog202320242Response200GameLogItem:
    """
    Attributes:
        game_id (int):
        team_abbrev (str):
        home_road_flag (str):
        game_date (datetime.date):
        goals (int):
        assists (int):
        common_name (LanguageString):
        opponent_common_name (LanguageString):
        points (int):
        plus_minus (int):
        power_play_goals (int):
        power_play_points (int):
        game_winning_goals (int):
        ot_goals (int):
        shots (int):
        shifts (int):
        shorthanded_goals (int):
        shorthanded_points (int):
        opponent_abbrev (str):
        pim (int):
        toi (str):
    """

    game_id: int
    team_abbrev: str
    home_road_flag: str
    game_date: datetime.date
    goals: int
    assists: int
    common_name: "LanguageString"
    opponent_common_name: "LanguageString"
    points: int
    plus_minus: int
    power_play_goals: int
    power_play_points: int
    game_winning_goals: int
    ot_goals: int
    shots: int
    shifts: int
    shorthanded_goals: int
    shorthanded_points: int
    opponent_abbrev: str
    pim: int
    toi: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        game_id = self.game_id
        team_abbrev = self.team_abbrev
        home_road_flag = self.home_road_flag
        game_date = self.game_date.isoformat()
        goals = self.goals
        assists = self.assists
        common_name = self.common_name.to_dict()

        opponent_common_name = self.opponent_common_name.to_dict()

        points = self.points
        plus_minus = self.plus_minus
        power_play_goals = self.power_play_goals
        power_play_points = self.power_play_points
        game_winning_goals = self.game_winning_goals
        ot_goals = self.ot_goals
        shots = self.shots
        shifts = self.shifts
        shorthanded_goals = self.shorthanded_goals
        shorthanded_points = self.shorthanded_points
        opponent_abbrev = self.opponent_abbrev
        pim = self.pim
        toi = self.toi

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gameId": game_id,
                "teamAbbrev": team_abbrev,
                "homeRoadFlag": home_road_flag,
                "gameDate": game_date,
                "goals": goals,
                "assists": assists,
                "commonName": common_name,
                "opponentCommonName": opponent_common_name,
                "points": points,
                "plusMinus": plus_minus,
                "powerPlayGoals": power_play_goals,
                "powerPlayPoints": power_play_points,
                "gameWinningGoals": game_winning_goals,
                "otGoals": ot_goals,
                "shots": shots,
                "shifts": shifts,
                "shorthandedGoals": shorthanded_goals,
                "shorthandedPoints": shorthanded_points,
                "opponentAbbrev": opponent_abbrev,
                "pim": pim,
                "toi": toi,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        game_id = d.pop("gameId")

        team_abbrev = d.pop("teamAbbrev")

        home_road_flag = d.pop("homeRoadFlag")

        game_date = isoparse(d.pop("gameDate")).date()

        goals = d.pop("goals")

        assists = d.pop("assists")

        common_name = LanguageString.from_dict(d.pop("commonName"))

        opponent_common_name = LanguageString.from_dict(d.pop("opponentCommonName"))

        points = d.pop("points")

        plus_minus = d.pop("plusMinus")

        power_play_goals = d.pop("powerPlayGoals")

        power_play_points = d.pop("powerPlayPoints")

        game_winning_goals = d.pop("gameWinningGoals")

        ot_goals = d.pop("otGoals")

        shots = d.pop("shots")

        shifts = d.pop("shifts")

        shorthanded_goals = d.pop("shorthandedGoals")

        shorthanded_points = d.pop("shorthandedPoints")

        opponent_abbrev = d.pop("opponentAbbrev")

        pim = d.pop("pim")

        toi = d.pop("toi")

        get_v1_player_8476453_game_log_202320242_response_200_game_log_item = cls(
            game_id=game_id,
            team_abbrev=team_abbrev,
            home_road_flag=home_road_flag,
            game_date=game_date,
            goals=goals,
            assists=assists,
            common_name=common_name,
            opponent_common_name=opponent_common_name,
            points=points,
            plus_minus=plus_minus,
            power_play_goals=power_play_goals,
            power_play_points=power_play_points,
            game_winning_goals=game_winning_goals,
            ot_goals=ot_goals,
            shots=shots,
            shifts=shifts,
            shorthanded_goals=shorthanded_goals,
            shorthanded_points=shorthanded_points,
            opponent_abbrev=opponent_abbrev,
            pim=pim,
            toi=toi,
        )

        get_v1_player_8476453_game_log_202320242_response_200_game_log_item.additional_properties = d
        return get_v1_player_8476453_game_log_202320242_response_200_game_log_item

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
