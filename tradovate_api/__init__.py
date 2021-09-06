##-----------------------------##
## Tradovate PyAPI             ##
## Written By: Ryan Smith      ##
##-----------------------------##

## Imports

"""
Tradovate PyAPI v1.0.0.0
"""

## Constants
__author__ = "Ryan Smith"
__title__ = "Tradovate PyAPI"
__version__ = (1, 0, 0, 0)


## Functions
def get_version() -> str:
    return 'v' + '.'.join(str(i) for i in __version__)