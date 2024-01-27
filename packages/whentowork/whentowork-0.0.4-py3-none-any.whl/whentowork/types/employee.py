from typing import Optional, TypedDict


class Employee(TypedDict):
    """
    Type Format for Employee

    :param COMPANY_ID: Unique ID for a company
    :param W2W_EMPLOYEE_ID: ID for an employee (Unique over employees in W2W system)
    :param EMPLOYEE_NUMBER: ID for employee (Unique over employees in the company)
    :param FIRST_NAME: First name of employee
    :param LAST_NAME: Last name of Employee
    :param PHONE: Primary Phone number of employee
    :param PHONE_2: Secondary Phone number of employee
    :param MOBILE_PHONE: Mobile phone number of employee
    :param EMAILS: Email of employee
    :param LAST_SIGN_IN: Datetime of last sign to W2W in for employee
    :param SIGN_IN_COUNT: Number of times employee has signed in to W2W
    :param ADDRESS: Street address of employee
    :param ADDRESS_2: Unit/Apt number of employee
    :param CITY: City of employee’s address
    :param STATE: State of employee’s address
    :param ZIP: Zip Code of Employee’s address
    :param COMMENTS: Comments managers have given to employee
    :param MAX_HRS_DAY: Maximum allowed hours assigned per day for employee
    :param MAX_SHIFTS_DAY: Maximum allowed Shifts assigned per day for employee
    :param MAX_HRS_WEEK: Maximum allowed hours assigned per week for employee
    :param MAX_DAYS_WEEK: Maximum allowed days assigned per week for employee
    :param HIRE_DATE: Date employee was hired
    :param STATUS: Custom status icon
    :param PRIORITY_GROUP: Priority group employee is a part of when scheduling
    :param CUSTOM_1: Custom text field 1
    :param CUSTOM_2: Custom text field 2
    :param BIWEEKLY_TARGET_HRS: Target hours to be assigned to employee every 2 weeks
    :param PAY_RATE: Hourly Pay rate for employee
    :param ALERT_DATE:
    :param NEXT_ALERT
    """
    COMPANY_ID: int
    W2W_EMPLOYEE_ID: int
    EMPLOYEE_NUMBER: int
    FIRST_NAME: str
    LAST_NAME: str
    PHONE: str
    PHONE_2: str
    MOBILE_PHONE: str
    EMAILS: str
    LAST_SIGN_IN: str
    SIGN_IN_COUNT: int
    ADDRESS: str
    ADDRESS_2: str
    CITY: str
    STATE: str
    ZIP: str
    COMMENTS: str
    MAX_HRS_DAY: int
    MAX_SHIFTS_DAY: int
    MAX_HRS_WEEK: int
    MAX_DAYS_WEEK: int
    HIRE_DATE: str
    STATUS: int
    PRIORITY_GROUP: int
    CUSTOM_1: str
    CUSTOM_2: str
    BIWEEKLY_TARGET_HRS: int
    PAY_RATE: Optional[int]
    ALERT_DATE: str
    NEXT_ALERT: str
