#!/usr/bin/env python3

import getopt
import os
import select
import struct
import sys
import time
import typing


def usage():
    print(
        "usage: sdnotify-wrapper [ -d fd ] [ -f ] [ -t timeout ] [ -k ] prog...",
        file=sys.stderr,
    )


def main():
    args = Arguments.parse()

    if "NOTIFY_SOCKET" not in os.environ:
        os.execvp(args.argv[0], args.argv)

    main_pid = os.getpid()
    read_pipe, write_pipe = os.pipe()

    pid = os.fork() if args.fork_once else double_fork()
    if is_forked_child(pid):
        os.close(write_pipe)
        return run_child(read_pipe, args.timeout_ms, main_pid)

    os.close(read_pipe)

    if write_pipe == args.fd:
        # by default pipes aren't inheritable
        os.set_inheritable(write_pipe, True)
    else:
        os.dup2(write_pipe, args.fd)
        os.close(write_pipe)

    if not args.keep:
        del os.environ["NOTIFY_SOCKET"]

    return os.execvp(args.argv[0], args.argv)


class Arguments(typing.NamedTuple):
    argv: typing.List[str]
    fd: int = 1  # default is stdout
    fork_once: bool = False
    timeout_ms: typing.Optional[int] = None
    keep: bool = False

    @classmethod
    def parse(cls):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "d:ft:k")
        except getopt.GetoptError as err:
            print(err, file=sys.stderr)
            usage()
            sys.exit(2)

        init_args = {}
        for opt, arg in opts:
            if opt == "-d":
                init_args["fd"] = int(arg)
            elif opt == "-f":
                init_args["fork_once"] = True
            elif opt == "-t":
                init_args["timeout_ms"] = int(arg)
            elif opt == "-k":
                init_args["keep"] = True
            else:
                assert False, "unhandled option"

        if not args:
            usage()
            sys.exit(2)

        return cls(argv=args, **init_args)


# pylint: disable=R1732
# - consider-using-with: can't use a context manager when using fork()
def double_fork():
    read_pipe, write_pipe = os.pipe()
    read_pipe = open(read_pipe, "rb")
    write_pipe = open(write_pipe, "wb")

    pid = os.fork()
    if is_forked_child(pid):
        read_pipe.close()
        pid = os.fork()
        if is_forked_child(pid):
            # grandchild
            write_pipe.close()
            return 0

        msg = struct.pack("!Q", pid)
        write_pipe.write(msg)
        write_pipe.flush()
        os._exit(0)

    write_pipe.close()
    msg = read_pipe.read(8)
    read_pipe.close()
    os.waitpid(pid, 0)  # wait for child #1 to exit
    grandchild = struct.unpack("!Q", msg)[0]
    return grandchild


def is_forked_child(pid):
    return pid == 0


def run_child(read_pipe, timeout_ms, main_pid):
    deadline = time.time() + (timeout_ms / 1000) if timeout_ms else None
    data = b""

    while b"\n" not in data:
        if deadline:
            timeout = max(deadline - time.time(), 0)
            readable = select.select([read_pipe], [], [], timeout)[0]
            if not readable:
                return 99

        data = os.read(read_pipe, 4096)
        if not data:
            return 1
    return notify_systemd(main_pid)


def notify_systemd(main_pid):
    argv = ["systemd-notify", "--ready", f"--pid={main_pid}"]
    os.execvp(argv[0], argv)


if __name__ == "__main__":
    sys.exit(main())
