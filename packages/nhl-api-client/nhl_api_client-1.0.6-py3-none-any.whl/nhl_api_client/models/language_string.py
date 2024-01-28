from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union


T = TypeVar("T", bound="LanguageString")


@_attrs_define
class LanguageString:
    """
    Attributes:
        default (Union[Unset, str]):
        fr (Union[Unset, None, str]):
        sk (Union[Unset, None, str]):
        cs (Union[Unset, None, str]):
        fi (Union[Unset, None, str]):
        de (Union[Unset, None, str]):
        sv (Union[Unset, None, str]):
        es (Union[Unset, None, str]):
    """

    default: Union[Unset, str] = UNSET
    fr: Union[Unset, None, str] = UNSET
    sk: Union[Unset, None, str] = UNSET
    cs: Union[Unset, None, str] = UNSET
    fi: Union[Unset, None, str] = UNSET
    de: Union[Unset, None, str] = UNSET
    sv: Union[Unset, None, str] = UNSET
    es: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default = self.default
        fr = self.fr
        sk = self.sk
        cs = self.cs
        fi = self.fi
        de = self.de
        sv = self.sv
        es = self.es

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if fr is not UNSET:
            field_dict["fr"] = fr
        if sk is not UNSET:
            field_dict["sk"] = sk
        if cs is not UNSET:
            field_dict["cs"] = cs
        if fi is not UNSET:
            field_dict["fi"] = fi
        if de is not UNSET:
            field_dict["de"] = de
        if sv is not UNSET:
            field_dict["sv"] = sv
        if es is not UNSET:
            field_dict["es"] = es

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        default = d.pop("default", UNSET)

        fr = d.pop("fr", UNSET)

        sk = d.pop("sk", UNSET)

        cs = d.pop("cs", UNSET)

        fi = d.pop("fi", UNSET)

        de = d.pop("de", UNSET)

        sv = d.pop("sv", UNSET)

        es = d.pop("es", UNSET)

        language_string = cls(
            default=default,
            fr=fr,
            sk=sk,
            cs=cs,
            fi=fi,
            de=de,
            sv=sv,
            es=es,
        )

        language_string.additional_properties = d
        return language_string

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
