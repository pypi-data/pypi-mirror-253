"""
Entry point of pytest-lock plugin.

Pytest will automatically load this file when the plugin is activated.
Pytest will use the function 'pytest_addoption' to add new argument CLI.
Pytest will use the fixture 'lock' to give access to the lock feature.
"""

from pathlib import Path
from typing import Optional

import pytest
from _pytest.config import Config
from pytest import FixtureRequest

from pytest_lock.cache import CacheLock
from pytest_lock.config import ArgumentCLI, LockConfig
from pytest_lock.fixture import FixtureLock
from pytest_lock.parser_file.builder import ParserFileBuilder

CACHE_LOCK_PATH = ".pytest_lock"
TESTS_PATH = "tests"
EXTENSION = ".json"


def pytest_addoption(parser: Config):
    """Add new argument CLI to pytest."""
    parser.addoption(ArgumentCLI.LOCK, action="store_true", help="Activate lock feature")  # type: ignore
    parser.addoption(ArgumentCLI.SIMULATE, action="store_true", help="Simulate lock feature")  # type: ignore
    parser.addoption(ArgumentCLI.LOCK_DATE, action="store", type=str, help="Activate lock date feature")  # type: ignore
    parser.addoption(ArgumentCLI.ONLY_SKIP, action="store_true", help="Lock only tests without lock")  # type: ignore


@pytest.fixture(scope="function")
def lock(
    pytestconfig: Config,
    request: FixtureRequest,
    tests_path: Optional[Path] = None,
    cache_path: Optional[Path] = None,
    extension: Optional[str] = None,
) -> FixtureLock:
    """
    Fixture to give access to lock feature.

    This fixture is used to give access to lock feature.
    Pytest will automatically load this fixture when the plugin is activated.

    Args:
        pytestconfig (Config): Pytest configuration.
        request (FixtureRequest): Pytest request.
        tests_path (Path, optional): Path to tests. Defaults to None.
        cache_path (Path, optional): Path to cache. Defaults to None.
        extension (str, optional): Extension of cache file. Defaults to None.

    Returns:
        FixtureLock: Lock fixture.

    """

    return _lock(
        pytestconfig=pytestconfig,
        request=request,
        tests_path=tests_path,
        cache_path=cache_path,
        extension=extension,
    )


def _lock(
    pytestconfig: Config,
    request: FixtureRequest,
    tests_path: Optional[Path] = None,
    cache_path: Optional[Path] = None,
    extension: Optional[str] = None,
) -> FixtureLock:
    """
    Fixture function accessible without use like pytest way.

    Notes:
        This way of creating the fixture is necessary, because in the tests we need to supply
        the pytesterconfig and request of the unit test and not that of the sub-test
        that launches pytest-lock. Without this manipulation, the plugin don't work
        if we want to test it. In folder tests we use _lock instead of lock, who
        can be call without use pytest way who preload lock function.

    Args:
        pytestconfig (Config): Pytest configuration.
        request (FixtureRequest): Pytest request.
        tests_path (Path, optional): Path to tests. Defaults to None.
        cache_path (Path, optional): Path to cache. Defaults to None.
        extension (str, optional): Extension of cache file. Defaults to None.

    Returns:
        FixtureLock: Lock fixture.

    """
    root_path = pytestconfig.rootpath
    # Use default values if not given
    tests_path = tests_path or root_path / TESTS_PATH
    cache_path = cache_path or root_path / CACHE_LOCK_PATH
    extension = extension or EXTENSION

    # Create configuration for lock fixture
    config = LockConfig.from_pytest_run(
        pytestconfig=pytestconfig,
        request=request,
        tests_path=tests_path,
        cache_path=cache_path,
        extension=extension,
    )

    # Create cache system
    parser_file_builder = ParserFileBuilder()
    parser_file = parser_file_builder.build(EXTENSION)
    cache_system = CacheLock(config, parser_file)

    # Create lock fixture with configuration and cache system
    lock_fixture = FixtureLock(config, cache_system)

    return lock_fixture
