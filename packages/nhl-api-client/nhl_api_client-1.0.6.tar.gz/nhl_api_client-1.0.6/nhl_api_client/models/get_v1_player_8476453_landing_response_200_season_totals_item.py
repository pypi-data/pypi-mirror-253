from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import Dict

if TYPE_CHECKING:
    from ..models.language_string import LanguageString


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200SeasonTotalsItem")


@_attrs_define
class GetV1Player8476453LandingResponse200SeasonTotalsItem:
    """
    Attributes:
        season (int):
        game_type_id (int):
        league_abbrev (str):
        team_name (LanguageString):
        sequence (int):
        games_played (int):
        goals (int):
        assists (int):
        points (int):
        pim (int):
        plus_minus (Union[Unset, int]):
        power_play_goals (Union[Unset, int]):
        game_winning_goals (Union[Unset, int]):
        shorthanded_goals (Union[Unset, int]):
        shots (Union[Unset, int]):
        shooting_pctg (Union[Unset, float]):
        power_play_points (Union[Unset, int]):
        shorthanded_points (Union[Unset, int]):
        ot_goals (Union[Unset, int]):
        faceoff_winning_pctg (Union[Unset, float]):
        avg_toi (Union[Unset, str]):
    """

    season: int
    game_type_id: int
    league_abbrev: str
    team_name: "LanguageString"
    sequence: int
    games_played: int
    goals: int
    assists: int
    points: int
    pim: int
    plus_minus: Union[Unset, int] = UNSET
    power_play_goals: Union[Unset, int] = UNSET
    game_winning_goals: Union[Unset, int] = UNSET
    shorthanded_goals: Union[Unset, int] = UNSET
    shots: Union[Unset, int] = UNSET
    shooting_pctg: Union[Unset, float] = UNSET
    power_play_points: Union[Unset, int] = UNSET
    shorthanded_points: Union[Unset, int] = UNSET
    ot_goals: Union[Unset, int] = UNSET
    faceoff_winning_pctg: Union[Unset, float] = UNSET
    avg_toi: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season = self.season
        game_type_id = self.game_type_id
        league_abbrev = self.league_abbrev
        team_name = self.team_name.to_dict()

        sequence = self.sequence
        games_played = self.games_played
        goals = self.goals
        assists = self.assists
        points = self.points
        pim = self.pim
        plus_minus = self.plus_minus
        power_play_goals = self.power_play_goals
        game_winning_goals = self.game_winning_goals
        shorthanded_goals = self.shorthanded_goals
        shots = self.shots
        shooting_pctg = self.shooting_pctg
        power_play_points = self.power_play_points
        shorthanded_points = self.shorthanded_points
        ot_goals = self.ot_goals
        faceoff_winning_pctg = self.faceoff_winning_pctg
        avg_toi = self.avg_toi

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "season": season,
                "gameTypeId": game_type_id,
                "leagueAbbrev": league_abbrev,
                "teamName": team_name,
                "sequence": sequence,
                "gamesPlayed": games_played,
                "goals": goals,
                "assists": assists,
                "points": points,
                "pim": pim,
            }
        )
        if plus_minus is not UNSET:
            field_dict["plusMinus"] = plus_minus
        if power_play_goals is not UNSET:
            field_dict["powerPlayGoals"] = power_play_goals
        if game_winning_goals is not UNSET:
            field_dict["gameWinningGoals"] = game_winning_goals
        if shorthanded_goals is not UNSET:
            field_dict["shorthandedGoals"] = shorthanded_goals
        if shots is not UNSET:
            field_dict["shots"] = shots
        if shooting_pctg is not UNSET:
            field_dict["shootingPctg"] = shooting_pctg
        if power_play_points is not UNSET:
            field_dict["powerPlayPoints"] = power_play_points
        if shorthanded_points is not UNSET:
            field_dict["shorthandedPoints"] = shorthanded_points
        if ot_goals is not UNSET:
            field_dict["otGoals"] = ot_goals
        if faceoff_winning_pctg is not UNSET:
            field_dict["faceoffWinningPctg"] = faceoff_winning_pctg
        if avg_toi is not UNSET:
            field_dict["avgToi"] = avg_toi

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        season = d.pop("season")

        game_type_id = d.pop("gameTypeId")

        league_abbrev = d.pop("leagueAbbrev")

        team_name = LanguageString.from_dict(d.pop("teamName"))

        sequence = d.pop("sequence")

        games_played = d.pop("gamesPlayed")

        goals = d.pop("goals")

        assists = d.pop("assists")

        points = d.pop("points")

        pim = d.pop("pim")

        plus_minus = d.pop("plusMinus", UNSET)

        power_play_goals = d.pop("powerPlayGoals", UNSET)

        game_winning_goals = d.pop("gameWinningGoals", UNSET)

        shorthanded_goals = d.pop("shorthandedGoals", UNSET)

        shots = d.pop("shots", UNSET)

        shooting_pctg = d.pop("shootingPctg", UNSET)

        power_play_points = d.pop("powerPlayPoints", UNSET)

        shorthanded_points = d.pop("shorthandedPoints", UNSET)

        ot_goals = d.pop("otGoals", UNSET)

        faceoff_winning_pctg = d.pop("faceoffWinningPctg", UNSET)

        avg_toi = d.pop("avgToi", UNSET)

        get_v1_player_8476453_landing_response_200_season_totals_item = cls(
            season=season,
            game_type_id=game_type_id,
            league_abbrev=league_abbrev,
            team_name=team_name,
            sequence=sequence,
            games_played=games_played,
            goals=goals,
            assists=assists,
            points=points,
            pim=pim,
            plus_minus=plus_minus,
            power_play_goals=power_play_goals,
            game_winning_goals=game_winning_goals,
            shorthanded_goals=shorthanded_goals,
            shots=shots,
            shooting_pctg=shooting_pctg,
            power_play_points=power_play_points,
            shorthanded_points=shorthanded_points,
            ot_goals=ot_goals,
            faceoff_winning_pctg=faceoff_winning_pctg,
            avg_toi=avg_toi,
        )

        get_v1_player_8476453_landing_response_200_season_totals_item.additional_properties = d
        return get_v1_player_8476453_landing_response_200_season_totals_item

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
