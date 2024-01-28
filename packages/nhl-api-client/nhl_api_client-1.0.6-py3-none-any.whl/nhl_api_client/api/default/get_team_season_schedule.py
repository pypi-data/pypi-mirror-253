from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.season_schedule import SeasonSchedule
from typing import Dict


def _get_kwargs(
    team_abbrev: str,
    season_code: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v1/club-schedule-season/{team_abbrev}/{season_code}".format(
            team_abbrev=team_abbrev,
            season_code=season_code,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SeasonSchedule]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SeasonSchedule.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SeasonSchedule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_abbrev: str,
    season_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SeasonSchedule]:
    """/v1/club-schedule-season/COL/20232024

     **Host**: http://api-web.nhle.com

    Args:
        team_abbrev (str):
        season_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeasonSchedule]
    """

    kwargs = _get_kwargs(
        team_abbrev=team_abbrev,
        season_code=season_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_abbrev: str,
    season_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SeasonSchedule]:
    """/v1/club-schedule-season/COL/20232024

     **Host**: http://api-web.nhle.com

    Args:
        team_abbrev (str):
        season_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeasonSchedule
    """

    return sync_detailed(
        team_abbrev=team_abbrev,
        season_code=season_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_abbrev: str,
    season_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SeasonSchedule]:
    """/v1/club-schedule-season/COL/20232024

     **Host**: http://api-web.nhle.com

    Args:
        team_abbrev (str):
        season_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeasonSchedule]
    """

    kwargs = _get_kwargs(
        team_abbrev=team_abbrev,
        season_code=season_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_abbrev: str,
    season_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SeasonSchedule]:
    """/v1/club-schedule-season/COL/20232024

     **Host**: http://api-web.nhle.com

    Args:
        team_abbrev (str):
        season_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeasonSchedule
    """

    return (
        await asyncio_detailed(
            team_abbrev=team_abbrev,
            season_code=season_code,
            client=client,
        )
    ).parsed
