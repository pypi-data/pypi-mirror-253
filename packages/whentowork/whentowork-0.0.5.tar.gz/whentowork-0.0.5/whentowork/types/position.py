from typing import Optional, TypedDict


class Position(TypedDict):
    """
    Type Format for Position

    :param COMPANY_ID: Unique ID for a company
    :param POSITION_ID: ID for a position (Unique to the company)
    :param POSITION_NAME: Name of Position
    :param POSITION_CUSTOM1:
    :param POSITION_CUSTOM2:
    :param POSITION_CUSTOM3:
    :param LAST_CHANGED_TS: Timestamp of last change to position
    """
    COMPANY_ID: int
    POSITION_ID: int
    POSITION_NAME: str
    POSITION_CUSTOM1: str
    POSITION_CUSTOM2: str
    POSITION_CUSTOM3: str
    LAST_CHANGED_TS: Optional[str]
