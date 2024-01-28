from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200AwardsItemSeasonsItem")


@_attrs_define
class GetV1Player8476453LandingResponse200AwardsItemSeasonsItem:
    """
    Attributes:
        season_id (int):
        games_played (int):
        game_type_id (int):
        goals (int):
        assists (int):
        points (int):
        plus_minus (int):
        hits (int):
        blocked_shots (int):
        pim (int):
    """

    season_id: int
    games_played: int
    game_type_id: int
    goals: int
    assists: int
    points: int
    plus_minus: int
    hits: int
    blocked_shots: int
    pim: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season_id = self.season_id
        games_played = self.games_played
        game_type_id = self.game_type_id
        goals = self.goals
        assists = self.assists
        points = self.points
        plus_minus = self.plus_minus
        hits = self.hits
        blocked_shots = self.blocked_shots
        pim = self.pim

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seasonId": season_id,
                "gamesPlayed": games_played,
                "gameTypeId": game_type_id,
                "goals": goals,
                "assists": assists,
                "points": points,
                "plusMinus": plus_minus,
                "hits": hits,
                "blockedShots": blocked_shots,
                "pim": pim,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        season_id = d.pop("seasonId")

        games_played = d.pop("gamesPlayed")

        game_type_id = d.pop("gameTypeId")

        goals = d.pop("goals")

        assists = d.pop("assists")

        points = d.pop("points")

        plus_minus = d.pop("plusMinus")

        hits = d.pop("hits")

        blocked_shots = d.pop("blockedShots")

        pim = d.pop("pim")

        get_v1_player_8476453_landing_response_200_awards_item_seasons_item = cls(
            season_id=season_id,
            games_played=games_played,
            game_type_id=game_type_id,
            goals=goals,
            assists=assists,
            points=points,
            plus_minus=plus_minus,
            hits=hits,
            blocked_shots=blocked_shots,
            pim=pim,
        )

        get_v1_player_8476453_landing_response_200_awards_item_seasons_item.additional_properties = d
        return get_v1_player_8476453_landing_response_200_awards_item_seasons_item

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
