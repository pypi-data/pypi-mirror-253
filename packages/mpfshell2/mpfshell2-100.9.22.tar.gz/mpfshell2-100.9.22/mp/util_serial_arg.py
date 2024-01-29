"""
This method is intended to be used in commands like:
    minicom --baudrate 115200 --device /dev/ttyUSB0
Instead of hardcoding '/dev/ttyUSB0' the vendor/product id may be used:
    minicom --baudrate 115200 --device `serial_arg --vid=2E8A`

Find a usb connected uart according the command line paraments.

Print the device name to stdout.

Return an error code when the uart was not found.
"""
import sys
import argparse

from .util_serial import (
    find_serial_port,
    print_ports,
    SerialPortNotFoundException,
    ArgumentWrapperFind,
)


def main():
    parser = argparse.ArgumentParser()
    ArgumentWrapperFind.add_arguments(parser)
    args = parser.parse_args()

    try:
        awf =ArgumentWrapperFind(args)
        device = find_serial_port(awf.args)
        print(device)
    except SerialPortNotFoundException:
        print(f"No serial port found for {args}", file=sys.stderr)
        print_ports(file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
