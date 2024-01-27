# Released under GPLv3+ License
# Danial Behzadi<dani.behzi@ubuntu.com>, 2020-2024

"""
module for setting and removing proxy
"""

from gi.repository import Gio
from . import checks
from . import control


def proxy_set(verbose: bool = False) -> None:
    """
    setup proxy
    """
    if not checks.running():
        print("Tractor is not running!")
    elif checks.proxy_set():
        checks.verbose_print("Proxy is already set", verbose)
    else:
        proxy = Gio.Settings.new("org.gnome.system.proxy")
        socks = Gio.Settings.new("org.gnome.system.proxy.socks")
        my_ip, socks_port = control.get_listener("socks")
        ignored = [
            "localhost",
            "127.0.0.0/8",
            "::1",
            "192.168.0.0/16",
            "10.0.0.0/8",
            "172.16.0.0/12",
        ]
        socks.set_string("host", my_ip)
        socks.set_int("port", socks_port)
        proxy.set_string("mode", "manual")
        proxy.set_strv("ignore-hosts", ignored)
        checks.verbose_print("Proxy set", verbose)


def proxy_unset(verbose: bool = False) -> None:
    """
    unset proxy
    """
    if checks.proxy_set():
        proxy = Gio.Settings.new("org.gnome.system.proxy")
        proxy.set_string("mode", "none")
        checks.verbose_print("Proxy unset", verbose)
    else:
        checks.verbose_print("Proxy is not set", verbose)
