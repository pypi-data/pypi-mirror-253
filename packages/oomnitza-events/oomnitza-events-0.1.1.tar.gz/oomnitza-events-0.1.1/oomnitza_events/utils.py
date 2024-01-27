# -*- coding: utf-8 -*-
"""Utility module

This is the place for utilities which will be used among the project.
"""


class Validator:
    @classmethod
    def verify_subdomain(cls, subdomain: str) -> None:
        if not subdomain:
            err_msg = "'subdomain' is required."
            raise AssertionError(err_msg)

        if not isinstance(subdomain, str):
            err_msg = "'subdomain' has to be a string."  # type: ignore [unreachable]
            raise TypeError(err_msg)

    @classmethod
    def verify_system_type(cls, system_type: str) -> None:
        if not system_type:
            err_msg = "'system_type' is required."
            raise AssertionError(err_msg)

        if not isinstance(system_type, str):
            err_msg = "'system_type' has to be a string."  # type: ignore[unreachable]
            raise TypeError(err_msg)

    @classmethod
    def verify_enabled(cls, enabled: bool) -> None:
        if not isinstance(enabled, bool):
            err_msg = "'enabled' has to be a bool value."  # type: ignore[unreachable]
            raise TypeError(err_msg)
