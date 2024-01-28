from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.play_by_play import PlayByPlay
from typing import Dict


def _get_kwargs(
    game_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v1/gamecenter/{game_id}/play-by-play".format(
            game_id=game_id,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PlayByPlay]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PlayByPlay.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PlayByPlay]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PlayByPlay]:
    """/v1/gamecenter/game_id/play-by-play

     **Host**: http://api-web.nhle.com

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlayByPlay]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PlayByPlay]:
    """/v1/gamecenter/game_id/play-by-play

     **Host**: http://api-web.nhle.com

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlayByPlay
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    game_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PlayByPlay]:
    """/v1/gamecenter/game_id/play-by-play

     **Host**: http://api-web.nhle.com

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlayByPlay]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PlayByPlay]:
    """/v1/gamecenter/game_id/play-by-play

     **Host**: http://api-web.nhle.com

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlayByPlay
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
        )
    ).parsed
