from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.get_v1_player_8476453_landing_response_200 import GetV1Player8476453LandingResponse200
from typing import Dict


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v1/player/8476453/landing",
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetV1Player8476453LandingResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetV1Player8476453LandingResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetV1Player8476453LandingResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetV1Player8476453LandingResponse200]:
    """/v1/player/8476453/landing

     **Host**: http://api-web.nhle.com

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1Player8476453LandingResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetV1Player8476453LandingResponse200]:
    """/v1/player/8476453/landing

     **Host**: http://api-web.nhle.com

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1Player8476453LandingResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetV1Player8476453LandingResponse200]:
    """/v1/player/8476453/landing

     **Host**: http://api-web.nhle.com

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1Player8476453LandingResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetV1Player8476453LandingResponse200]:
    """/v1/player/8476453/landing

     **Host**: http://api-web.nhle.com

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1Player8476453LandingResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
