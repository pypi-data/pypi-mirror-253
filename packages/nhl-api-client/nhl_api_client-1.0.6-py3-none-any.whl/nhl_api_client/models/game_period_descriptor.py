from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union


T = TypeVar("T", bound="GamePeriodDescriptor")


@_attrs_define
class GamePeriodDescriptor:
    """
    Attributes:
        number (Union[Unset, None, int]):
        period_type (Union[Unset, str]):
    """

    number: Union[Unset, None, int] = UNSET
    period_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        period_type = self.period_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if period_type is not UNSET:
            field_dict["periodType"] = period_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        period_type = d.pop("periodType", UNSET)

        game_period_descriptor = cls(
            number=number,
            period_type=period_type,
        )

        game_period_descriptor.additional_properties = d
        return game_period_descriptor

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
