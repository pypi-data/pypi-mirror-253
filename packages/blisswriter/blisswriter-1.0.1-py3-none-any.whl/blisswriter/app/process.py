import sys
from blisswriter.parameters import all_cli_saveoptions
from blisswriter.subscribers.session_subscriber import NexusSessionSubscriber
from blisswriter.utils import logging_utils
from blisswriter.utils import patch_testing
from .utils import config_root_logger


def main(argv=None):
    import argparse

    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(
        description="Start python a process for saving Bliss data in HDF5"
    )
    parser.add_argument("session_name", type=str, help="Session name")
    cli_saveoptions = all_cli_saveoptions()
    for attr, okwargs in cli_saveoptions.items():
        parser.add_argument("--" + attr, **okwargs)
    logging_utils.add_cli_args(parser)
    patch_testing.add_test_cli_args(parser)

    # Parse CLI arguments
    args = parser.parse_args(argv[1:])
    config_root_logger(args)
    patch_testing.apply_test_cli_args(args)
    kwargs = {}
    cli_saveoptions = all_cli_saveoptions(configurable=args.configurable)
    for attr, okwargs in cli_saveoptions.items():
        option = okwargs["dest"]
        try:
            kwargs[option] = getattr(args, option)
        except AttributeError:
            continue

    # Launch the session writer
    subscriber = NexusSessionSubscriber(
        args.session_name, writer_name="external", **kwargs
    )
    subscriber.start()
    subscriber.join()


if __name__ == "__main__":
    sys.exit(main())
