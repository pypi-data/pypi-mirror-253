from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import Dict

if TYPE_CHECKING:
    from ..models.play_by_play_plays_item_period_descriptor import PlayByPlayPlaysItemPeriodDescriptor
    from ..models.play_by_play_plays_item_details import PlayByPlayPlaysItemDetails


T = TypeVar("T", bound="PlayByPlayPlaysItem")


@_attrs_define
class PlayByPlayPlaysItem:
    """
    Attributes:
        event_id (Union[Unset, int]):
        period (Union[Unset, int]):
        sort_order (Union[Unset, int]):
        type_code (Union[Unset, int]):
        time_in_period (Union[Unset, str]):
        time_remaining (Union[Unset, str]):
        situation_code (Union[Unset, str]):
        home_team_defending_side (Union[Unset, str]):
        type_desc_key (Union[Unset, str]):
        period_descriptor (Union[Unset, PlayByPlayPlaysItemPeriodDescriptor]):
        details (Union[Unset, PlayByPlayPlaysItemDetails]):
    """

    event_id: Union[Unset, int] = UNSET
    period: Union[Unset, int] = UNSET
    sort_order: Union[Unset, int] = UNSET
    type_code: Union[Unset, int] = UNSET
    time_in_period: Union[Unset, str] = UNSET
    time_remaining: Union[Unset, str] = UNSET
    situation_code: Union[Unset, str] = UNSET
    home_team_defending_side: Union[Unset, str] = UNSET
    type_desc_key: Union[Unset, str] = UNSET
    period_descriptor: Union[Unset, "PlayByPlayPlaysItemPeriodDescriptor"] = UNSET
    details: Union[Unset, "PlayByPlayPlaysItemDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_id = self.event_id
        period = self.period
        sort_order = self.sort_order
        type_code = self.type_code
        time_in_period = self.time_in_period
        time_remaining = self.time_remaining
        situation_code = self.situation_code
        home_team_defending_side = self.home_team_defending_side
        type_desc_key = self.type_desc_key
        period_descriptor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period_descriptor, Unset):
            period_descriptor = self.period_descriptor.to_dict()

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if period is not UNSET:
            field_dict["period"] = period
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if type_code is not UNSET:
            field_dict["typeCode"] = type_code
        if time_in_period is not UNSET:
            field_dict["timeInPeriod"] = time_in_period
        if time_remaining is not UNSET:
            field_dict["timeRemaining"] = time_remaining
        if situation_code is not UNSET:
            field_dict["situationCode"] = situation_code
        if home_team_defending_side is not UNSET:
            field_dict["homeTeamDefendingSide"] = home_team_defending_side
        if type_desc_key is not UNSET:
            field_dict["typeDescKey"] = type_desc_key
        if period_descriptor is not UNSET:
            field_dict["periodDescriptor"] = period_descriptor
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.play_by_play_plays_item_period_descriptor import PlayByPlayPlaysItemPeriodDescriptor
        from ..models.play_by_play_plays_item_details import PlayByPlayPlaysItemDetails

        d = src_dict.copy()
        event_id = d.pop("eventId", UNSET)

        period = d.pop("period", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        type_code = d.pop("typeCode", UNSET)

        time_in_period = d.pop("timeInPeriod", UNSET)

        time_remaining = d.pop("timeRemaining", UNSET)

        situation_code = d.pop("situationCode", UNSET)

        home_team_defending_side = d.pop("homeTeamDefendingSide", UNSET)

        type_desc_key = d.pop("typeDescKey", UNSET)

        _period_descriptor = d.pop("periodDescriptor", UNSET)
        period_descriptor: Union[Unset, PlayByPlayPlaysItemPeriodDescriptor]
        if isinstance(_period_descriptor, Unset):
            period_descriptor = UNSET
        else:
            period_descriptor = PlayByPlayPlaysItemPeriodDescriptor.from_dict(_period_descriptor)

        _details = d.pop("details", UNSET)
        details: Union[Unset, PlayByPlayPlaysItemDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = PlayByPlayPlaysItemDetails.from_dict(_details)

        play_by_play_plays_item = cls(
            event_id=event_id,
            period=period,
            sort_order=sort_order,
            type_code=type_code,
            time_in_period=time_in_period,
            time_remaining=time_remaining,
            situation_code=situation_code,
            home_team_defending_side=home_team_defending_side,
            type_desc_key=type_desc_key,
            period_descriptor=period_descriptor,
            details=details,
        )

        play_by_play_plays_item.additional_properties = d
        return play_by_play_plays_item

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
