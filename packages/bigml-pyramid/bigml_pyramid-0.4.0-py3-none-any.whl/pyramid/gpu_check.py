#!/usr/bin/env python
import os


def main():
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "0"  # Everything
    import logging

    logging.getLogger("tensorflow").setLevel(logging.DEBUG)
    import tensorflow

    logging.getLogger("tensorflow").setLevel(logging.DEBUG)

    print("\nGetting physical devices...")
    devices = tensorflow.config.list_physical_devices()
    print("\nPhysical devices:")
    print(devices)

    print("\nGetting logical devices...")
    devices = tensorflow.config.list_logical_devices()
    print("\nLogical devices:")
    print(devices)


if __name__ == "__main__":
    main()
