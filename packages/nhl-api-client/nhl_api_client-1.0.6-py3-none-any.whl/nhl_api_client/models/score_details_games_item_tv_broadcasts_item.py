from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union


T = TypeVar("T", bound="ScoreDetailsGamesItemTvBroadcastsItem")


@_attrs_define
class ScoreDetailsGamesItemTvBroadcastsItem:
    """
    Attributes:
        id (Union[Unset, int]):
        market (Union[Unset, str]):
        country_code (Union[Unset, str]):
        network (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    market: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        market = self.market
        country_code = self.country_code
        network = self.network

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if market is not UNSET:
            field_dict["market"] = market
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        market = d.pop("market", UNSET)

        country_code = d.pop("countryCode", UNSET)

        network = d.pop("network", UNSET)

        score_details_games_item_tv_broadcasts_item = cls(
            id=id,
            market=market,
            country_code=country_code,
            network=network,
        )

        score_details_games_item_tv_broadcasts_item.additional_properties = d
        return score_details_games_item_tv_broadcasts_item

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
