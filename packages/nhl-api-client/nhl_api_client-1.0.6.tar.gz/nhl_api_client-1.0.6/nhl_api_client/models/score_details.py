from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from ..models.score_details_game_week_item import ScoreDetailsGameWeekItem
    from ..models.score_details_odds_partners_item import ScoreDetailsOddsPartnersItem
    from ..models.score_details_games_item import ScoreDetailsGamesItem


T = TypeVar("T", bound="ScoreDetails")


@_attrs_define
class ScoreDetails:
    """
    Attributes:
        prev_date (Union[Unset, str]):
        current_date (Union[Unset, str]):
        next_date (Union[Unset, str]):
        game_week (Union[Unset, List['ScoreDetailsGameWeekItem']]):
        odds_partners (Union[Unset, List['ScoreDetailsOddsPartnersItem']]):
        games (Union[Unset, List['ScoreDetailsGamesItem']]):
    """

    prev_date: Union[Unset, str] = UNSET
    current_date: Union[Unset, str] = UNSET
    next_date: Union[Unset, str] = UNSET
    game_week: Union[Unset, List["ScoreDetailsGameWeekItem"]] = UNSET
    odds_partners: Union[Unset, List["ScoreDetailsOddsPartnersItem"]] = UNSET
    games: Union[Unset, List["ScoreDetailsGamesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prev_date = self.prev_date
        current_date = self.current_date
        next_date = self.next_date
        game_week: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.game_week, Unset):
            game_week = []
            for game_week_item_data in self.game_week:
                game_week_item = game_week_item_data.to_dict()

                game_week.append(game_week_item)

        odds_partners: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.odds_partners, Unset):
            odds_partners = []
            for odds_partners_item_data in self.odds_partners:
                odds_partners_item = odds_partners_item_data.to_dict()

                odds_partners.append(odds_partners_item)

        games: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.games, Unset):
            games = []
            for games_item_data in self.games:
                games_item = games_item_data.to_dict()

                games.append(games_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prev_date is not UNSET:
            field_dict["prevDate"] = prev_date
        if current_date is not UNSET:
            field_dict["currentDate"] = current_date
        if next_date is not UNSET:
            field_dict["nextDate"] = next_date
        if game_week is not UNSET:
            field_dict["gameWeek"] = game_week
        if odds_partners is not UNSET:
            field_dict["oddsPartners"] = odds_partners
        if games is not UNSET:
            field_dict["games"] = games

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.score_details_game_week_item import ScoreDetailsGameWeekItem
        from ..models.score_details_odds_partners_item import ScoreDetailsOddsPartnersItem
        from ..models.score_details_games_item import ScoreDetailsGamesItem

        d = src_dict.copy()
        prev_date = d.pop("prevDate", UNSET)

        current_date = d.pop("currentDate", UNSET)

        next_date = d.pop("nextDate", UNSET)

        game_week = []
        _game_week = d.pop("gameWeek", UNSET)
        for game_week_item_data in _game_week or []:
            game_week_item = ScoreDetailsGameWeekItem.from_dict(game_week_item_data)

            game_week.append(game_week_item)

        odds_partners = []
        _odds_partners = d.pop("oddsPartners", UNSET)
        for odds_partners_item_data in _odds_partners or []:
            odds_partners_item = ScoreDetailsOddsPartnersItem.from_dict(odds_partners_item_data)

            odds_partners.append(odds_partners_item)

        games = []
        _games = d.pop("games", UNSET)
        for games_item_data in _games or []:
            games_item = ScoreDetailsGamesItem.from_dict(games_item_data)

            games.append(games_item)

        score_details = cls(
            prev_date=prev_date,
            current_date=current_date,
            next_date=next_date,
            game_week=game_week,
            odds_partners=odds_partners,
            games=games,
        )

        score_details.additional_properties = d
        return score_details

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
