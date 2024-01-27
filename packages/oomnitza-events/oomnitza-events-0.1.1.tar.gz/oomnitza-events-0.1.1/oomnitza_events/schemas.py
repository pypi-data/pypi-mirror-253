# -*- coding: utf-8 -*-
"""Schemas module

This module defines data schemas for validating properties coming through
the trackers.
"""
from typing_extensions import Final

CLIENT_TYPES: Final = ("mobile", "web")
AUTH_TYPES: Final = ("basic", "saml")
ACTION_TYPES: Final = ("view", "create", "edit", "delete", "restore")
WF_STATUS: Final = ("start", "done")
AGENT_TYPES: Final = (
    "api",
    "connector",
    "import",
    "ticket_plugin",
    "webui",
    "wf",
    "jit",
    "saas",
)
OBJECT_TYPES: Final = (
    "accessories",
    "assets",
    "audits",
    "contracts",
    "locations",
    "users",
    "saas",
    "software",
    "stockrooms",
)
SYSTEM_TYPES: Final = ("demo", "dev", "poc", "prod", "sandbox", "preprod")
MODULE_ENABLED_VALUES: Final = ("enabled", "disabled")


USER_SCHEMA: Final = {
    "full_name": {
        "type": "string",
        "required": True,
        "nullable": True,  # 'empty' default is True
    },
    "role": {"type": "string", "required": True, "nullable": True},
    "server": {"type": "string", "required": True, "empty": False},
    "system_type": {"type": "string", "allowed": SYSTEM_TYPES, "required": True},
    "oomnitza_events_version": {"type": "string", "required": True, "empty": False},
}


UPLOAD_SCHEMA: Final = {
    "server": {"type": "string", "required": True, "empty": False},
    "system_type": {"type": "string", "allowed": SYSTEM_TYPES, "required": True},
    "oomnitza_events_version": {"type": "string", "required": True, "empty": False},
}


USER_UPLOAD_SCHEMA: Final = {
    "user_id": {"type": "string", "required": True, "empty": False},
    "full_name": {"type": "string", "required": True, "nullable": True},
    "role": {"type": "string", "required": True, "nullable": True},
}


LOGIN_SCHEMA: Final = {
    "client_type": {"type": "string", "allowed": CLIENT_TYPES, "required": True},
    "auth_type": {"type": "string", "allowed": AUTH_TYPES, "required": True},
    "identity_provider": {
        "type": "string",
        "required": True,
        "nullable": True,  # 'empty' default is True
    },
    "user_agent": {"type": "string", "required": True, "nullable": True},
    "server": {
        "type": "string",
        "required": True,
        "empty": False,  # 'nullable' default is False
    },
    "system_type": {"type": "string", "allowed": SYSTEM_TYPES, "required": True},
    "oomnitza_events_version": {"type": "string", "required": True, "empty": False},
}


OOMNITZA_USER_LOGIN_SCHEMA: Final = {
    "email": {"type": "string", "required": True, "empty": False},
    "ip_address": {"type": "string", "required": True, "nullable": True},
    "role": {"type": "string", "required": True, "nullable": True},
    "access_date": {"type": "string", "required": True, "empty": False},
    "reason": {"type": "string", "required": True, "nullable": True},
    "description": {"type": "string", "required": True, "nullable": True},
    "server": {
        "type": "string",
        "required": True,
        "empty": False,  # 'nullable' default is False
    },
    "system_type": {"type": "string", "allowed": SYSTEM_TYPES, "required": True},
    "oomnitza_events_version": {"type": "string", "required": True, "empty": False},
}

WORKFLOW_RUN_SCHEMA: Final = {
    "run_id": {"type": "integer", "required": True},
    "wf_id": {"type": "integer", "required": True},
    "wf_external_id": {"type": "string", "required": True},
    "wf_name": {"type": "string", "required": True, "empty": False},
    "action_type": {"type": "string", "required": True},
    "object_type": {"type": "string", "required": True},
    "status": {"type": "string", "required": True, "allowed": WF_STATUS},
    "server": {"type": "string", "required": True, "empty": False},
    "system_type": {"type": "string", "allowed": SYSTEM_TYPES, "required": True},
    "oomnitza_events_version": {"type": "string", "required": True, "empty": False},
}

OBJECT_ACTION_SCHEMA: Final = {
    "action_type": {"type": "string", "required": True, "allowed": ACTION_TYPES},
    "agent_type": {"type": "string", "required": True, "allowed": AGENT_TYPES},
    "agent_name": {
        "type": "string",
        "required": True,
        "nullable": True,  # 'empty' default is True
    },
    "object_type": {"type": "string", "required": True, "allowed": OBJECT_TYPES},
    "server": {"type": "string", "required": True, "empty": False},
    "system_type": {"type": "string", "allowed": SYSTEM_TYPES, "required": True},
    "oomnitza_events_version": {"type": "string", "required": True, "empty": False},
}

DAILY_DATA_LOAD_SCHEMA: Final = {
    "accessories_enabled": {
        "type": "string",
        "required": True,
        "allowed": MODULE_ENABLED_VALUES,
    },
    "accessories_total_active": {"type": "integer", "required": True},
    "accessories_total_archived": {"type": "integer", "required": True},
    "accessories_wf_total_active": {"type": "integer", "required": True},
    "accessories_total_history": {"type": "integer", "required": True},
    "assets_enabled": {
        "type": "string",
        "required": True,
        "allowed": MODULE_ENABLED_VALUES,
    },
    "assets_total_active": {"type": "integer", "required": True},
    "assets_total_archived": {"type": "integer", "required": True},
    "assets_wf_total_active": {"type": "integer", "required": True},
    "assets_total_history": {"type": "integer", "required": True},
    "contracts_enabled": {
        "type": "string",
        "required": True,
        "allowed": MODULE_ENABLED_VALUES,
    },
    "contracts_total_active": {"type": "integer", "required": True},
    "contracts_total_archived": {"type": "integer", "required": True},
    "contracts_wf_total_active": {"type": "integer", "required": True},
    "contracts_total_history": {"type": "integer", "required": True},
    "locations_total_active": {"type": "integer", "required": True},
    "locations_total_archived": {"type": "integer", "required": True},
    "locations_wf_total_active": {"type": "integer", "required": True},
    "locations_total_history": {"type": "integer", "required": True},
    "users_enabled": {
        "type": "string",
        "required": True,
        "allowed": MODULE_ENABLED_VALUES,
    },
    "users_total_active": {"type": "integer", "required": True},
    "users_total_archived": {"type": "integer", "required": True},
    "users_wf_total_active": {"type": "integer", "required": True},
    "users_total_history": {"type": "integer", "required": True},
    "saas_enabled": {
        "type": "string",
        "required": True,
        "allowed": MODULE_ENABLED_VALUES,
    },
    "saas_total_active": {"type": "integer", "required": True},
    "saas_total_archived": {"type": "integer", "required": True},
    "saas_wf_total_active": {"type": "integer", "required": True},
    "saas_total_history": {"type": "integer", "required": True},
    "saas_users_wf_total_active": {"type": "integer", "required": True},
    "software_enabled": {
        "type": "string",
        "required": True,
        "allowed": MODULE_ENABLED_VALUES,
    },
    "software_total_active": {"type": "integer", "required": True},
    "software_total_archived": {"type": "integer", "required": True},
    "software_wf_total_active": {"type": "integer", "required": True},
    "software_total_history": {"type": "integer", "required": True},
    "stockrooms_total_active": {"type": "integer", "required": True},
    "stockrooms_total_archived": {"type": "integer", "required": True},
    "stockrooms_wf_total_active": {"type": "integer", "required": True},
    "stockrooms_total_history": {"type": "integer", "required": True},
    "audits_wf_total_active": {"type": "integer", "required": True},
    "transactions_wf_total_active": {"type": "integer", "required": True},
    "migrations_enabled": {
        "type": "string",
        "required": True,
        "allowed": MODULE_ENABLED_VALUES,
    },
    "wf_total_active": {"type": "integer", "required": True},
    "roles_total_active": {"type": "integer", "required": True},
    "last_login_date": {"type": "string", "required": True, "nullable": True},
    "total_logins_past_7_days": {"type": "integer", "required": True},
    "total_logins_past_4_weeks": {"type": "integer", "required": True},
    "server": {"type": "string", "required": True, "empty": False},
    "release_version": {"type": "string", "required": True},
    "system_type": {"type": "string", "required": True, "allowed": SYSTEM_TYPES},
    "oomnitza_events_version": {"type": "string", "required": True, "empty": False},
}
