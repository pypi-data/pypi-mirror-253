from typing import Any, Dict, Type, TypeVar, Optional

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import Optional
from dateutil.parser import isoparse
import datetime


T = TypeVar("T", bound="GetAllSeasonDetailsResponse200DataItem")


@_attrs_define
class GetAllSeasonDetailsResponse200DataItem:
    """
    Attributes:
        id (int):
        all_star_game_in_use (int):
        conferences_in_use (int):
        divisions_in_use (int):
        end_date (datetime.datetime):
        entry_draft_in_use (int):
        formatted_season_id (str):
        minimum_playoff_minutes_for_goalie_stats_leaders (int):
        minimum_regular_games_for_goalie_stats_leaders (int):
        nhl_stanley_cup_owner (int):
        number_of_games (int):
        olympics_participation (int):
        point_for_ot_loss_in_use (int):
        regular_season_end_date (datetime.datetime):
        row_in_use (int):
        season_ordinal (int):
        start_date (datetime.datetime):
        supplemental_draft_in_use (int):
        ties_in_use (int):
        total_playoff_games (int):
        total_regular_season_games (int):
        wildcard_in_use (int):
        preseason_startdate (Optional[datetime.datetime]):
    """

    id: int
    all_star_game_in_use: int
    conferences_in_use: int
    divisions_in_use: int
    end_date: datetime.datetime
    entry_draft_in_use: int
    formatted_season_id: str
    minimum_playoff_minutes_for_goalie_stats_leaders: int
    minimum_regular_games_for_goalie_stats_leaders: int
    nhl_stanley_cup_owner: int
    number_of_games: int
    olympics_participation: int
    point_for_ot_loss_in_use: int
    regular_season_end_date: datetime.datetime
    row_in_use: int
    season_ordinal: int
    start_date: datetime.datetime
    supplemental_draft_in_use: int
    ties_in_use: int
    total_playoff_games: int
    total_regular_season_games: int
    wildcard_in_use: int
    preseason_startdate: Optional[datetime.datetime]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        all_star_game_in_use = self.all_star_game_in_use
        conferences_in_use = self.conferences_in_use
        divisions_in_use = self.divisions_in_use
        end_date = self.end_date.isoformat()

        entry_draft_in_use = self.entry_draft_in_use
        formatted_season_id = self.formatted_season_id
        minimum_playoff_minutes_for_goalie_stats_leaders = self.minimum_playoff_minutes_for_goalie_stats_leaders
        minimum_regular_games_for_goalie_stats_leaders = self.minimum_regular_games_for_goalie_stats_leaders
        nhl_stanley_cup_owner = self.nhl_stanley_cup_owner
        number_of_games = self.number_of_games
        olympics_participation = self.olympics_participation
        point_for_ot_loss_in_use = self.point_for_ot_loss_in_use
        regular_season_end_date = self.regular_season_end_date.isoformat()

        row_in_use = self.row_in_use
        season_ordinal = self.season_ordinal
        start_date = self.start_date.isoformat()

        supplemental_draft_in_use = self.supplemental_draft_in_use
        ties_in_use = self.ties_in_use
        total_playoff_games = self.total_playoff_games
        total_regular_season_games = self.total_regular_season_games
        wildcard_in_use = self.wildcard_in_use
        preseason_startdate = self.preseason_startdate.isoformat() if self.preseason_startdate else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "allStarGameInUse": all_star_game_in_use,
                "conferencesInUse": conferences_in_use,
                "divisionsInUse": divisions_in_use,
                "endDate": end_date,
                "entryDraftInUse": entry_draft_in_use,
                "formattedSeasonId": formatted_season_id,
                "minimumPlayoffMinutesForGoalieStatsLeaders": minimum_playoff_minutes_for_goalie_stats_leaders,
                "minimumRegularGamesForGoalieStatsLeaders": minimum_regular_games_for_goalie_stats_leaders,
                "nhlStanleyCupOwner": nhl_stanley_cup_owner,
                "numberOfGames": number_of_games,
                "olympicsParticipation": olympics_participation,
                "pointForOTLossInUse": point_for_ot_loss_in_use,
                "regularSeasonEndDate": regular_season_end_date,
                "rowInUse": row_in_use,
                "seasonOrdinal": season_ordinal,
                "startDate": start_date,
                "supplementalDraftInUse": supplemental_draft_in_use,
                "tiesInUse": ties_in_use,
                "totalPlayoffGames": total_playoff_games,
                "totalRegularSeasonGames": total_regular_season_games,
                "wildcardInUse": wildcard_in_use,
                "preseasonStartdate": preseason_startdate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        all_star_game_in_use = d.pop("allStarGameInUse")

        conferences_in_use = d.pop("conferencesInUse")

        divisions_in_use = d.pop("divisionsInUse")

        end_date = isoparse(d.pop("endDate"))

        entry_draft_in_use = d.pop("entryDraftInUse")

        formatted_season_id = d.pop("formattedSeasonId")

        minimum_playoff_minutes_for_goalie_stats_leaders = d.pop("minimumPlayoffMinutesForGoalieStatsLeaders")

        minimum_regular_games_for_goalie_stats_leaders = d.pop("minimumRegularGamesForGoalieStatsLeaders")

        nhl_stanley_cup_owner = d.pop("nhlStanleyCupOwner")

        number_of_games = d.pop("numberOfGames")

        olympics_participation = d.pop("olympicsParticipation")

        point_for_ot_loss_in_use = d.pop("pointForOTLossInUse")

        regular_season_end_date = isoparse(d.pop("regularSeasonEndDate"))

        row_in_use = d.pop("rowInUse")

        season_ordinal = d.pop("seasonOrdinal")

        start_date = isoparse(d.pop("startDate"))

        supplemental_draft_in_use = d.pop("supplementalDraftInUse")

        ties_in_use = d.pop("tiesInUse")

        total_playoff_games = d.pop("totalPlayoffGames")

        total_regular_season_games = d.pop("totalRegularSeasonGames")

        wildcard_in_use = d.pop("wildcardInUse")

        _preseason_startdate = d.pop("preseasonStartdate")
        preseason_startdate: Optional[datetime.datetime]
        if _preseason_startdate is None:
            preseason_startdate = None
        else:
            preseason_startdate = isoparse(_preseason_startdate)

        get_all_season_details_response_200_data_item = cls(
            id=id,
            all_star_game_in_use=all_star_game_in_use,
            conferences_in_use=conferences_in_use,
            divisions_in_use=divisions_in_use,
            end_date=end_date,
            entry_draft_in_use=entry_draft_in_use,
            formatted_season_id=formatted_season_id,
            minimum_playoff_minutes_for_goalie_stats_leaders=minimum_playoff_minutes_for_goalie_stats_leaders,
            minimum_regular_games_for_goalie_stats_leaders=minimum_regular_games_for_goalie_stats_leaders,
            nhl_stanley_cup_owner=nhl_stanley_cup_owner,
            number_of_games=number_of_games,
            olympics_participation=olympics_participation,
            point_for_ot_loss_in_use=point_for_ot_loss_in_use,
            regular_season_end_date=regular_season_end_date,
            row_in_use=row_in_use,
            season_ordinal=season_ordinal,
            start_date=start_date,
            supplemental_draft_in_use=supplemental_draft_in_use,
            ties_in_use=ties_in_use,
            total_playoff_games=total_playoff_games,
            total_regular_season_games=total_regular_season_games,
            wildcard_in_use=wildcard_in_use,
            preseason_startdate=preseason_startdate,
        )

        get_all_season_details_response_200_data_item.additional_properties = d
        return get_all_season_details_response_200_data_item

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
