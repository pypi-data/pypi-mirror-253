from typing import Optional, TypedDict


class TimeOff(TypedDict):
    """
    Type Format for TimeOff

    :param COMPANY_ID: Unique ID for a company
    :param TIMEOFF_ID: Unique ID for a Time Off Reservation
    :param W2W_EMPLOYEE_ID: ID for an employee (Unique over employees in W2W system)
    :param FIRST_NAME: First name of employee
    :param LAST_NAME: Last name of Employee
    :param EMPLOYEE_NUMBER: ID for employee (Unique over employees in the company)
    :param DESCRIPTION: Description of time off
    :param PARTIAL_DAY: Y if partial day off N if full day off
    :param START_DATE: Date of the start of time off
    :param START_TIME: Time of the start of time off
    :param END_DATE: Date of the end of time off
    :param END_TIME: Time of the end of time off
    :param WHEN_REQUESTED_TS: Timestamp of when the time off was first requested
    :param LAST_CHANGED_TS: Timestamp of when the time off was last changed
    :param LAST_CHANGED_BY: Name of User who last changed time off
    """
    COMPANY_ID: int
    TIMEOFF_ID: int
    W2W_EMPLOYEE_ID: int
    FIRST_NAME: str
    LAST_NAME: str
    EMPLOYEE_NUMBER: int
    DESCRIPTION: str
    PARTIAL_DAY: bool
    START_DATE: str
    START_TIME: str
    END_DATE: str
    END_TIME: str
    WHEN_REQUESTED_TS: str
    LAST_CHANGED_TS: str
    LAST_CHANGED_BY: str
