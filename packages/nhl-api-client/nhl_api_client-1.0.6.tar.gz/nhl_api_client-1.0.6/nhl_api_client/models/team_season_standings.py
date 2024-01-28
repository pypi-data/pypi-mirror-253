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


T = TypeVar("T", bound="TeamSeasonStandings")


@_attrs_define
class TeamSeasonStandings:
    """
    Attributes:
        conference_abbrev (Union[Unset, str]):
        conference_home_sequence (Union[Unset, int]):
        conference_l10_sequence (Union[Unset, int]):
        conference_name (Union[Unset, str]):
        conference_road_sequence (Union[Unset, int]):
        conference_sequence (Union[Unset, int]):
        date (Union[Unset, str]):
        division_abbrev (Union[Unset, str]):
        division_home_sequence (Union[Unset, int]):
        division_l10_sequence (Union[Unset, int]):
        division_name (Union[Unset, str]):
        division_road_sequence (Union[Unset, int]):
        division_sequence (Union[Unset, int]):
        game_type_id (Union[Unset, int]):
        games_played (Union[Unset, int]):
        goal_differential (Union[Unset, int]):
        goal_differential_pctg (Union[Unset, float]):
        goal_against (Union[Unset, int]):
        goal_for (Union[Unset, int]):
        goals_for_pctg (Union[Unset, float]):
        home_games_played (Union[Unset, int]):
        home_goal_differential (Union[Unset, int]):
        home_goals_against (Union[Unset, int]):
        home_goals_for (Union[Unset, int]):
        home_losses (Union[Unset, int]):
        home_ot_losses (Union[Unset, int]):
        home_points (Union[Unset, int]):
        home_regulation_plus_ot_wins (Union[Unset, int]):
        home_regulation_wins (Union[Unset, int]):
        home_ties (Union[Unset, int]):
        home_wins (Union[Unset, int]):
        l_10_games_played (Union[Unset, int]):
        l_10_goal_differential (Union[Unset, int]):
        l_10_goals_against (Union[Unset, int]):
        l_10_goals_for (Union[Unset, int]):
        l_10_losses (Union[Unset, int]):
        l_10_ot_losses (Union[Unset, int]):
        l_10_points (Union[Unset, int]):
        l_10_regulation_plus_ot_wins (Union[Unset, int]):
        l_10_regulation_wins (Union[Unset, int]):
        l_10_ties (Union[Unset, int]):
        l_10_wins (Union[Unset, int]):
        league_home_sequence (Union[Unset, int]):
        league_l10_sequence (Union[Unset, int]):
        league_road_sequence (Union[Unset, int]):
        league_sequence (Union[Unset, int]):
        losses (Union[Unset, int]):
        ot_losses (Union[Unset, int]):
        place_name (Union[Unset, LanguageString]):
        point_pctg (Union[Unset, float]):
        points (Union[Unset, int]):
        regulation_plus_ot_win_pctg (Union[Unset, float]):
        regulation_plus_ot_wins (Union[Unset, int]):
        regulation_win_pctg (Union[Unset, float]):
        regulation_wins (Union[Unset, int]):
        road_games_played (Union[Unset, int]):
        road_goal_differential (Union[Unset, int]):
        road_goals_against (Union[Unset, int]):
        road_goals_for (Union[Unset, int]):
        road_losses (Union[Unset, int]):
        road_ot_losses (Union[Unset, int]):
        road_points (Union[Unset, int]):
        road_regulation_plus_ot_wins (Union[Unset, int]):
        road_regulation_wins (Union[Unset, int]):
        road_ties (Union[Unset, int]):
        road_wins (Union[Unset, int]):
        season_id (Union[Unset, int]):
        shootout_losses (Union[Unset, int]):
        shootout_wins (Union[Unset, int]):
        streak_code (Union[Unset, str]):
        streak_count (Union[Unset, int]):
        team_name (Union[Unset, LanguageString]):
        team_abbrev (Union[Unset, LanguageString]):
        team_logo (Union[Unset, str]):
        ties (Union[Unset, int]):
        waivers_sequence (Union[Unset, int]):
        wildcard_sequence (Union[Unset, int]):
        win_pctg (Union[Unset, float]):
        wins (Union[Unset, int]):
    """

    conference_abbrev: Union[Unset, str] = UNSET
    conference_home_sequence: Union[Unset, int] = UNSET
    conference_l10_sequence: Union[Unset, int] = UNSET
    conference_name: Union[Unset, str] = UNSET
    conference_road_sequence: Union[Unset, int] = UNSET
    conference_sequence: Union[Unset, int] = UNSET
    date: Union[Unset, str] = UNSET
    division_abbrev: Union[Unset, str] = UNSET
    division_home_sequence: Union[Unset, int] = UNSET
    division_l10_sequence: Union[Unset, int] = UNSET
    division_name: Union[Unset, str] = UNSET
    division_road_sequence: Union[Unset, int] = UNSET
    division_sequence: Union[Unset, int] = UNSET
    game_type_id: Union[Unset, int] = UNSET
    games_played: Union[Unset, int] = UNSET
    goal_differential: Union[Unset, int] = UNSET
    goal_differential_pctg: Union[Unset, float] = UNSET
    goal_against: Union[Unset, int] = UNSET
    goal_for: Union[Unset, int] = UNSET
    goals_for_pctg: Union[Unset, float] = UNSET
    home_games_played: Union[Unset, int] = UNSET
    home_goal_differential: Union[Unset, int] = UNSET
    home_goals_against: Union[Unset, int] = UNSET
    home_goals_for: Union[Unset, int] = UNSET
    home_losses: Union[Unset, int] = UNSET
    home_ot_losses: Union[Unset, int] = UNSET
    home_points: Union[Unset, int] = UNSET
    home_regulation_plus_ot_wins: Union[Unset, int] = UNSET
    home_regulation_wins: Union[Unset, int] = UNSET
    home_ties: Union[Unset, int] = UNSET
    home_wins: Union[Unset, int] = UNSET
    l_10_games_played: Union[Unset, int] = UNSET
    l_10_goal_differential: Union[Unset, int] = UNSET
    l_10_goals_against: Union[Unset, int] = UNSET
    l_10_goals_for: Union[Unset, int] = UNSET
    l_10_losses: Union[Unset, int] = UNSET
    l_10_ot_losses: Union[Unset, int] = UNSET
    l_10_points: Union[Unset, int] = UNSET
    l_10_regulation_plus_ot_wins: Union[Unset, int] = UNSET
    l_10_regulation_wins: Union[Unset, int] = UNSET
    l_10_ties: Union[Unset, int] = UNSET
    l_10_wins: Union[Unset, int] = UNSET
    league_home_sequence: Union[Unset, int] = UNSET
    league_l10_sequence: Union[Unset, int] = UNSET
    league_road_sequence: Union[Unset, int] = UNSET
    league_sequence: Union[Unset, int] = UNSET
    losses: Union[Unset, int] = UNSET
    ot_losses: Union[Unset, int] = UNSET
    place_name: Union[Unset, "LanguageString"] = UNSET
    point_pctg: Union[Unset, float] = UNSET
    points: Union[Unset, int] = UNSET
    regulation_plus_ot_win_pctg: Union[Unset, float] = UNSET
    regulation_plus_ot_wins: Union[Unset, int] = UNSET
    regulation_win_pctg: Union[Unset, float] = UNSET
    regulation_wins: Union[Unset, int] = UNSET
    road_games_played: Union[Unset, int] = UNSET
    road_goal_differential: Union[Unset, int] = UNSET
    road_goals_against: Union[Unset, int] = UNSET
    road_goals_for: Union[Unset, int] = UNSET
    road_losses: Union[Unset, int] = UNSET
    road_ot_losses: Union[Unset, int] = UNSET
    road_points: Union[Unset, int] = UNSET
    road_regulation_plus_ot_wins: Union[Unset, int] = UNSET
    road_regulation_wins: Union[Unset, int] = UNSET
    road_ties: Union[Unset, int] = UNSET
    road_wins: Union[Unset, int] = UNSET
    season_id: Union[Unset, int] = UNSET
    shootout_losses: Union[Unset, int] = UNSET
    shootout_wins: Union[Unset, int] = UNSET
    streak_code: Union[Unset, str] = UNSET
    streak_count: Union[Unset, int] = UNSET
    team_name: Union[Unset, "LanguageString"] = UNSET
    team_abbrev: Union[Unset, "LanguageString"] = UNSET
    team_logo: Union[Unset, str] = UNSET
    ties: Union[Unset, int] = UNSET
    waivers_sequence: Union[Unset, int] = UNSET
    wildcard_sequence: Union[Unset, int] = UNSET
    win_pctg: Union[Unset, float] = UNSET
    wins: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conference_abbrev = self.conference_abbrev
        conference_home_sequence = self.conference_home_sequence
        conference_l10_sequence = self.conference_l10_sequence
        conference_name = self.conference_name
        conference_road_sequence = self.conference_road_sequence
        conference_sequence = self.conference_sequence
        date = self.date
        division_abbrev = self.division_abbrev
        division_home_sequence = self.division_home_sequence
        division_l10_sequence = self.division_l10_sequence
        division_name = self.division_name
        division_road_sequence = self.division_road_sequence
        division_sequence = self.division_sequence
        game_type_id = self.game_type_id
        games_played = self.games_played
        goal_differential = self.goal_differential
        goal_differential_pctg = self.goal_differential_pctg
        goal_against = self.goal_against
        goal_for = self.goal_for
        goals_for_pctg = self.goals_for_pctg
        home_games_played = self.home_games_played
        home_goal_differential = self.home_goal_differential
        home_goals_against = self.home_goals_against
        home_goals_for = self.home_goals_for
        home_losses = self.home_losses
        home_ot_losses = self.home_ot_losses
        home_points = self.home_points
        home_regulation_plus_ot_wins = self.home_regulation_plus_ot_wins
        home_regulation_wins = self.home_regulation_wins
        home_ties = self.home_ties
        home_wins = self.home_wins
        l_10_games_played = self.l_10_games_played
        l_10_goal_differential = self.l_10_goal_differential
        l_10_goals_against = self.l_10_goals_against
        l_10_goals_for = self.l_10_goals_for
        l_10_losses = self.l_10_losses
        l_10_ot_losses = self.l_10_ot_losses
        l_10_points = self.l_10_points
        l_10_regulation_plus_ot_wins = self.l_10_regulation_plus_ot_wins
        l_10_regulation_wins = self.l_10_regulation_wins
        l_10_ties = self.l_10_ties
        l_10_wins = self.l_10_wins
        league_home_sequence = self.league_home_sequence
        league_l10_sequence = self.league_l10_sequence
        league_road_sequence = self.league_road_sequence
        league_sequence = self.league_sequence
        losses = self.losses
        ot_losses = self.ot_losses
        place_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.place_name, Unset):
            place_name = self.place_name.to_dict()

        point_pctg = self.point_pctg
        points = self.points
        regulation_plus_ot_win_pctg = self.regulation_plus_ot_win_pctg
        regulation_plus_ot_wins = self.regulation_plus_ot_wins
        regulation_win_pctg = self.regulation_win_pctg
        regulation_wins = self.regulation_wins
        road_games_played = self.road_games_played
        road_goal_differential = self.road_goal_differential
        road_goals_against = self.road_goals_against
        road_goals_for = self.road_goals_for
        road_losses = self.road_losses
        road_ot_losses = self.road_ot_losses
        road_points = self.road_points
        road_regulation_plus_ot_wins = self.road_regulation_plus_ot_wins
        road_regulation_wins = self.road_regulation_wins
        road_ties = self.road_ties
        road_wins = self.road_wins
        season_id = self.season_id
        shootout_losses = self.shootout_losses
        shootout_wins = self.shootout_wins
        streak_code = self.streak_code
        streak_count = self.streak_count
        team_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team_name, Unset):
            team_name = self.team_name.to_dict()

        team_abbrev: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team_abbrev, Unset):
            team_abbrev = self.team_abbrev.to_dict()

        team_logo = self.team_logo
        ties = self.ties
        waivers_sequence = self.waivers_sequence
        wildcard_sequence = self.wildcard_sequence
        win_pctg = self.win_pctg
        wins = self.wins

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conference_abbrev is not UNSET:
            field_dict["conferenceAbbrev"] = conference_abbrev
        if conference_home_sequence is not UNSET:
            field_dict["conferenceHomeSequence"] = conference_home_sequence
        if conference_l10_sequence is not UNSET:
            field_dict["conferenceL10Sequence"] = conference_l10_sequence
        if conference_name is not UNSET:
            field_dict["conferenceName"] = conference_name
        if conference_road_sequence is not UNSET:
            field_dict["conferenceRoadSequence"] = conference_road_sequence
        if conference_sequence is not UNSET:
            field_dict["conferenceSequence"] = conference_sequence
        if date is not UNSET:
            field_dict["date"] = date
        if division_abbrev is not UNSET:
            field_dict["divisionAbbrev"] = division_abbrev
        if division_home_sequence is not UNSET:
            field_dict["divisionHomeSequence"] = division_home_sequence
        if division_l10_sequence is not UNSET:
            field_dict["divisionL10Sequence"] = division_l10_sequence
        if division_name is not UNSET:
            field_dict["divisionName"] = division_name
        if division_road_sequence is not UNSET:
            field_dict["divisionRoadSequence"] = division_road_sequence
        if division_sequence is not UNSET:
            field_dict["divisionSequence"] = division_sequence
        if game_type_id is not UNSET:
            field_dict["gameTypeId"] = game_type_id
        if games_played is not UNSET:
            field_dict["gamesPlayed"] = games_played
        if goal_differential is not UNSET:
            field_dict["goalDifferential"] = goal_differential
        if goal_differential_pctg is not UNSET:
            field_dict["goalDifferentialPctg"] = goal_differential_pctg
        if goal_against is not UNSET:
            field_dict["goalAgainst"] = goal_against
        if goal_for is not UNSET:
            field_dict["goalFor"] = goal_for
        if goals_for_pctg is not UNSET:
            field_dict["goalsForPctg"] = goals_for_pctg
        if home_games_played is not UNSET:
            field_dict["homeGamesPlayed"] = home_games_played
        if home_goal_differential is not UNSET:
            field_dict["homeGoalDifferential"] = home_goal_differential
        if home_goals_against is not UNSET:
            field_dict["homeGoalsAgainst"] = home_goals_against
        if home_goals_for is not UNSET:
            field_dict["homeGoalsFor"] = home_goals_for
        if home_losses is not UNSET:
            field_dict["homeLosses"] = home_losses
        if home_ot_losses is not UNSET:
            field_dict["homeOtLosses"] = home_ot_losses
        if home_points is not UNSET:
            field_dict["homePoints"] = home_points
        if home_regulation_plus_ot_wins is not UNSET:
            field_dict["homeRegulationPlusOtWins"] = home_regulation_plus_ot_wins
        if home_regulation_wins is not UNSET:
            field_dict["homeRegulationWins"] = home_regulation_wins
        if home_ties is not UNSET:
            field_dict["homeTies"] = home_ties
        if home_wins is not UNSET:
            field_dict["homeWins"] = home_wins
        if l_10_games_played is not UNSET:
            field_dict["l10GamesPlayed"] = l_10_games_played
        if l_10_goal_differential is not UNSET:
            field_dict["l10GoalDifferential"] = l_10_goal_differential
        if l_10_goals_against is not UNSET:
            field_dict["l10GoalsAgainst"] = l_10_goals_against
        if l_10_goals_for is not UNSET:
            field_dict["l10GoalsFor"] = l_10_goals_for
        if l_10_losses is not UNSET:
            field_dict["l10Losses"] = l_10_losses
        if l_10_ot_losses is not UNSET:
            field_dict["l10OtLosses"] = l_10_ot_losses
        if l_10_points is not UNSET:
            field_dict["l10Points"] = l_10_points
        if l_10_regulation_plus_ot_wins is not UNSET:
            field_dict["l10RegulationPlusOtWins"] = l_10_regulation_plus_ot_wins
        if l_10_regulation_wins is not UNSET:
            field_dict["l10RegulationWins"] = l_10_regulation_wins
        if l_10_ties is not UNSET:
            field_dict["l10Ties"] = l_10_ties
        if l_10_wins is not UNSET:
            field_dict["l10Wins"] = l_10_wins
        if league_home_sequence is not UNSET:
            field_dict["leagueHomeSequence"] = league_home_sequence
        if league_l10_sequence is not UNSET:
            field_dict["leagueL10Sequence"] = league_l10_sequence
        if league_road_sequence is not UNSET:
            field_dict["leagueRoadSequence"] = league_road_sequence
        if league_sequence is not UNSET:
            field_dict["leagueSequence"] = league_sequence
        if losses is not UNSET:
            field_dict["losses"] = losses
        if ot_losses is not UNSET:
            field_dict["otLosses"] = ot_losses
        if place_name is not UNSET:
            field_dict["placeName"] = place_name
        if point_pctg is not UNSET:
            field_dict["pointPctg"] = point_pctg
        if points is not UNSET:
            field_dict["points"] = points
        if regulation_plus_ot_win_pctg is not UNSET:
            field_dict["regulationPlusOtWinPctg"] = regulation_plus_ot_win_pctg
        if regulation_plus_ot_wins is not UNSET:
            field_dict["regulationPlusOtWins"] = regulation_plus_ot_wins
        if regulation_win_pctg is not UNSET:
            field_dict["regulationWinPctg"] = regulation_win_pctg
        if regulation_wins is not UNSET:
            field_dict["regulationWins"] = regulation_wins
        if road_games_played is not UNSET:
            field_dict["roadGamesPlayed"] = road_games_played
        if road_goal_differential is not UNSET:
            field_dict["roadGoalDifferential"] = road_goal_differential
        if road_goals_against is not UNSET:
            field_dict["roadGoalsAgainst"] = road_goals_against
        if road_goals_for is not UNSET:
            field_dict["roadGoalsFor"] = road_goals_for
        if road_losses is not UNSET:
            field_dict["roadLosses"] = road_losses
        if road_ot_losses is not UNSET:
            field_dict["roadOtLosses"] = road_ot_losses
        if road_points is not UNSET:
            field_dict["roadPoints"] = road_points
        if road_regulation_plus_ot_wins is not UNSET:
            field_dict["roadRegulationPlusOtWins"] = road_regulation_plus_ot_wins
        if road_regulation_wins is not UNSET:
            field_dict["roadRegulationWins"] = road_regulation_wins
        if road_ties is not UNSET:
            field_dict["roadTies"] = road_ties
        if road_wins is not UNSET:
            field_dict["roadWins"] = road_wins
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if shootout_losses is not UNSET:
            field_dict["shootoutLosses"] = shootout_losses
        if shootout_wins is not UNSET:
            field_dict["shootoutWins"] = shootout_wins
        if streak_code is not UNSET:
            field_dict["streakCode"] = streak_code
        if streak_count is not UNSET:
            field_dict["streakCount"] = streak_count
        if team_name is not UNSET:
            field_dict["teamName"] = team_name
        if team_abbrev is not UNSET:
            field_dict["teamAbbrev"] = team_abbrev
        if team_logo is not UNSET:
            field_dict["teamLogo"] = team_logo
        if ties is not UNSET:
            field_dict["ties"] = ties
        if waivers_sequence is not UNSET:
            field_dict["waiversSequence"] = waivers_sequence
        if wildcard_sequence is not UNSET:
            field_dict["wildcardSequence"] = wildcard_sequence
        if win_pctg is not UNSET:
            field_dict["winPctg"] = win_pctg
        if wins is not UNSET:
            field_dict["wins"] = wins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        conference_abbrev = d.pop("conferenceAbbrev", UNSET)

        conference_home_sequence = d.pop("conferenceHomeSequence", UNSET)

        conference_l10_sequence = d.pop("conferenceL10Sequence", UNSET)

        conference_name = d.pop("conferenceName", UNSET)

        conference_road_sequence = d.pop("conferenceRoadSequence", UNSET)

        conference_sequence = d.pop("conferenceSequence", UNSET)

        date = d.pop("date", UNSET)

        division_abbrev = d.pop("divisionAbbrev", UNSET)

        division_home_sequence = d.pop("divisionHomeSequence", UNSET)

        division_l10_sequence = d.pop("divisionL10Sequence", UNSET)

        division_name = d.pop("divisionName", UNSET)

        division_road_sequence = d.pop("divisionRoadSequence", UNSET)

        division_sequence = d.pop("divisionSequence", UNSET)

        game_type_id = d.pop("gameTypeId", UNSET)

        games_played = d.pop("gamesPlayed", UNSET)

        goal_differential = d.pop("goalDifferential", UNSET)

        goal_differential_pctg = d.pop("goalDifferentialPctg", UNSET)

        goal_against = d.pop("goalAgainst", UNSET)

        goal_for = d.pop("goalFor", UNSET)

        goals_for_pctg = d.pop("goalsForPctg", UNSET)

        home_games_played = d.pop("homeGamesPlayed", UNSET)

        home_goal_differential = d.pop("homeGoalDifferential", UNSET)

        home_goals_against = d.pop("homeGoalsAgainst", UNSET)

        home_goals_for = d.pop("homeGoalsFor", UNSET)

        home_losses = d.pop("homeLosses", UNSET)

        home_ot_losses = d.pop("homeOtLosses", UNSET)

        home_points = d.pop("homePoints", UNSET)

        home_regulation_plus_ot_wins = d.pop("homeRegulationPlusOtWins", UNSET)

        home_regulation_wins = d.pop("homeRegulationWins", UNSET)

        home_ties = d.pop("homeTies", UNSET)

        home_wins = d.pop("homeWins", UNSET)

        l_10_games_played = d.pop("l10GamesPlayed", UNSET)

        l_10_goal_differential = d.pop("l10GoalDifferential", UNSET)

        l_10_goals_against = d.pop("l10GoalsAgainst", UNSET)

        l_10_goals_for = d.pop("l10GoalsFor", UNSET)

        l_10_losses = d.pop("l10Losses", UNSET)

        l_10_ot_losses = d.pop("l10OtLosses", UNSET)

        l_10_points = d.pop("l10Points", UNSET)

        l_10_regulation_plus_ot_wins = d.pop("l10RegulationPlusOtWins", UNSET)

        l_10_regulation_wins = d.pop("l10RegulationWins", UNSET)

        l_10_ties = d.pop("l10Ties", UNSET)

        l_10_wins = d.pop("l10Wins", UNSET)

        league_home_sequence = d.pop("leagueHomeSequence", UNSET)

        league_l10_sequence = d.pop("leagueL10Sequence", UNSET)

        league_road_sequence = d.pop("leagueRoadSequence", UNSET)

        league_sequence = d.pop("leagueSequence", UNSET)

        losses = d.pop("losses", UNSET)

        ot_losses = d.pop("otLosses", UNSET)

        _place_name = d.pop("placeName", UNSET)
        place_name: Union[Unset, LanguageString]
        if isinstance(_place_name, Unset):
            place_name = UNSET
        else:
            place_name = LanguageString.from_dict(_place_name)

        point_pctg = d.pop("pointPctg", UNSET)

        points = d.pop("points", UNSET)

        regulation_plus_ot_win_pctg = d.pop("regulationPlusOtWinPctg", UNSET)

        regulation_plus_ot_wins = d.pop("regulationPlusOtWins", UNSET)

        regulation_win_pctg = d.pop("regulationWinPctg", UNSET)

        regulation_wins = d.pop("regulationWins", UNSET)

        road_games_played = d.pop("roadGamesPlayed", UNSET)

        road_goal_differential = d.pop("roadGoalDifferential", UNSET)

        road_goals_against = d.pop("roadGoalsAgainst", UNSET)

        road_goals_for = d.pop("roadGoalsFor", UNSET)

        road_losses = d.pop("roadLosses", UNSET)

        road_ot_losses = d.pop("roadOtLosses", UNSET)

        road_points = d.pop("roadPoints", UNSET)

        road_regulation_plus_ot_wins = d.pop("roadRegulationPlusOtWins", UNSET)

        road_regulation_wins = d.pop("roadRegulationWins", UNSET)

        road_ties = d.pop("roadTies", UNSET)

        road_wins = d.pop("roadWins", UNSET)

        season_id = d.pop("seasonId", UNSET)

        shootout_losses = d.pop("shootoutLosses", UNSET)

        shootout_wins = d.pop("shootoutWins", UNSET)

        streak_code = d.pop("streakCode", UNSET)

        streak_count = d.pop("streakCount", UNSET)

        _team_name = d.pop("teamName", UNSET)
        team_name: Union[Unset, LanguageString]
        if isinstance(_team_name, Unset):
            team_name = UNSET
        else:
            team_name = LanguageString.from_dict(_team_name)

        _team_abbrev = d.pop("teamAbbrev", UNSET)
        team_abbrev: Union[Unset, LanguageString]
        if isinstance(_team_abbrev, Unset):
            team_abbrev = UNSET
        else:
            team_abbrev = LanguageString.from_dict(_team_abbrev)

        team_logo = d.pop("teamLogo", UNSET)

        ties = d.pop("ties", UNSET)

        waivers_sequence = d.pop("waiversSequence", UNSET)

        wildcard_sequence = d.pop("wildcardSequence", UNSET)

        win_pctg = d.pop("winPctg", UNSET)

        wins = d.pop("wins", UNSET)

        team_season_standings = cls(
            conference_abbrev=conference_abbrev,
            conference_home_sequence=conference_home_sequence,
            conference_l10_sequence=conference_l10_sequence,
            conference_name=conference_name,
            conference_road_sequence=conference_road_sequence,
            conference_sequence=conference_sequence,
            date=date,
            division_abbrev=division_abbrev,
            division_home_sequence=division_home_sequence,
            division_l10_sequence=division_l10_sequence,
            division_name=division_name,
            division_road_sequence=division_road_sequence,
            division_sequence=division_sequence,
            game_type_id=game_type_id,
            games_played=games_played,
            goal_differential=goal_differential,
            goal_differential_pctg=goal_differential_pctg,
            goal_against=goal_against,
            goal_for=goal_for,
            goals_for_pctg=goals_for_pctg,
            home_games_played=home_games_played,
            home_goal_differential=home_goal_differential,
            home_goals_against=home_goals_against,
            home_goals_for=home_goals_for,
            home_losses=home_losses,
            home_ot_losses=home_ot_losses,
            home_points=home_points,
            home_regulation_plus_ot_wins=home_regulation_plus_ot_wins,
            home_regulation_wins=home_regulation_wins,
            home_ties=home_ties,
            home_wins=home_wins,
            l_10_games_played=l_10_games_played,
            l_10_goal_differential=l_10_goal_differential,
            l_10_goals_against=l_10_goals_against,
            l_10_goals_for=l_10_goals_for,
            l_10_losses=l_10_losses,
            l_10_ot_losses=l_10_ot_losses,
            l_10_points=l_10_points,
            l_10_regulation_plus_ot_wins=l_10_regulation_plus_ot_wins,
            l_10_regulation_wins=l_10_regulation_wins,
            l_10_ties=l_10_ties,
            l_10_wins=l_10_wins,
            league_home_sequence=league_home_sequence,
            league_l10_sequence=league_l10_sequence,
            league_road_sequence=league_road_sequence,
            league_sequence=league_sequence,
            losses=losses,
            ot_losses=ot_losses,
            place_name=place_name,
            point_pctg=point_pctg,
            points=points,
            regulation_plus_ot_win_pctg=regulation_plus_ot_win_pctg,
            regulation_plus_ot_wins=regulation_plus_ot_wins,
            regulation_win_pctg=regulation_win_pctg,
            regulation_wins=regulation_wins,
            road_games_played=road_games_played,
            road_goal_differential=road_goal_differential,
            road_goals_against=road_goals_against,
            road_goals_for=road_goals_for,
            road_losses=road_losses,
            road_ot_losses=road_ot_losses,
            road_points=road_points,
            road_regulation_plus_ot_wins=road_regulation_plus_ot_wins,
            road_regulation_wins=road_regulation_wins,
            road_ties=road_ties,
            road_wins=road_wins,
            season_id=season_id,
            shootout_losses=shootout_losses,
            shootout_wins=shootout_wins,
            streak_code=streak_code,
            streak_count=streak_count,
            team_name=team_name,
            team_abbrev=team_abbrev,
            team_logo=team_logo,
            ties=ties,
            waivers_sequence=waivers_sequence,
            wildcard_sequence=wildcard_sequence,
            win_pctg=win_pctg,
            wins=wins,
        )

        team_season_standings.additional_properties = d
        return team_season_standings

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
