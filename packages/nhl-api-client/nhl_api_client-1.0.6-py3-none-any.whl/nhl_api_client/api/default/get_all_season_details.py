from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Union
from ...models.get_all_season_details_response_200 import GetAllSeasonDetailsResponse200
from typing import Dict
from typing import Optional
from ...types import UNSET, Unset


def _get_kwargs(
    *,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/stats/rest/en/season",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllSeasonDetailsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAllSeasonDetailsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllSeasonDetailsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sort: Union[Unset, None, str] = UNSET,
) -> Response[GetAllSeasonDetailsResponse200]:
    """/stats/rest/en/season

     **Host**: http://api.nhle.com

    Args:
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllSeasonDetailsResponse200]
    """

    kwargs = _get_kwargs(
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[GetAllSeasonDetailsResponse200]:
    """/stats/rest/en/season

     **Host**: http://api.nhle.com

    Args:
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllSeasonDetailsResponse200
    """

    return sync_detailed(
        client=client,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sort: Union[Unset, None, str] = UNSET,
) -> Response[GetAllSeasonDetailsResponse200]:
    """/stats/rest/en/season

     **Host**: http://api.nhle.com

    Args:
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllSeasonDetailsResponse200]
    """

    kwargs = _get_kwargs(
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[GetAllSeasonDetailsResponse200]:
    """/stats/rest/en/season

     **Host**: http://api.nhle.com

    Args:
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllSeasonDetailsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            sort=sort,
        )
    ).parsed
