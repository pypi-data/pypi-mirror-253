from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union


T = TypeVar("T", bound="ScoreDetailsOddsPartnersItem")


@_attrs_define
class ScoreDetailsOddsPartnersItem:
    """
    Attributes:
        partner_id (Union[Unset, int]):
        country (Union[Unset, str]):
        name (Union[Unset, str]):
        image_url (Union[Unset, str]):
        site_url (Union[Unset, str]):
        bg_color (Union[Unset, str]):
        text_color (Union[Unset, str]):
        accent_color (Union[Unset, str]):
    """

    partner_id: Union[Unset, int] = UNSET
    country: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    site_url: Union[Unset, str] = UNSET
    bg_color: Union[Unset, str] = UNSET
    text_color: Union[Unset, str] = UNSET
    accent_color: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        partner_id = self.partner_id
        country = self.country
        name = self.name
        image_url = self.image_url
        site_url = self.site_url
        bg_color = self.bg_color
        text_color = self.text_color
        accent_color = self.accent_color

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if country is not UNSET:
            field_dict["country"] = country
        if name is not UNSET:
            field_dict["name"] = name
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if site_url is not UNSET:
            field_dict["siteUrl"] = site_url
        if bg_color is not UNSET:
            field_dict["bgColor"] = bg_color
        if text_color is not UNSET:
            field_dict["textColor"] = text_color
        if accent_color is not UNSET:
            field_dict["accentColor"] = accent_color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        partner_id = d.pop("partnerId", UNSET)

        country = d.pop("country", UNSET)

        name = d.pop("name", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        site_url = d.pop("siteUrl", UNSET)

        bg_color = d.pop("bgColor", UNSET)

        text_color = d.pop("textColor", UNSET)

        accent_color = d.pop("accentColor", UNSET)

        score_details_odds_partners_item = cls(
            partner_id=partner_id,
            country=country,
            name=name,
            image_url=image_url,
            site_url=site_url,
            bg_color=bg_color,
            text_color=text_color,
            accent_color=accent_color,
        )

        score_details_odds_partners_item.additional_properties = d
        return score_details_odds_partners_item

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
