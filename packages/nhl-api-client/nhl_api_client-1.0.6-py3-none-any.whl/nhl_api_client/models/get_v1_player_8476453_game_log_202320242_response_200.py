from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import List
from typing import Dict

if TYPE_CHECKING:
    from ..models.get_v1_player_8476453_game_log_202320242_response_200_game_log_item import (
        GetV1Player8476453GameLog202320242Response200GameLogItem,
    )
    from ..models.get_v1_player_8476453_game_log_202320242_response_200_player_stats_seasons_item import (
        GetV1Player8476453GameLog202320242Response200PlayerStatsSeasonsItem,
    )


T = TypeVar("T", bound="GetV1Player8476453GameLog202320242Response200")


@_attrs_define
class GetV1Player8476453GameLog202320242Response200:
    """
    Attributes:
        season_id (int):
        game_type_id (int):
        player_stats_seasons (List['GetV1Player8476453GameLog202320242Response200PlayerStatsSeasonsItem']):
        game_log (List['GetV1Player8476453GameLog202320242Response200GameLogItem']):
    """

    season_id: int
    game_type_id: int
    player_stats_seasons: List["GetV1Player8476453GameLog202320242Response200PlayerStatsSeasonsItem"]
    game_log: List["GetV1Player8476453GameLog202320242Response200GameLogItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season_id = self.season_id
        game_type_id = self.game_type_id
        player_stats_seasons = []
        for player_stats_seasons_item_data in self.player_stats_seasons:
            player_stats_seasons_item = player_stats_seasons_item_data.to_dict()

            player_stats_seasons.append(player_stats_seasons_item)

        game_log = []
        for game_log_item_data in self.game_log:
            game_log_item = game_log_item_data.to_dict()

            game_log.append(game_log_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seasonId": season_id,
                "gameTypeId": game_type_id,
                "playerStatsSeasons": player_stats_seasons,
                "gameLog": game_log,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_v1_player_8476453_game_log_202320242_response_200_game_log_item import (
            GetV1Player8476453GameLog202320242Response200GameLogItem,
        )
        from ..models.get_v1_player_8476453_game_log_202320242_response_200_player_stats_seasons_item import (
            GetV1Player8476453GameLog202320242Response200PlayerStatsSeasonsItem,
        )

        d = src_dict.copy()
        season_id = d.pop("seasonId")

        game_type_id = d.pop("gameTypeId")

        player_stats_seasons = []
        _player_stats_seasons = d.pop("playerStatsSeasons")
        for player_stats_seasons_item_data in _player_stats_seasons:
            player_stats_seasons_item = GetV1Player8476453GameLog202320242Response200PlayerStatsSeasonsItem.from_dict(
                player_stats_seasons_item_data
            )

            player_stats_seasons.append(player_stats_seasons_item)

        game_log = []
        _game_log = d.pop("gameLog")
        for game_log_item_data in _game_log:
            game_log_item = GetV1Player8476453GameLog202320242Response200GameLogItem.from_dict(game_log_item_data)

            game_log.append(game_log_item)

        get_v1_player_8476453_game_log_202320242_response_200 = cls(
            season_id=season_id,
            game_type_id=game_type_id,
            player_stats_seasons=player_stats_seasons,
            game_log=game_log,
        )

        get_v1_player_8476453_game_log_202320242_response_200.additional_properties = d
        return get_v1_player_8476453_game_log_202320242_response_200

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
