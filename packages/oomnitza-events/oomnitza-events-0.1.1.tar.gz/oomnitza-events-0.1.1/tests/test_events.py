import pytest

from oomnitza_events import events


@pytest.fixture()
def load_empty_subdomains():
    invalid_subdomains = ["", None, {}, [], ()]
    credentials = "foo.bar"
    enabled = True
    system_type = "foo.bar"
    return invalid_subdomains, credentials, enabled, system_type


@pytest.fixture()
def load_wrong_type_subdomains():
    invalid_subdomains = [1, True]
    credentials = "foo.bar"
    enabled = True
    system_type = "foo.bar"
    return invalid_subdomains, credentials, enabled, system_type


@pytest.fixture()
def load_invalid_enabled_values():
    subdomain = "foo"
    credentials = "bar"
    invalid_enabled_values = [1, "True", None, {}, [], ()]
    system_type = "foo.bar"
    return subdomain, credentials, invalid_enabled_values, system_type


def test_client_init_with_invalid_subdomain(
    load_empty_subdomains,
    load_wrong_type_subdomains,
):
    empty_subdomains, credentials, enabled, system_type = load_empty_subdomains
    for subdomain in empty_subdomains:
        with pytest.raises(AssertionError):
            events.Client(subdomain, credentials, enabled, system_type)

    (
        wrong_type_subdomains,
        credentials,
        enabled,
        system_type,
    ) = load_wrong_type_subdomains
    for subdomain in wrong_type_subdomains:
        with pytest.raises(TypeError):
            events.Client(subdomain, credentials, enabled, system_type)


def test_client_init_with_invalid_enabled_values(load_invalid_enabled_values):
    (
        subdomain,
        credentials,
        invalid_enabled_values,
        system_type,
    ) = load_invalid_enabled_values
    for enabled in invalid_enabled_values:
        with pytest.raises(TypeError):
            events.Client(subdomain, credentials, enabled, system_type)
