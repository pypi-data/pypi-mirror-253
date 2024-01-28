class ArgumentCLI:
    """
    CLI argument of pytest-lock fixture.

    Attributes:
        LOCK: Argument to lock a function and save the result in a cache file
        SIMULATE: Argument to simulate a locking and don't write in a cache file
        LOCK_DATE: Argument to lock a function with expiry date
        ONLY_SKIP: Argument to target only test without lock
    """

    LOCK = "--lock"
    SIMULATE = "--simulate"
    LOCK_DATE = "--lock-date"
    ONLY_SKIP = "--only-skip"
