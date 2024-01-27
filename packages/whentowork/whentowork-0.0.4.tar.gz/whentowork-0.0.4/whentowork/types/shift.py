from typing import Optional, TypedDict


class Shift(TypedDict):
    """
    Type Format for Shift

    :param COMPANY_ID: Unique ID for a company
    :param SHIFT_ID: ID for a shift (Unique to the company)
    :param PUBLISHED: Y if shift is published, N if shift is not published
    :param W2W_EMPLOYEE_ID: ID for an employee (Unique over employees in W2W system)
    :param FIRST_NAME: First name of employee
    :param LAST_NAME: Last name of employee
    :param EMPLOYEE_NUMBER: ID for an employee (Unique over employees in a company)
    :param START_DATE: Start Date of shift
    :param START_TIME: Start Time of shift
    :param END_DATE: End Date of shift
    :param END_TIME: End Time of shift
    :param DURATION: Duration of shift in hours
    :param DESCRIPTION: Description of shift
    :param POSITION_ID: ID for a position (Unique to the company)
    :param POSITION_NAME: Name of Position
    :param CATEGORY_ID: ID for a category (Unique to the company)
    :param CATEGORY_NAME: Name of Category
    :param CATEGORY_SHORT: Abbreviated name of Category
    :param COLOR_ID: ID for color of shift
    :param PAY_RATE: Hourly Pay Rate of the shift
    :param POSITION_CUSTOM1:
    :param POSITION_CUSTOM2:
    :param POSITION_CUSTOM3:
    :param CATEGORY_CUSTOM1:
    :param CATEGORY_CUSTOM2:
    :param CATEGORY_CUSTOM3:
    :param LAST_CHANGED_TS: Timestamp of the last change
    :param LAST_CHANGED_BY: Name of user who last changed
    """
    COMPANY_ID: int
    SHIFT_ID: int
    PUBLISHED: bool
    W2W_EMPLOYEE_ID: int
    FIRST_NAME: str
    LAST_NAME: str
    EMPLOYEE_NUMBER: int
    START_DATE: str
    START_TIME: str
    END_DATE: str
    END_TIME: str
    DURATION: int
    DESCRIPTION: str
    POSITION_ID: int
    POSITION_NAME: str
    CATEGORY_ID: Optional[int]
    CATEGORY_NAME: Optional[str]
    CATEGORY_SHORT: Optional[str]
    COLOR_ID: int
    PAY_RATE: Optional[int]
    POSITION_CUSTOM1: str
    POSITION_CUSTOM2: str
    POSITION_CUSTOM3: str
    CATEGORY_CUSTOM1: Optional[str]
    CATEGORY_CUSTOM2: Optional[str]
    CATEGORY_CUSTOM3: Optional[str]
    LAST_CHANGED_TS: str
    LAST_CHANGED_BY: str
