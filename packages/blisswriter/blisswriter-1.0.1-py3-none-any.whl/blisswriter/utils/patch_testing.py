from typing import Tuple, Sequence, Optional


def popen_args(patches: Optional[Sequence[str]]) -> Tuple[str]:
    if patches:
        return tuple(f"--patch={name}" for name in patches)
    return tuple()


def add_test_cli_args(parser) -> None:
    parser.add_argument(
        "--patch",
        action="append",
        default=[],
        help="Patches to be applied for unit testing",
    )


def apply_test_cli_args(args) -> None:
    for name in args.patch:
        if name == "slowdisk":
            _slow_disc_patch()
        else:
            raise ValueError(name)


def _slow_disc_patch():
    import os
    from os import statvfs as statvfs_orig
    from gevent.monkey import get_original

    def statvfs(*args, **kw):
        sleep = get_original("time", "sleep")
        sleep(10)  # longer than the default tango client timeout (3 seconds)
        return statvfs_orig(args, **kw)

    os.statvfs = statvfs
