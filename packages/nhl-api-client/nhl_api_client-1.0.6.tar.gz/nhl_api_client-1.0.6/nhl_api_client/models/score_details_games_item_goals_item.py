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
    from ..models.score_details_games_item_goals_item_period_descriptor import (
        ScoreDetailsGamesItemGoalsItemPeriodDescriptor,
    )


T = TypeVar("T", bound="ScoreDetailsGamesItemGoalsItem")


@_attrs_define
class ScoreDetailsGamesItemGoalsItem:
    """
    Attributes:
        period (Union[Unset, int]):
        period_descriptor (Union[Unset, ScoreDetailsGamesItemGoalsItemPeriodDescriptor]):
        time_in_period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        name (Union[Unset, LanguageString]):
        mugshot (Union[Unset, str]):
        team_abbrev (Union[Unset, str]):
        goals_to_date (Union[Unset, int]):
        away_score (Union[Unset, int]):
        home_score (Union[Unset, int]):
        strength (Union[Unset, str]):
        highlight_clip (Union[Unset, int]):
        highlight_clip_fr (Union[Unset, int]):
    """

    period: Union[Unset, int] = UNSET
    period_descriptor: Union[Unset, "ScoreDetailsGamesItemGoalsItemPeriodDescriptor"] = UNSET
    time_in_period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    name: Union[Unset, "LanguageString"] = UNSET
    mugshot: Union[Unset, str] = UNSET
    team_abbrev: Union[Unset, str] = UNSET
    goals_to_date: Union[Unset, int] = UNSET
    away_score: Union[Unset, int] = UNSET
    home_score: Union[Unset, int] = UNSET
    strength: Union[Unset, str] = UNSET
    highlight_clip: Union[Unset, int] = UNSET
    highlight_clip_fr: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period
        period_descriptor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period_descriptor, Unset):
            period_descriptor = self.period_descriptor.to_dict()

        time_in_period = self.time_in_period
        player_id = self.player_id
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        mugshot = self.mugshot
        team_abbrev = self.team_abbrev
        goals_to_date = self.goals_to_date
        away_score = self.away_score
        home_score = self.home_score
        strength = self.strength
        highlight_clip = self.highlight_clip
        highlight_clip_fr = self.highlight_clip_fr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if period_descriptor is not UNSET:
            field_dict["periodDescriptor"] = period_descriptor
        if time_in_period is not UNSET:
            field_dict["timeInPeriod"] = time_in_period
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if name is not UNSET:
            field_dict["name"] = name
        if mugshot is not UNSET:
            field_dict["mugshot"] = mugshot
        if team_abbrev is not UNSET:
            field_dict["teamAbbrev"] = team_abbrev
        if goals_to_date is not UNSET:
            field_dict["goalsToDate"] = goals_to_date
        if away_score is not UNSET:
            field_dict["awayScore"] = away_score
        if home_score is not UNSET:
            field_dict["homeScore"] = home_score
        if strength is not UNSET:
            field_dict["strength"] = strength
        if highlight_clip is not UNSET:
            field_dict["highlightClip"] = highlight_clip
        if highlight_clip_fr is not UNSET:
            field_dict["highlightClipFr"] = highlight_clip_fr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString
        from ..models.score_details_games_item_goals_item_period_descriptor import (
            ScoreDetailsGamesItemGoalsItemPeriodDescriptor,
        )

        d = src_dict.copy()
        period = d.pop("period", UNSET)

        _period_descriptor = d.pop("periodDescriptor", UNSET)
        period_descriptor: Union[Unset, ScoreDetailsGamesItemGoalsItemPeriodDescriptor]
        if isinstance(_period_descriptor, Unset):
            period_descriptor = UNSET
        else:
            period_descriptor = ScoreDetailsGamesItemGoalsItemPeriodDescriptor.from_dict(_period_descriptor)

        time_in_period = d.pop("timeInPeriod", UNSET)

        player_id = d.pop("playerId", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, LanguageString]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = LanguageString.from_dict(_name)

        mugshot = d.pop("mugshot", UNSET)

        team_abbrev = d.pop("teamAbbrev", UNSET)

        goals_to_date = d.pop("goalsToDate", UNSET)

        away_score = d.pop("awayScore", UNSET)

        home_score = d.pop("homeScore", UNSET)

        strength = d.pop("strength", UNSET)

        highlight_clip = d.pop("highlightClip", UNSET)

        highlight_clip_fr = d.pop("highlightClipFr", UNSET)

        score_details_games_item_goals_item = cls(
            period=period,
            period_descriptor=period_descriptor,
            time_in_period=time_in_period,
            player_id=player_id,
            name=name,
            mugshot=mugshot,
            team_abbrev=team_abbrev,
            goals_to_date=goals_to_date,
            away_score=away_score,
            home_score=home_score,
            strength=strength,
            highlight_clip=highlight_clip,
            highlight_clip_fr=highlight_clip_fr,
        )

        score_details_games_item_goals_item.additional_properties = d
        return score_details_games_item_goals_item

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
