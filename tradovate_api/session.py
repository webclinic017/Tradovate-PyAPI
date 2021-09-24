#!/usr/bin/python
##-------------------------------##
## Tradovate PyAPI               ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Session Class                 ##
##-------------------------------##

## Imports
from __future__ import annotations

from aiohttp import ClientSession


## Classes
class Session:
    """Tradovate Session"""

    # -Constructor
    def __init__(self) -> Session:
        self.authenticated: bool = False
        self._aiosession: ClientSession = ClientSession(raise_for_status=True)

    # -Dunder Methods
    def __repr__(self) -> str:
        return f"Session(authenticated={self.authenticated})"

    # -Instance Methods
    async def close(self) -> None:
        self.authenticated = False
        await self._aiosession.close()
