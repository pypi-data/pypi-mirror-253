import logging
import sys
import time
from abc import ABC
from datetime import datetime
from typing import Any, Callable, Optional, Tuple

import pytest

from pytest_lock.fixtures.base import FixtureBase
from pytest_lock.models.cache.lock import Lock

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override


def is_valid_date(date_string: str, date_format: str = "%Y/%m/%d") -> bool:
    """
    Check if date string respect format

    Parameters:
        date_string (str): Date string to check
        date_format (str): Date format with strptime format

    Examples:
        >>> is_valid_date("2021/01/01", "%Y/%m/%d")
        True
        >>> is_valid_date("2021-01-01", "%Y/%m/%d")
        False
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


class MixinLock(FixtureBase, ABC):
    """Mixin for lock.lock fixture."""

    @override
    def lock(self, function: Callable, arguments: Tuple[Any, ...]) -> None:
        # Hides the execution of the error; the error will be visible in the test file.
        __tracebackhide__ = True

        # Create new lock and get old lock
        new_lock = Lock.from_function_and_arguments(function, arguments)
        old_lock = self.cache_system.read_lock(new_lock)

        if self.config.is_lock:
            self._update_lock(new_lock, old_lock)
        else:
            self._check_lock(new_lock, old_lock)

    def _update_lock(self, new_lock: Lock, old_lock: Optional[Lock]) -> None:
        """
        Update lock in cache file (append or update)

        Args:
            new_lock: Lock to write in cache file
            old_lock: Lock to update in cache file
        """
        __tracebackhide__ = True

        if old_lock is None:
            logging.info(f"No lock found, create a new lock with result {new_lock.result}")
        else:
            logging.info(f"Lock found, modified result {old_lock.result} with {new_lock.result}")

        # If 'lock-date' is activated, add the date to the lock
        if self.config.is_lock_date:
            # If lock_date don't respect format, raise error
            if not is_valid_date(self.config.is_lock_date):
                raise ValueError(f"Lock date '{self.config.is_lock_date}' don't respect format '{self.config.date_format}'")
            new_lock.expiration_date = self.config.is_lock_date

        conditions = (
            old_lock is not None and self.config.only_skip,
            # If old lock exist and 'only-skip' is activated, don't write
        )

        if not any(conditions):
            if not self.config.is_simulate:
                self.cache_system.write_lock(new_lock)
                logging.info(f"Write in the cache file with result {new_lock.result}")
            else:
                logging.info(f"[Simulate] Write in the cache file with result {new_lock.result}")

            pytest.skip(f"Write in the cache file with result {new_lock.result}")

    def _check_lock(self, new_lock: Lock, old_lock: Optional[Lock]) -> None:
        """
        Check if lock is valid with old lock

        Args:
            new_lock: new lock to check with old lock
            old_lock: old lock create with the same signature at last locking
        """
        __tracebackhide__ = True

        if old_lock is None:
            # Add to history allow targeting with '--only-skip' for next '--lock' command
            pytest.fail("No lock found, please run the lock of this test")

        assert old_lock.result == new_lock.result, f"The test result does not match the last lock ({old_lock.result} != {new_lock.result})"
        assert old_lock.result_type == new_lock.result_type, f"The test type does not match the last lock ({old_lock.result} != {new_lock.result})"

        # If date was indicate by 'lock-date', check if always valid
        if old_lock.expiration_date is not None:
            today_str = time.strftime(self.config.date_format, time.localtime())

            today = time.strptime(today_str, self.config.date_format)
            old_date = time.strptime(old_lock.expiration_date, self.config.date_format)

            logging.info(f"Lock found, result {old_lock.result}, expiration date on '{old_date}'")
            assert old_date >= today, f"The lock is invalid due to the expiration date, please restart its lock ({old_date} > {today})"
