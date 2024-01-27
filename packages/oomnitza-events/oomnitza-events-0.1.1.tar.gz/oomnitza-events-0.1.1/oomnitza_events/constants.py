# -*- coding: utf-8 -*-
"""Constants module

This module defines constants for the project.
"""
from typing_extensions import Final

OOMNITZA_EMAIL_DOMAIN: Final = "oomnitza.com"

# Event names
LOGIN_EVENT_NAME: Final = "Login"
OOMNITZA_USER_LOGIN_EVENT_NAME: Final = "Oomnitza User Login"
WORKFLOW_RUN_EVENT_NAME: Final = "Workflow Run"
OBJECT_ACTION_EVENT_NAME: Final = "Object Action"
DAILY_DATA_LOAD_EVENT_NAME: Final = "Daily Data Load"

# Logging name for monitoring / log managements
OOMNITZA_EVENTS_LOG_NAME: Final = "oomnitza_events"
