from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union


T = TypeVar("T", bound="PlayByPlayClock")


@_attrs_define
class PlayByPlayClock:
    """
    Attributes:
        time_remaining (Union[Unset, str]):
        seconds_remaining (Union[Unset, int]):
        running (Union[Unset, bool]):
        in_intermission (Union[Unset, bool]):
    """

    time_remaining: Union[Unset, str] = UNSET
    seconds_remaining: Union[Unset, int] = UNSET
    running: Union[Unset, bool] = UNSET
    in_intermission: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_remaining = self.time_remaining
        seconds_remaining = self.seconds_remaining
        running = self.running
        in_intermission = self.in_intermission

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_remaining is not UNSET:
            field_dict["timeRemaining"] = time_remaining
        if seconds_remaining is not UNSET:
            field_dict["secondsRemaining"] = seconds_remaining
        if running is not UNSET:
            field_dict["running"] = running
        if in_intermission is not UNSET:
            field_dict["inIntermission"] = in_intermission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time_remaining = d.pop("timeRemaining", UNSET)

        seconds_remaining = d.pop("secondsRemaining", UNSET)

        running = d.pop("running", UNSET)

        in_intermission = d.pop("inIntermission", UNSET)

        play_by_play_clock = cls(
            time_remaining=time_remaining,
            seconds_remaining=seconds_remaining,
            running=running,
            in_intermission=in_intermission,
        )

        play_by_play_clock.additional_properties = d
        return play_by_play_clock

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
