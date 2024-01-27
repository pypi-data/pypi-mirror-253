import cerberus
import pytest

from oomnitza_events.schemas import (
    DAILY_DATA_LOAD_SCHEMA,
    LOGIN_SCHEMA,
    OBJECT_ACTION_SCHEMA,
    OOMNITZA_USER_LOGIN_SCHEMA,
    WORKFLOW_RUN_SCHEMA,
)


@pytest.fixture(scope="module")
def get_validator():
    return cerberus.Validator()


@pytest.fixture()
def load_mock_data():
    def _load_mock_data(track_type):
        return {
            "login": {
                "client_type": "web",
                "auth_type": "saml",
                "identity_provider": "foo",
                "user_agent": "foo",
                "server": "bar",
                "system_type": "dev",
                "oomnitza_events_version": "0.0.1",
            },
            "oomnitza_user_login": {
                "email": "foo.bar@oom.com",
                "ip_address": "127.0.0.1",
                "role": "Super Admin",
                "access_date": "2020-10-22T15:05:41.000Z",
                "reason": "foo",
                "description": "bar",
                "server": "bar",
                "system_type": "dev",
                "oomnitza_events_version": "0.0.1",
            },
            "workflow_run": {
                "run_id": 196,
                "wf_id": 1,
                "wf_external_id": "mock_ext_id",
                "wf_name": "foo",
                "action_type": "create",
                "object_type": "assets",
                "status": "start",
                "server": "bar",
                "system_type": "dev",
                "oomnitza_events_version": "0.0.1",
            },
            "object_action": {
                "action_type": "create",
                "agent_type": "connector",
                "agent_name": "okta",
                "object_type": "assets",
                "server": "bar",
                "system_type": "dev",
                "oomnitza_events_version": "0.0.1",
            },
            "daily_data_load": {
                "accessories_enabled": "enabled",
                "accessories_total_active": 0,
                "accessories_total_archived": 0,
                "accessories_total_history": 0,
                "accessories_wf_total_active": 0,
                "assets_enabled": "enabled",
                "assets_total_active": 0,
                "assets_total_history": 0,
                "assets_total_archived": 0,
                "assets_wf_total_active": 0,
                "contracts_enabled": "enabled",
                "contracts_total_active": 0,
                "contracts_total_archived": 0,
                "contracts_total_history": 0,
                "contracts_wf_total_active": 0,
                "locations_total_active": 0,
                "locations_total_archived": 0,
                "locations_total_history": 0,
                "locations_wf_total_active": 0,
                "users_enabled": "enabled",
                "users_total_active": 0,
                "users_total_archived": 0,
                "users_total_history": 0,
                "users_wf_total_active": 0,
                "saas_enabled": "enabled",
                "saas_total_active": 0,
                "saas_total_archived": 0,
                "saas_total_history": 0,
                "saas_wf_total_active": 0,
                "saas_users_wf_total_active": 0,
                "software_enabled": 0,
                "software_total_active": 0,
                "software_total_archived": 0,
                "software_total_history": 0,
                "software_wf_total_active": 0,
                "stockrooms_total_active": 0,
                "stockrooms_total_archived": 0,
                "stockrooms_total_history": 0,
                "stockrooms_wf_total_active": 0,
                "audits_wf_total_active": 0,
                "transactions_wf_total_active": 0,
                "migrations_enabled": "enabled",
                "wf_total_active": 0,
                "roles_total_active": 0,
                "last_login_date": "2020-10-22T15:05:41.000Z",
                "total_logins_past_7_days": 0,
                "total_logins_past_4_weeks": 0,
                "release_version": "0.0.1",
                "server": "bar",
                "system_type": "dev",
                "oomnitza_events_version": "0.0.1",
            },
        }.get(track_type)

    return _load_mock_data


def load_all_required_fields():
    return [
        (
            "login",
            LOGIN_SCHEMA,
            (
                "client_type",
                "auth_type",
                "identity_provider",
                "user_agent",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "oomnitza_user_login",
            OOMNITZA_USER_LOGIN_SCHEMA,
            (
                "email",
                "ip_address",
                "role",
                "access_date",
                "reason",
                "description",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "workflow_run",
            WORKFLOW_RUN_SCHEMA,
            (
                "run_id",
                "wf_id",
                "wf_external_id",
                "wf_name",
                "action_type",
                "object_type",
                "status",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "object_action",
            OBJECT_ACTION_SCHEMA,
            (
                "action_type",
                "agent_type",
                "agent_name",
                "object_type",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "daily_data_load",
            DAILY_DATA_LOAD_SCHEMA,
            (
                "accessories_enabled",
                "accessories_total_active",
                "accessories_total_archived",
                "accessories_wf_total_active",
                "accessories_total_history",
                "assets_enabled",
                "assets_total_active",
                "assets_total_archived",
                "assets_wf_total_active",
                "assets_total_history",
                "contracts_enabled",
                "contracts_total_active",
                "contracts_total_archived",
                "contracts_wf_total_active",
                "contracts_total_history",
                "locations_total_active",
                "locations_total_archived",
                "locations_wf_total_active",
                "locations_total_history",
                "users_enabled",
                "users_total_active",
                "users_total_archived",
                "users_wf_total_active",
                "users_total_history",
                "saas_enabled",
                "saas_total_active",
                "saas_total_archived",
                "saas_wf_total_active",
                "saas_users_wf_total_active",
                "saas_total_history",
                "software_enabled",
                "software_total_active",
                "software_total_archived",
                "software_wf_total_active",
                "software_total_history",
                "stockrooms_total_active",
                "stockrooms_total_archived",
                "stockrooms_wf_total_active",
                "stockrooms_total_history",
                "audits_wf_total_active",
                "transactions_wf_total_active",
                "migrations_enabled",
                "wf_total_active",
                "roles_total_active",
                "last_login_date",
                "total_logins_past_7_days",
                "total_logins_past_4_weeks",
                "release_version",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
    ]


def load_all_string_fields():
    return [
        (
            "login",
            LOGIN_SCHEMA,
            (
                "client_type",
                "auth_type",
                "identity_provider",
                "user_agent",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "oomnitza_user_login",
            OOMNITZA_USER_LOGIN_SCHEMA,
            (
                "email",
                "ip_address",
                "role",
                "access_date",
                "reason",
                "description",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "workflow_run",
            WORKFLOW_RUN_SCHEMA,
            (
                "wf_name",
                "action_type",
                "object_type",
                "status",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "object_action",
            OBJECT_ACTION_SCHEMA,
            (
                "action_type",
                "agent_type",
                "agent_name",
                "object_type",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "daily_data_load",
            DAILY_DATA_LOAD_SCHEMA,
            (
                "accessories_enabled",
                "assets_enabled",
                "contracts_enabled",
                "users_enabled",
                "saas_enabled",
                "software_enabled",
                "migrations_enabled",
                "last_login_date",
                "release_version",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
    ]


def load_all_integer_fields():
    return [
        ("workflow_run", WORKFLOW_RUN_SCHEMA, ("run_id", "wf_id")),
        (
            "daily_data_load",
            DAILY_DATA_LOAD_SCHEMA,
            (
                "accessories_total_active",
                "accessories_total_archived",
                "accessories_wf_total_active",
                "accessories_total_history",
                "assets_total_active",
                "assets_total_archived",
                "assets_wf_total_active",
                "assets_total_history",
                "contracts_total_active",
                "contracts_total_archived",
                "contracts_wf_total_active",
                "contracts_total_history",
                "locations_total_active",
                "locations_total_archived",
                "locations_wf_total_active",
                "locations_total_history",
                "users_total_active",
                "users_total_archived",
                "users_wf_total_active",
                "users_total_history",
                "saas_total_active",
                "saas_total_archived",
                "saas_wf_total_active",
                "saas_users_wf_total_active",
                "saas_total_history",
                "software_total_active",
                "software_total_archived",
                "software_wf_total_active",
                "software_total_history",
                "stockrooms_total_active",
                "stockrooms_total_archived",
                "stockrooms_wf_total_active",
                "stockrooms_total_history",
                "audits_wf_total_active",
                "transactions_wf_total_active",
                "wf_total_active",
                "roles_total_active",
                "total_logins_past_7_days",
                "total_logins_past_4_weeks",
            ),
        ),
    ]


def load_all_fields_null_not_allowed():
    return [
        (
            "login",
            LOGIN_SCHEMA,
            (
                "client_type",
                "auth_type",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "oomnitza_user_login",
            OOMNITZA_USER_LOGIN_SCHEMA,
            (
                "email",
                "access_date",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "workflow_run",
            WORKFLOW_RUN_SCHEMA,
            (
                "run_id",
                "wf_id",
                "wf_external_id",
                "wf_name",
                "action_type",
                "object_type",
                "status",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "object_action",
            OBJECT_ACTION_SCHEMA,
            (
                "action_type",
                "agent_type",
                "object_type",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "daily_data_load",
            DAILY_DATA_LOAD_SCHEMA,
            (
                "accessories_enabled",
                "accessories_total_active",
                "accessories_total_archived",
                "accessories_wf_total_active",
                "assets_enabled",
                "assets_total_active",
                "assets_total_archived",
                "assets_wf_total_active",
                "contracts_enabled",
                "contracts_total_active",
                "contracts_total_archived",
                "contracts_wf_total_active",
                "locations_total_active",
                "locations_total_archived",
                "locations_wf_total_active",
                "users_enabled",
                "users_total_active",
                "users_total_archived",
                "users_wf_total_active",
                "saas_enabled",
                "saas_total_active",
                "saas_total_archived",
                "saas_wf_total_active",
                "saas_users_wf_total_active",
                "software_enabled",
                "software_total_active",
                "software_total_archived",
                "software_wf_total_active",
                "stockrooms_total_active",
                "stockrooms_total_archived",
                "stockrooms_wf_total_active",
                "audits_wf_total_active",
                "transactions_wf_total_active",
                "migrations_enabled",
                "wf_total_active",
                "roles_total_active",
                "total_logins_past_7_days",
                "total_logins_past_4_weeks",
                "release_version",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
    ]


def load_all_fields_empty_not_allowed():
    return [
        (
            "login",
            LOGIN_SCHEMA,
            (
                "client_type",
                "auth_type",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "oomnitza_user_login",
            OOMNITZA_USER_LOGIN_SCHEMA,
            (
                "email",
                "access_date",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "workflow_run",
            WORKFLOW_RUN_SCHEMA,
            (
                "wf_name",
                "status",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "object_action",
            OBJECT_ACTION_SCHEMA,
            (
                "action_type",
                "agent_type",
                "object_type",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
        (
            "daily_data_load",
            DAILY_DATA_LOAD_SCHEMA,
            (
                "accessories_enabled",
                "assets_enabled",
                "contracts_enabled",
                "users_enabled",
                "saas_enabled",
                "software_enabled",
                "migrations_enabled",
                "server",
                "system_type",
                "oomnitza_events_version",
            ),
        ),
    ]


def load_all_fields_with_specified_allowed_values():
    return [
        ("login", LOGIN_SCHEMA, ("client_type", "auth_type", "system_type")),
        ("oomnitza_user_login", OOMNITZA_USER_LOGIN_SCHEMA, ("system_type")),
        (
            "workflow_run",
            WORKFLOW_RUN_SCHEMA,
            ("status", "system_type"),
        ),
        (
            "object_action",
            OBJECT_ACTION_SCHEMA,
            ("action_type", "agent_type", "object_type", "system_type"),
        ),
        (
            "daily_data_load",
            DAILY_DATA_LOAD_SCHEMA,
            (
                "accessories_enabled",
                "assets_enabled",
                "contracts_enabled",
                "users_enabled",
                "saas_enabled",
                "software_enabled",
                "migrations_enabled",
                "system_type",
            ),
        ),
    ]


@pytest.mark.parametrize(
    ("track_type", "schema", "candidates"),
    load_all_required_fields(),
)
def test_missing_required_field(
    track_type,
    schema,
    candidates,
    load_mock_data,
    get_validator,
):
    for candidate in candidates:
        mock_data = load_mock_data(track_type)
        mock_data.pop(candidate)
        assert not get_validator.validate(mock_data, schema)


@pytest.mark.parametrize(
    ("track_type", "schema", "candidates"),
    load_all_string_fields(),
)
def test_str_field_with_non_string_value(
    track_type,
    schema,
    candidates,
    load_mock_data,
    get_validator,
):
    for candidate in candidates:
        for non_str_val in (0, True):
            mock_data = load_mock_data(track_type)
            mock_data[candidate] = non_str_val
            assert not get_validator.validate(mock_data, schema)


@pytest.mark.parametrize(
    ("track_type", "schema", "candidates"),
    load_all_integer_fields(),
)
def test_int_field_with_non_int_value(
    track_type,
    schema,
    candidates,
    load_mock_data,
    get_validator,
):
    for candidate in candidates:
        mock_data = load_mock_data(track_type)
        mock_data[candidate] = "aaa"
        assert not get_validator.validate(mock_data, schema)


@pytest.mark.parametrize(
    ("track_type", "schema", "candidates"),
    load_all_fields_null_not_allowed(),
)
def test_non_nullable_field_with_null(
    track_type,
    schema,
    candidates,
    load_mock_data,
    get_validator,
):
    for candidate in candidates:
        mock_data = load_mock_data(track_type)
        mock_data[candidate] = None
        assert not get_validator.validate(mock_data, schema)


@pytest.mark.parametrize(
    ("track_type", "schema", "candidates"),
    load_all_fields_empty_not_allowed(),
)
def test_non_empty_field_with_empty_str(
    track_type,
    schema,
    candidates,
    load_mock_data,
    get_validator,
):
    for candidate in candidates:
        mock_data = load_mock_data(track_type)
        mock_data[candidate] = ""
        assert not get_validator.validate(mock_data, schema)


@pytest.mark.parametrize(
    ("track_type", "schema", "candidates"),
    load_all_fields_with_specified_allowed_values(),
)
def test_allowed_values_field_with_unexpected_value(
    track_type,
    schema,
    candidates,
    load_mock_data,
    get_validator,
):
    for candidate in candidates:
        mock_data = load_mock_data(track_type)
        mock_data[candidate] = "!UNEXPECTED VALUE!"
        assert not get_validator.validate(mock_data, schema)
