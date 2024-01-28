from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import List
from typing import Dict

if TYPE_CHECKING:
    from ..models.get_v1_player_8476453_landing_response_200_awards_item import (
        GetV1Player8476453LandingResponse200AwardsItem,
    )
    from ..models.get_v1_player_8476453_landing_response_200_last_5_games_item import (
        GetV1Player8476453LandingResponse200Last5GamesItem,
    )
    from ..models.get_v1_player_8476453_landing_response_200_season_totals_item import (
        GetV1Player8476453LandingResponse200SeasonTotalsItem,
    )
    from ..models.language_string import LanguageString
    from ..models.get_v1_player_8476453_landing_response_200_draft_details import (
        GetV1Player8476453LandingResponse200DraftDetails,
    )
    from ..models.get_v1_player_8476453_landing_response_200_current_team_roster_item import (
        GetV1Player8476453LandingResponse200CurrentTeamRosterItem,
    )
    from ..models.get_v1_player_8476453_landing_response_200_career_totals import (
        GetV1Player8476453LandingResponse200CareerTotals,
    )
    from ..models.get_v1_player_8476453_landing_response_200_featured_stats import (
        GetV1Player8476453LandingResponse200FeaturedStats,
    )


T = TypeVar("T", bound="GetV1Player8476453LandingResponse200")


@_attrs_define
class GetV1Player8476453LandingResponse200:
    """
    Attributes:
        player_id (int):
        is_active (bool):
        current_team_id (int):
        current_team_abbrev (str):
        full_team_name (LanguageString):
        first_name (LanguageString):
        last_name (LanguageString):
        team_logo (str):
        sweater_number (int):
        position (str):
        headshot (str):
        hero_image (str):
        height_in_inches (int):
        height_in_centimeters (int):
        weight_in_pounds (int):
        weight_in_kilograms (int):
        birth_date (str):
        birth_city (LanguageString):
        birth_country (str):
        shoots_catches (str):
        draft_details (GetV1Player8476453LandingResponse200DraftDetails):
        player_slug (str):
        in_top_100_all_time (int):
        in_hhof (int):
        featured_stats (GetV1Player8476453LandingResponse200FeaturedStats):
        career_totals (GetV1Player8476453LandingResponse200CareerTotals):
        shop_link (str):
        twitter_link (str):
        watch_link (str):
        last_5_games (List['GetV1Player8476453LandingResponse200Last5GamesItem']):
        season_totals (List['GetV1Player8476453LandingResponse200SeasonTotalsItem']):
        awards (List['GetV1Player8476453LandingResponse200AwardsItem']):
        current_team_roster (List['GetV1Player8476453LandingResponse200CurrentTeamRosterItem']):
    """

    player_id: int
    is_active: bool
    current_team_id: int
    current_team_abbrev: str
    full_team_name: "LanguageString"
    first_name: "LanguageString"
    last_name: "LanguageString"
    team_logo: str
    sweater_number: int
    position: str
    headshot: str
    hero_image: str
    height_in_inches: int
    height_in_centimeters: int
    weight_in_pounds: int
    weight_in_kilograms: int
    birth_date: str
    birth_city: "LanguageString"
    birth_country: str
    shoots_catches: str
    draft_details: "GetV1Player8476453LandingResponse200DraftDetails"
    player_slug: str
    in_top_100_all_time: int
    in_hhof: int
    featured_stats: "GetV1Player8476453LandingResponse200FeaturedStats"
    career_totals: "GetV1Player8476453LandingResponse200CareerTotals"
    shop_link: str
    twitter_link: str
    watch_link: str
    last_5_games: List["GetV1Player8476453LandingResponse200Last5GamesItem"]
    season_totals: List["GetV1Player8476453LandingResponse200SeasonTotalsItem"]
    awards: List["GetV1Player8476453LandingResponse200AwardsItem"]
    current_team_roster: List["GetV1Player8476453LandingResponse200CurrentTeamRosterItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id
        is_active = self.is_active
        current_team_id = self.current_team_id
        current_team_abbrev = self.current_team_abbrev
        full_team_name = self.full_team_name.to_dict()

        first_name = self.first_name.to_dict()

        last_name = self.last_name.to_dict()

        team_logo = self.team_logo
        sweater_number = self.sweater_number
        position = self.position
        headshot = self.headshot
        hero_image = self.hero_image
        height_in_inches = self.height_in_inches
        height_in_centimeters = self.height_in_centimeters
        weight_in_pounds = self.weight_in_pounds
        weight_in_kilograms = self.weight_in_kilograms
        birth_date = self.birth_date
        birth_city = self.birth_city.to_dict()

        birth_country = self.birth_country
        shoots_catches = self.shoots_catches
        draft_details = self.draft_details.to_dict()

        player_slug = self.player_slug
        in_top_100_all_time = self.in_top_100_all_time
        in_hhof = self.in_hhof
        featured_stats = self.featured_stats.to_dict()

        career_totals = self.career_totals.to_dict()

        shop_link = self.shop_link
        twitter_link = self.twitter_link
        watch_link = self.watch_link
        last_5_games = []
        for last_5_games_item_data in self.last_5_games:
            last_5_games_item = last_5_games_item_data.to_dict()

            last_5_games.append(last_5_games_item)

        season_totals = []
        for season_totals_item_data in self.season_totals:
            season_totals_item = season_totals_item_data.to_dict()

            season_totals.append(season_totals_item)

        awards = []
        for awards_item_data in self.awards:
            awards_item = awards_item_data.to_dict()

            awards.append(awards_item)

        current_team_roster = []
        for current_team_roster_item_data in self.current_team_roster:
            current_team_roster_item = current_team_roster_item_data.to_dict()

            current_team_roster.append(current_team_roster_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "playerId": player_id,
                "isActive": is_active,
                "currentTeamId": current_team_id,
                "currentTeamAbbrev": current_team_abbrev,
                "fullTeamName": full_team_name,
                "firstName": first_name,
                "lastName": last_name,
                "teamLogo": team_logo,
                "sweaterNumber": sweater_number,
                "position": position,
                "headshot": headshot,
                "heroImage": hero_image,
                "heightInInches": height_in_inches,
                "heightInCentimeters": height_in_centimeters,
                "weightInPounds": weight_in_pounds,
                "weightInKilograms": weight_in_kilograms,
                "birthDate": birth_date,
                "birthCity": birth_city,
                "birthCountry": birth_country,
                "shootsCatches": shoots_catches,
                "draftDetails": draft_details,
                "playerSlug": player_slug,
                "inTop100AllTime": in_top_100_all_time,
                "inHHOF": in_hhof,
                "featuredStats": featured_stats,
                "careerTotals": career_totals,
                "shopLink": shop_link,
                "twitterLink": twitter_link,
                "watchLink": watch_link,
                "last5Games": last_5_games,
                "seasonTotals": season_totals,
                "awards": awards,
                "currentTeamRoster": current_team_roster,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_v1_player_8476453_landing_response_200_awards_item import (
            GetV1Player8476453LandingResponse200AwardsItem,
        )
        from ..models.get_v1_player_8476453_landing_response_200_last_5_games_item import (
            GetV1Player8476453LandingResponse200Last5GamesItem,
        )
        from ..models.get_v1_player_8476453_landing_response_200_season_totals_item import (
            GetV1Player8476453LandingResponse200SeasonTotalsItem,
        )
        from ..models.language_string import LanguageString
        from ..models.get_v1_player_8476453_landing_response_200_draft_details import (
            GetV1Player8476453LandingResponse200DraftDetails,
        )
        from ..models.get_v1_player_8476453_landing_response_200_current_team_roster_item import (
            GetV1Player8476453LandingResponse200CurrentTeamRosterItem,
        )
        from ..models.get_v1_player_8476453_landing_response_200_career_totals import (
            GetV1Player8476453LandingResponse200CareerTotals,
        )
        from ..models.get_v1_player_8476453_landing_response_200_featured_stats import (
            GetV1Player8476453LandingResponse200FeaturedStats,
        )

        d = src_dict.copy()
        player_id = d.pop("playerId")

        is_active = d.pop("isActive")

        current_team_id = d.pop("currentTeamId")

        current_team_abbrev = d.pop("currentTeamAbbrev")

        full_team_name = LanguageString.from_dict(d.pop("fullTeamName"))

        first_name = LanguageString.from_dict(d.pop("firstName"))

        last_name = LanguageString.from_dict(d.pop("lastName"))

        team_logo = d.pop("teamLogo")

        sweater_number = d.pop("sweaterNumber")

        position = d.pop("position")

        headshot = d.pop("headshot")

        hero_image = d.pop("heroImage")

        height_in_inches = d.pop("heightInInches")

        height_in_centimeters = d.pop("heightInCentimeters")

        weight_in_pounds = d.pop("weightInPounds")

        weight_in_kilograms = d.pop("weightInKilograms")

        birth_date = d.pop("birthDate")

        birth_city = LanguageString.from_dict(d.pop("birthCity"))

        birth_country = d.pop("birthCountry")

        shoots_catches = d.pop("shootsCatches")

        draft_details = GetV1Player8476453LandingResponse200DraftDetails.from_dict(d.pop("draftDetails"))

        player_slug = d.pop("playerSlug")

        in_top_100_all_time = d.pop("inTop100AllTime")

        in_hhof = d.pop("inHHOF")

        featured_stats = GetV1Player8476453LandingResponse200FeaturedStats.from_dict(d.pop("featuredStats"))

        career_totals = GetV1Player8476453LandingResponse200CareerTotals.from_dict(d.pop("careerTotals"))

        shop_link = d.pop("shopLink")

        twitter_link = d.pop("twitterLink")

        watch_link = d.pop("watchLink")

        last_5_games = []
        _last_5_games = d.pop("last5Games")
        for last_5_games_item_data in _last_5_games:
            last_5_games_item = GetV1Player8476453LandingResponse200Last5GamesItem.from_dict(last_5_games_item_data)

            last_5_games.append(last_5_games_item)

        season_totals = []
        _season_totals = d.pop("seasonTotals")
        for season_totals_item_data in _season_totals:
            season_totals_item = GetV1Player8476453LandingResponse200SeasonTotalsItem.from_dict(season_totals_item_data)

            season_totals.append(season_totals_item)

        awards = []
        _awards = d.pop("awards")
        for awards_item_data in _awards:
            awards_item = GetV1Player8476453LandingResponse200AwardsItem.from_dict(awards_item_data)

            awards.append(awards_item)

        current_team_roster = []
        _current_team_roster = d.pop("currentTeamRoster")
        for current_team_roster_item_data in _current_team_roster:
            current_team_roster_item = GetV1Player8476453LandingResponse200CurrentTeamRosterItem.from_dict(
                current_team_roster_item_data
            )

            current_team_roster.append(current_team_roster_item)

        get_v1_player_8476453_landing_response_200 = cls(
            player_id=player_id,
            is_active=is_active,
            current_team_id=current_team_id,
            current_team_abbrev=current_team_abbrev,
            full_team_name=full_team_name,
            first_name=first_name,
            last_name=last_name,
            team_logo=team_logo,
            sweater_number=sweater_number,
            position=position,
            headshot=headshot,
            hero_image=hero_image,
            height_in_inches=height_in_inches,
            height_in_centimeters=height_in_centimeters,
            weight_in_pounds=weight_in_pounds,
            weight_in_kilograms=weight_in_kilograms,
            birth_date=birth_date,
            birth_city=birth_city,
            birth_country=birth_country,
            shoots_catches=shoots_catches,
            draft_details=draft_details,
            player_slug=player_slug,
            in_top_100_all_time=in_top_100_all_time,
            in_hhof=in_hhof,
            featured_stats=featured_stats,
            career_totals=career_totals,
            shop_link=shop_link,
            twitter_link=twitter_link,
            watch_link=watch_link,
            last_5_games=last_5_games,
            season_totals=season_totals,
            awards=awards,
            current_team_roster=current_team_roster,
        )

        get_v1_player_8476453_landing_response_200.additional_properties = d
        return get_v1_player_8476453_landing_response_200

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
