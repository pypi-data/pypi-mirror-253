"""
The MIT License (MIT), Copyright (c) 2024 Hans Märki

List all serial uarts
"""
import sys
from .util_serial import print_ports


def main():
    print_ports(file=sys.stdout)


if __name__ == "__main__":
    main()
