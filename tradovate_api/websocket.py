#!/usr/bin/python
##-------------------------------##
## Tradovate PyAPI               ##
## Written By: Ryan Smith        ##
##-------------------------------##
## WebSocket Class               ##
##-------------------------------##

## Imports
from __future__ import annotations

from aiohttp import ClientWebSocketResponse


## Classes
class WebSocket:
    """Tradovate WebSocket"""

    # -Constructor
    def __init__(self, websocket: ClientWebSocketResponse) -> WebSocket:
        self.authenticated: bool = False
        self._aiowebsocket: ClientWebSocketResponse = websocket

    # -Dunder Methods
    def __repr__(self) -> str:
        return f"WebSocket(authenticated={self.authenticated})"

    # -Instance Methods
    async def close(self) -> None:
        self.authenticated = False
        await self._aiowebsocket.close()
