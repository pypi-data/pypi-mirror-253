from typing import Optional, TypedDict


class Category(TypedDict):
    """
    Type Format for Category

    :param COMPANY_ID: Unique ID for a company
    :param CATEGORY_ID: ID for a Category (Unique to the company)
    :param CATEGORY_NAME: Name of Category
    :param CATEGORY_SHORT: Abbreviated name of Category
    :param CATEGORY_CUSTOM1:
    :param CATEGORY_CUSTOM2:
    :param CATEGORY_CUSTOM3:
    :param LAST_CHANGED_TS: Timestamp of last change to Category
    """
    COMPANY_ID: int
    CATEGORY_ID: int
    CATEGORY_NAME: str
    CATEGORY_SHORT: str
    CATEGORY_CUSTOM1: str
    CATEGORY_CUSTOM2: str
    CATEGORY_CUSTOM3: str
    LAST_CHANGED_TS: Optional[str]
