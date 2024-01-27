# Released under GPLv3+ License
# Danial Behzadi <dani.behzi@ubuntu.com>, 2023-2024.
"""
Module to get values of keys from gschema
"""

import os

from gi.repository import Gio, GLib


def dconf() -> Gio.Settings:
    """
    connect to gsettings database
    """
    schema = "org.tractor"
    schemas = Gio.SettingsSchemaSource.get_default()
    if not Gio.SettingsSchemaSource.lookup(schemas, schema, False):
        raise FileNotFoundError(
            f"""
        Please compile the "tractor.gschema.xml" file.
        In GNU/Linux you can copy it to "/usr/share/glib-2.0/schemas/"
        and run "sudo glib-compile-schemas /usr/share/glib-2.0/schemas/".
        The file is located at {os.path.dirname(os.path.abspath(__file__))}.
        """
        )
    conf = Gio.Settings.new(schema)
    return conf


def get_val(key: str) -> bool | int | str:
    """
    get the value of the key
    """
    conf = dconf()
    match key:
        case "socks-port" | "http-port" | "dns-port" | "bridge-type":
            return conf.get_int(key)
        case "plugable-transport" | "exit-node":
            return conf.get_string(key)
        case "accept-connection":
            return conf.get_boolean(key)
        case _:
            raise TypeError("key is not supported")


def set_val(key: str, value: bool | int | str) -> None:
    """
    set a value for the key
    """
    conf = dconf()
    match str(type(value)):
        case "<class 'bool'>":
            conf.set_boolean(key, value)
        case "<class 'int'>":
            conf.set_int(key, value)
        case "<class 'str'>":
            conf.set_string(key, value)
        case _:
            raise TypeError("value is not supported.")


def reset(key: str) -> None:
    """
    Reset a key
    """
    dconf().reset(key)


def data_directory() -> str:
    """
    return the data directory for tractor
    """
    return GLib.get_user_config_dir() + "/tractor"
