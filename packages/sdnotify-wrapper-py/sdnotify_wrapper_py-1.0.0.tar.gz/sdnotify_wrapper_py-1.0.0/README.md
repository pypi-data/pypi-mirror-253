# sdnotify-wrapper-py

This project provides a command line tool `sdnotify-wrapper`, that can be used
to send a readiness notification from a service to systemd, by simply writing a
newline to stdout. This can be an alternative to [`sd_notify(3)`] or
[`systemd-notify(1)`], if you don't want your service to depend on systemd.

[`sd_notify(3)`]: https://www.freedesktop.org/software/systemd/man/latest/sd_notify.html
[`systemd-notify(1)`]: https://www.freedesktop.org/software/systemd/man/latest/systemd-notify.html

## Installation

There's a package published on PyPi, so it can be installed either with `pip`,
or globally with `pipx`:

```
$ sudo PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx install sdnotify-wrapper-py
```

## Usage

In your service write one line to stdout whenever the service is ready (make
sure to write logs to stderr instead). For example in Python (characters other
than a newline are ignored):

```python
print("ready", flush=True)
```

Or in C:

```c
write(1, "\n", 1)
```

Then create a systemd service file with `Type=notify`, e.g. if your service
would be started with `my-service --foo bar`:

```ini
[Unit]
Description=My Service

[Service]
Type=notify
NotifyAccess=all
ExecStart=/usr/local/bin/sdnotify-wrapper my-service --foo bar

[Install]
WantedBy=multi-user.target
```

`sdnotify-wrapper` will then connect to the stdout of your service, notify
systemd when it reads a newline and exit.

## Why Python?

`sdnotify-wrapper` is a tool originally written by Laurent Bercot:
[`sdnotify-wrapper.c`][1]. Unfortunately this tool is not packaged for any of
the major Linux distributions, so it's not a great user experience if your
service requires this mechanism.

I chose to reimplement this tool in Python mainly, because it's easier to
install it with a Python package manager. In doing this, I hope this readiness
notification mechanism will be adopted by more projects and the original tool
will be packaged by more distributions.

[1]: https://www.skarnet.org/software/misc/sdnotify-wrapper.c
