from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import Dict

if TYPE_CHECKING:
    from ..models.language_string import LanguageString


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200CurrentTeamRosterItem")


@_attrs_define
class GetV1Player8476453LandingResponse200CurrentTeamRosterItem:
    """
    Attributes:
        player_id (int):
        last_name (LanguageString):
        first_name (LanguageString):
        player_slug (str):
    """

    player_id: int
    last_name: "LanguageString"
    first_name: "LanguageString"
    player_slug: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id
        last_name = self.last_name.to_dict()

        first_name = self.first_name.to_dict()

        player_slug = self.player_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "playerId": player_id,
                "lastName": last_name,
                "firstName": first_name,
                "playerSlug": player_slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        player_id = d.pop("playerId")

        last_name = LanguageString.from_dict(d.pop("lastName"))

        first_name = LanguageString.from_dict(d.pop("firstName"))

        player_slug = d.pop("playerSlug")

        get_v1_player_8476453_landing_response_200_current_team_roster_item = cls(
            player_id=player_id,
            last_name=last_name,
            first_name=first_name,
            player_slug=player_slug,
        )

        get_v1_player_8476453_landing_response_200_current_team_roster_item.additional_properties = d
        return get_v1_player_8476453_landing_response_200_current_team_roster_item

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
