
from alerta.app import severity
from alerta.models import severity_code

"""
Possible alert status codes.
"""

EMPTY_STATUS_CODE= 1
OPEN_STATUS_CODE = 2
ASSIGN_STATUS_CODE = 3
ACK_STATUS_CODE = 4
CLOSED_STATUS_CODE = 5
EXPIRED_STATUS_CODE = 6
UNKNOWN_STATUS_CODE = 9

EMPTY = 'empty'
OPEN = 'open'
ASSIGN = 'assign'
ACK = 'ack'
CLOSED = 'closed'
EXPIRED = 'expired'
UNKNOWN = 'unknown'
NOT_VALID = 'notValid'

ALL = [EMPTY, OPEN, ASSIGN, ACK, CLOSED, EXPIRED, UNKNOWN]

_STATUS_MAP = {
    EMPTY: EMPTY_STATUS_CODE,
    OPEN: OPEN_STATUS_CODE,
    ASSIGN: ASSIGN_STATUS_CODE,
    ACK: ACK_STATUS_CODE,
    CLOSED: CLOSED_STATUS_CODE,
    EXPIRED: EXPIRED_STATUS_CODE,
    UNKNOWN: UNKNOWN_STATUS_CODE,

}


def is_valid(name):
    return name in _STATUS_MAP


def name_to_code(name):
    return _STATUS_MAP.get(name, UNKNOWN_STATUS_CODE)


def parse_status(name):
    if name:
        for st in _STATUS_MAP:
            if name.lower() == st.lower():
                return st
    return NOT_VALID


def status_from_severity(previous_severity, current_severity, current_status=OPEN):
    if current_severity in [severity_code.NORMAL, severity_code.CLEARED, severity_code.OK]:
        return CLOSED
    if current_status in [CLOSED, EXPIRED]:
        return OPEN
    if severity.trend(previous_severity, current_severity) == severity_code.MORE_SEVERE:
        return OPEN
    return current_status
