import pytest

from oomnitza_events.connectors import Redshift, Segment
from oomnitza_events.errors import InvalidCredentialsError, InvalidDatabaseInfoError


@pytest.fixture()
def load_empty_credentials():
    return ""


@pytest.fixture()
def load_empty_db_schema_name():
    return ""


@pytest.fixture()
def load_wrong_type_db_schema_name():
    return False


@pytest.fixture()
def load_valid_db_schema_name():
    return "foo"


@pytest.fixture()
def load_none_db_config():
    return None


@pytest.fixture()
def load_wrong_type_db_config():
    return [1, 2, 3]


@pytest.fixture()
def load_missing_info_db_config():
    return {"host": "foo.bar", "port": 1234, "user": "foo", "password": "bar"}


@pytest.fixture()
def load_valid_db_config():
    return {
        "host": "foo.bar",
        "port": 1234,
        "user": "foo",
        "password": "bar",
        "database": "db",
    }


@pytest.fixture()
def load_invalid_types_credentials():
    return [1, True, None, {}, [], ()]


def test_segment_connector_init_with_empty_credentials(load_empty_credentials):
    with pytest.raises(InvalidCredentialsError):
        Segment(load_empty_credentials)


def test_segment_connector_init_with_invalid_credentials_types(
    load_invalid_types_credentials,
):
    for credentials in load_invalid_types_credentials:
        with pytest.raises(InvalidCredentialsError):
            Segment(credentials)


def test_redshift_connector_init_with_empty_db_schema_name(
    load_empty_db_schema_name,
    load_valid_db_config,
):
    with pytest.raises(InvalidDatabaseInfoError):
        Redshift(load_empty_db_schema_name, load_valid_db_config)


def test_redshift_connector_init_with_wrong_type_db_schema_name(
    load_wrong_type_db_schema_name,
    load_valid_db_config,
):
    with pytest.raises(InvalidDatabaseInfoError):
        Redshift(load_wrong_type_db_schema_name, load_valid_db_config)


def test_redshift_connector_init_with_none_db_config(
    load_valid_db_schema_name,
    load_none_db_config,
):
    with pytest.raises(InvalidDatabaseInfoError):
        Redshift(load_valid_db_schema_name, load_none_db_config)


def test_redshift_connector_init_with_wrong_type_db_config(
    load_valid_db_schema_name,
    load_wrong_type_db_config,
):
    with pytest.raises(InvalidDatabaseInfoError):
        Redshift(load_valid_db_schema_name, load_wrong_type_db_config)


def test_redshift_connector_init_with_missing_info_db_config(
    load_valid_db_schema_name,
    load_missing_info_db_config,
):
    with pytest.raises(InvalidDatabaseInfoError):
        Redshift(load_valid_db_schema_name, load_missing_info_db_config)
