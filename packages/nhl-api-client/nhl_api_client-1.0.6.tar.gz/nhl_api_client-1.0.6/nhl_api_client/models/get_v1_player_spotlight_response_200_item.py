from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import Dict

if TYPE_CHECKING:
    from ..models.language_string import LanguageString


T = TypeVar("T", bound="GetV1PlayerSpotlightResponse200Item")


@_attrs_define
class GetV1PlayerSpotlightResponse200Item:
    """
    Attributes:
        player_id (int):
        name (LanguageString):
        player_slug (str):
        position (str):
        sweater_number (int):
        team_id (int):
        headshot (str):
        team_tri_code (str):
        team_logo (str):
        sort_id (int):
    """

    player_id: int
    name: "LanguageString"
    player_slug: str
    position: str
    sweater_number: int
    team_id: int
    headshot: str
    team_tri_code: str
    team_logo: str
    sort_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id
        name = self.name.to_dict()

        player_slug = self.player_slug
        position = self.position
        sweater_number = self.sweater_number
        team_id = self.team_id
        headshot = self.headshot
        team_tri_code = self.team_tri_code
        team_logo = self.team_logo
        sort_id = self.sort_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "playerId": player_id,
                "name": name,
                "playerSlug": player_slug,
                "position": position,
                "sweaterNumber": sweater_number,
                "teamId": team_id,
                "headshot": headshot,
                "teamTriCode": team_tri_code,
                "teamLogo": team_logo,
                "sortId": sort_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        player_id = d.pop("playerId")

        name = LanguageString.from_dict(d.pop("name"))

        player_slug = d.pop("playerSlug")

        position = d.pop("position")

        sweater_number = d.pop("sweaterNumber")

        team_id = d.pop("teamId")

        headshot = d.pop("headshot")

        team_tri_code = d.pop("teamTriCode")

        team_logo = d.pop("teamLogo")

        sort_id = d.pop("sortId")

        get_v1_player_spotlight_response_200_item = cls(
            player_id=player_id,
            name=name,
            player_slug=player_slug,
            position=position,
            sweater_number=sweater_number,
            team_id=team_id,
            headshot=headshot,
            team_tri_code=team_tri_code,
            team_logo=team_logo,
            sort_id=sort_id,
        )

        get_v1_player_spotlight_response_200_item.additional_properties = d
        return get_v1_player_spotlight_response_200_item

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
