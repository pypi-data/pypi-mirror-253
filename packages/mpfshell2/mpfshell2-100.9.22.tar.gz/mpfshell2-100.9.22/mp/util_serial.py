"""
Find a usb connected uart.
Open and dump input to stdout.
Follow when the uart dissapears and appears again. This may happen when the usb device powercycles.
Optionally append the output to a file.
Optionally prepend a timestamp in front of every line.
"""
import argparse
import sys
import time
from typing import List
import dataclasses

import serial
from serial.tools import list_ports


class SerialPortNotFoundException(Exception):
    pass


def serial_ports_ordered() -> List[serial.Serial]:
    """
    return ordered list of comports. Ignore the ones which do not have vid/pid defined.
    """
    ports = list(list_ports.comports())
    ports.sort(key=lambda p: p.device)

    return [p for p in ports if p.vid and p.pid]


def print_ports(file):
    for port in serial_ports_ordered():
        print(port.device, file=file)
        # print(f"  device_path   {port.device_path}",file=file)
        # print(f"  location      {port.location}",file=file)
        # print(f"  description    {port.description}",file=file)
        print(f"  manufacturer   {port.manufacturer}", file=file)
        print(f"  product        {port.product}", file=file)
        print(f"  interface      {port.interface}", file=file)
        print(
            f"  --vid={port.vid:04X} --pid={port.pid:04X} --serial={port.serial_number}",
            file=file,
        )


@dataclasses.dataclass(frozen=True)
class FindArguments:
    vid: int = None
    pid: int = None
    serial: str = None
    n: int = 1
    """
    0 is the first occurence
    1 is the second occurence
    """


class ArgumentWrapperFind:
    def __init__(self, args: argparse.Namespace):
        vid = None
        pid = None
        if args.vid is not None:
            vid = int(args.vid, base=16)
        if args.pid is not None:
            pid = int(args.pid, base=16)

        self.args = FindArguments(vid=vid, pid=pid, serial=args.serial, n=args.n)

    @classmethod
    def add_arguments(cls, parser: argparse.ArgumentParser):
        parser.add_argument("--vid", default=None, help="Vender ID")
        parser.add_argument("--pid", default=None, help="Product Id")
        parser.add_argument("--serial", default=None, help="Serial number")
        parser.add_argument("--n", default=0, help="select n' occurence")


def find_serial_port(args: FindArguments) -> str:
    n = 0
    for port in serial_ports_ordered():
        if args.vid is not None:
            if args.vid != port.vid:
                continue
        if args.pid is not None:
            if args.pid != port.pid:
                continue
        if args.serial is not None:
            if args.serial != port.serial_number:
                continue
        if n < args.n:
            n += 1
            continue
        return port.device

    raise SerialPortNotFoundException(f"No serial interface found for {args}")


class ArgumentWrapperOpen:
    CHOICES_PARITY = {
        "none": serial.PARITY_NONE,
        "even": serial.PARITY_EVEN,
        "odd": serial.PARITY_ODD,
        "mark": serial.PARITY_MARK,
        "space": serial.PARITY_SPACE,
    }
    CHOICES_STOPBITS = {
        "1": serial.STOPBITS_ONE,
        "1.5": serial.STOPBITS_ONE_POINT_FIVE,
        "2": serial.STOPBITS_TWO,
    }
    CHOICES_BYTESIZE = {
        "5": serial.FIVEBITS,
        "6": serial.SIXBITS,
        "7": serial.SEVENBITS,
        "8": serial.EIGHTBITS,
    }

    def __init__(self, args: argparse.Namespace):
        self.baudrate = args.baudrate
        self.parity = self.CHOICES_PARITY[args.parity]
        self.stopbits = self.CHOICES_STOPBITS[args.stopbits]
        self.bytesize = self.CHOICES_BYTESIZE[args.bytesize]

    @classmethod
    def add_arguments(cls, parser: argparse.ArgumentParser):
        parser.add_argument(
            "--baudrate", default=9600, type=int, help="Baudrate: 9600, 19200, 115200"
        )
        parser.add_argument(
            "--parity",
            default="none",
            choices=cls.CHOICES_PARITY,
            help=f"One of {cls.CHOICES_PARITY}",
        )
        parser.add_argument(
            "--stopbits",
            choices=cls.CHOICES_STOPBITS,
            default="1",
            help=f"One of {cls.CHOICES_STOPBITS}",
        )
        parser.add_argument(
            "--bytesize",
            choices=cls.CHOICES_BYTESIZE,
            default="8",
            help=f"One of {cls.CHOICES_BYTESIZE}",
        )


class ArgumentWrapperLogfile:
    def __init__(self, args: argparse.Namespace):
        self.args = args

    @classmethod
    def add_arguments(cls, parser: argparse.ArgumentParser):
        parser.add_argument("-v", "--verbose", action="store_true")
        parser.add_argument(
            "--timestamp_format",
            default="%Y_%m_%d-%H_%M_%S >>> ",
            help="Formatting according to time.strftime",
        )
        parser.add_argument(
            "--logfile_format",
            default="dump_uart_%Y_%m_%d-%H_%M_%S.txt",
            help="Formatting according to time.strftime",
        )


class DumpSerialPort:
    def __init__(self, args: argparse.Namespace):
        self._args_find = ArgumentWrapperFind(args)
        self._args_open = ArgumentWrapperOpen(args)
        self._args_logfile = ArgumentWrapperLogfile(args)

    def dump_serial_port(self) -> None:
        try:
            find_serial_port(self._args_find.args)
        except SerialPortNotFoundException:
            pass
        while True:
            logfile = None
            try:
                port = find_serial_port(self._args_find.args)
            except SerialPortNotFoundException:
                time.sleep(0.5)
                print(".", end="")
                continue

            try:
                _serial = serial.Serial(
                    port,
                    baudrate=self._args_open.baudrate,
                    parity=self._args_open.parity,
                    stopbits=self._args_open.stopbits,
                    bytesize=self._args_open.bytesize,
                    timeout=0,
                )
                filename = ""
                if self._args_logfile.args.logfile_format:
                    filename = time.strftime(
                        self._args_logfile.args.logfile_format,
                        time.localtime(),
                    )
                    logfile = open(filename, "a", encoding="utf-8")
                msg = f"Connected to {port}"
                if filename:
                    msg += f", {filename}"
                print(msg)
                if logfile:
                    print(msg, file=logfile)
            except serial.SerialException:
                time.sleep(0.5)
                continue

            try:
                while True:
                    text = _serial.readline()
                    if len(text) == 0:
                        time.sleep(0.1)
                        continue
                    text = text.decode("ascii", errors="replace")
                    text = text.rstrip()
                    timestamp = ""
                    if self._args_logfile.args.timestamp_format:
                        timestamp = time.strftime(
                            self._args_logfile.args.timestamp_format,
                            time.localtime(),
                        )
                    line = f"{timestamp}{text}"
                    print(line)
                    if logfile:
                        print(line, file=logfile)
                        logfile.flush()
            except serial.SerialException:
                print("Disconnect! ", end="")
                if logfile:
                    print("Disconnect", file=logfile)
                    logfile.close()
                time.sleep(0.5)


def main():
    parser = argparse.ArgumentParser()
    ArgumentWrapperFind.add_arguments(parser)
    ArgumentWrapperOpen.add_arguments(parser)
    ArgumentWrapperLogfile.add_arguments(parser)

    args = parser.parse_args()
    dsp = DumpSerialPort(args)
    dsp.dump_serial_port()


if __name__ == "__main__":
    main()
