##-----------------------------##
## Tradovate PyAPI             ##
## Written By: Ryan Smith      ##
##-----------------------------##
## Profile Class               ##
##-----------------------------##

## Imports
from __future__ import annotations

import requests

from ..utils import urls

## Constants


## Functions


## Classes
class Profile:
    """"""

    # -Constructor
    def __init__(self, token: str) -> Profile:
        # -Account Details
        self.id: int = None
        self.name: str = None
        self.email: str = None
        self.trial: bool = True
        self.verified: bool = False
        # -Temporary
        self.header = {
            'AUTHORIZATION': "Bearer " + token
        }
        r = requests.get(urls.base_live + urls.auth_me, headers=self.header)
        if r.status_code == 200:
            r = r.json()
            self.id = r['userId']
            self.name = r['fullName']
            self.email = r['email']
            self.trial = r['isTrial']
            self.verified = r['emailVerified']

    # -Dunder Methods

    # -Instance Methods

    # -Class Methods

    # -Static Methods

    # -Properties

    # -Class Properties

    # -Sub-Classes


## Body
