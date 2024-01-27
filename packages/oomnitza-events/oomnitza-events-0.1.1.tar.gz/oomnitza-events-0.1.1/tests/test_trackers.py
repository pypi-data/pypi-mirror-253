import pytest

from oomnitza_events.trackers import (
    LoginTracker,
    ObjectActionTracker,
    UserIdentityTracker,
    WorkflowRunTracker,
)


@pytest.fixture()
def load_ini_enabled_data():
    user_id = "foo"
    credentials = "bar"
    enabled = True
    system_type = "foo.bar"
    return user_id, credentials, enabled, system_type


@pytest.fixture()
def load_ini_disabled_data():
    user_id = "foo"
    credentials = "bar"
    enabled = False
    system_type = "foo.bar"
    return user_id, credentials, enabled, system_type


@pytest.fixture()
def load_all_trackers():
    return LoginTracker, WorkflowRunTracker, ObjectActionTracker, UserIdentityTracker


def test_tracker_no_duplicates(load_ini_enabled_data, load_all_trackers):
    user_id, credentials, enabled, system_type = load_ini_enabled_data
    for tracker_class in load_all_trackers:
        init_tracker = tracker_class(user_id, credentials, system_type)
        recreated_tracker = tracker_class(user_id, credentials, system_type)
        assert id(init_tracker) == id(recreated_tracker)
