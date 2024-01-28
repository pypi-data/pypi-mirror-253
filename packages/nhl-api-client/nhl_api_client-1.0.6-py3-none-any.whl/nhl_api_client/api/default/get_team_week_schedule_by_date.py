from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.week_schedule import WeekSchedule
from typing import Dict


def _get_kwargs(
    team_abbrev: str,
    date: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v1/club-schedule/{team_abbrev}/week/{date}".format(
            team_abbrev=team_abbrev,
            date=date,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WeekSchedule]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WeekSchedule.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WeekSchedule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_abbrev: str,
    date: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WeekSchedule]:
    """/v1/club-schedule-season/COL/20232024

     **Host**: http://api-web.nhle.com

    Args:
        team_abbrev (str):
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WeekSchedule]
    """

    kwargs = _get_kwargs(
        team_abbrev=team_abbrev,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_abbrev: str,
    date: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WeekSchedule]:
    """/v1/club-schedule-season/COL/20232024

     **Host**: http://api-web.nhle.com

    Args:
        team_abbrev (str):
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WeekSchedule
    """

    return sync_detailed(
        team_abbrev=team_abbrev,
        date=date,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_abbrev: str,
    date: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WeekSchedule]:
    """/v1/club-schedule-season/COL/20232024

     **Host**: http://api-web.nhle.com

    Args:
        team_abbrev (str):
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WeekSchedule]
    """

    kwargs = _get_kwargs(
        team_abbrev=team_abbrev,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_abbrev: str,
    date: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WeekSchedule]:
    """/v1/club-schedule-season/COL/20232024

     **Host**: http://api-web.nhle.com

    Args:
        team_abbrev (str):
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WeekSchedule
    """

    return (
        await asyncio_detailed(
            team_abbrev=team_abbrev,
            date=date,
            client=client,
        )
    ).parsed
