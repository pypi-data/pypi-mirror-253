from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.season_standings import SeasonStandings
from typing import Dict


def _get_kwargs(
    date: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v1/standings/{date}".format(
            date=date,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SeasonStandings]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SeasonStandings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SeasonStandings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    date: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SeasonStandings]:
    """/v1/standings/2023-11-08

     **Host**: http://api-web.nhle.com

    Args:
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeasonStandings]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    date: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SeasonStandings]:
    """/v1/standings/2023-11-08

     **Host**: http://api-web.nhle.com

    Args:
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeasonStandings
    """

    return sync_detailed(
        date=date,
        client=client,
    ).parsed


async def asyncio_detailed(
    date: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SeasonStandings]:
    """/v1/standings/2023-11-08

     **Host**: http://api-web.nhle.com

    Args:
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SeasonStandings]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    date: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SeasonStandings]:
    """/v1/standings/2023-11-08

     **Host**: http://api-web.nhle.com

    Args:
        date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SeasonStandings
    """

    return (
        await asyncio_detailed(
            date=date,
            client=client,
        )
    ).parsed
