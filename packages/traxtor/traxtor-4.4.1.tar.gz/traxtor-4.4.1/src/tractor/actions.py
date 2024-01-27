# Released under GPLv3+ License
# Danial Behzadi <dani.behzi@ubuntu.com>, 2020-2024.

"""
real actions of tractor
"""

import os
import signal

from stem.process import launch_tor
from stem.util import term

from . import checks
from . import control
from . import db
from . import tractorrc


def ___print_bootstrap_lines(line) -> None:
    """
    prints bootstrap line in standard output
    """
    if "Bootstrapped " in line:
        print(term.format(line, term.Color.BLUE), flush=True)


def ___print_all_lines(line) -> None:
    """
    prints bootstrap line in standard output
    """
    print(term.format(line, term.Color.BLUE), flush=True)


def ___finish_notification(verbose: bool) -> None:
    """
    Notify user after start finished
    """
    if not checks.running():
        print(
            term.format(
                "Tractor could not connect.\n"
                "Please check your connection and try again.",
                term.Attr.BOLD,
                term.Color.RED,
            )
        )
    else:
        checks.verbose_print(
            term.format(
                "Tractor is conneted.",
                term.Attr.BOLD,
                term.Color.GREEN,
            ),
            verbose,
        )


def __launch(torrc: str, tmpdir: str, verbose: bool) -> None:
    """
    Actually launch tor
    """
    msg_handler = checks.verbose_return(
        ___print_bootstrap_lines, ___print_all_lines, verbose
    )
    try:
        tractor_process = launch_tor(
            torrc_path=torrc,
            init_msg_handler=msg_handler,
            timeout=120,
        )
        db.set_val("pid", tractor_process.pid)
    except OSError as error:
        print(term.format(f"{error}\n", term.Color.RED))
    except KeyboardInterrupt:
        pass
    else:
        ___finish_notification(verbose)
    finally:
        os.remove(torrc)
        os.rmdir(tmpdir)


def _start_launch(verbose: bool) -> None:
    """
    Start launching tor
    """
    data_dir = db.data_directory()
    os.makedirs(data_dir, mode=0o700, exist_ok=True)
    try:
        tmpdir, torrc = tractorrc.create()
    except ValueError:
        print(
            term.format(
                "Error Creating torrc. Check your configurations\n",
                term.Attr.BOLD,
                term.Color.RED,
            )
        )
    except EnvironmentError:
        print(
            term.format(
                "Error Creating torrc. No relevant bridge found\n",
                term.Attr.BOLD,
                term.Color.RED,
            )
        )
    else:
        checks.verbose_print(
            term.format(
                "Starting Tractor:\n", term.Attr.BOLD, term.Color.YELLOW
            ),
            verbose,
        )
        __launch(torrc, tmpdir, verbose)


def start(verbose: bool = False) -> None:
    """
    starts onion routing
    """
    if not checks.running():
        _start_launch(verbose)
    else:
        print(
            term.format(
                "Tractor is already started", term.Attr.BOLD, term.Color.GREEN
            )
        )


def stop(verbose: bool = False) -> None:
    """
    stops onion routing
    """
    if checks.running():
        control.send_signal("term")
        db.reset("pid")
        checks.verbose_print(
            term.format("Tractor stopped", term.Attr.BOLD, term.Color.YELLOW),
            verbose,
        )
    else:
        checks.verbose_print(
            term.format(
                "Tractor seems to be stopped.",
                term.Attr.BOLD,
                term.Color.YELLOW,
            ),
            verbose,
        )


def restart(verbose: bool = False) -> None:
    """
    stop, then start
    """
    stop(verbose)
    start(verbose)


def new_id(verbose: bool = False) -> None:
    """
    gives user a new identity
    """
    if not checks.running():
        print(
            term.format(
                "Tractor is stopped.", term.Attr.BOLD, term.Color.YELLOW
            )
        )
    else:
        control.send_signal("newnym")
        checks.verbose_print(
            term.format(
                "You now have a new ID.", term.Attr.BOLD, term.Color.GREEN
            ),
            verbose,
        )


def kill_tor(verbose: bool = False) -> None:
    """
    kill tor process
    """
    pid = control.get_pid()
    if pid:
        os.killpg(os.getpgid(control.get_pid()), signal.SIGTERM)
        db.reset("pid")
        checks.verbose_print(
            term.format(
                "Tor process has been successfully killed!",
                term.Attr.BOLD,
                term.Color.GREEN,
            ),
            verbose,
        )
    else:
        checks.verbose_print(
            term.format(
                "Couldn't find any process to kill!",
                term.Attr.BOLD,
                term.Color.RED,
            ),
            verbose,
        )
