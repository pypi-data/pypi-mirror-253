# Released under GPLv3+ License
# Danial Behzadi <dani.behzi@ubuntu.com>, 2020-2024.

"""
this module creates tractorrc file
"""

import os
import tempfile

from . import bridges
from . import db


def _get_port_lines() -> str:
    """
    Get torrc lines for different ports
    """
    if db.get_val("accept-connection"):
        my_ip = "0.0.0.0"
        socks_line = f"SocksPort {my_ip}:{str(db.get_val('socks-port'))}\n"
        socks_line += "SocksPolicy accept *\n"
    else:
        my_ip = "127.0.0.1"
        socks_line = f"SocksPort {my_ip}:{str(db.get_val('socks-port'))}\n"
    http_line = f"HTTPTunnelPort {my_ip}:{str(db.get_val('http-port'))}\n"
    dns_line = f"DNSPort {my_ip}:{str(db.get_val('dns-port'))}\n"
    dns_line += "AutomapHostsOnResolve 1\n"
    dns_line += "AutomapHostsSuffixes .exit,.onion\n"
    return f"{socks_line}{http_line}{dns_line}"


def _get_path_lines() -> str:
    """
    Get torrc lines for different pathes
    """
    data_dir = db.data_directory()
    path_line = f"DataDirectory {data_dir}\n"
    path_line += f"ControlSocket {data_dir}/control.sock\n"
    return path_line


def _get_exit_lines() -> str:
    """
    Get torrc lines for exit nodes
    """
    exit_node = db.get_val("exit-node")
    if exit_node != "ww":
        return f"ExitNodes {'{'}{exit_node}{'}'}\n" "StrictNodes 1\n"
    return ""


def __fill_bridge_lines(bridge_type: str, my_bridges: str) -> str:
    """
    Fill the bridge-related lines for torrc
    """
    bridge_line = "UseBridges 1\n"
    match bridge_type:
        case 1:  # vanilla bridge
            pass
        case 2:  # obfs bridge
            path = db.get_val('plugable-transport')
            bridge_line += f"ClientTransportPlugin obfs4 exec {path}\n"
        case _:
            raise ValueError("Bridge type is not supported")
    for line in my_bridges:
        bridge_line += f"Bridge {line}\n"
    return bridge_line


def _get_bridge_lines() -> str:
    """
    Get torrc lines for bridges
    """
    bridge_type = db.get_val("bridge-type")
    if bridge_type != 0:
        with open(bridges.get_file(), encoding="utf-8") as file:
            my_bridges = file.read()
        my_bridges = bridges.relevant_lines(my_bridges, bridge_type)
        if not my_bridges:
            raise EnvironmentError("No relevant bridges given")
        bridge_lines = __fill_bridge_lines(bridge_type, my_bridges)
        return bridge_lines
    return ""


def create() -> (str, str):
    """
    main function of the module
    """
    port_lines = _get_port_lines()
    path_lines = _get_path_lines()
    exit_lines = _get_exit_lines()
    bridge_lines = _get_bridge_lines()
    tmpdir = tempfile.mkdtemp()
    path = os.path.join(tmpdir, "tractorrc")
    with open(path, "w", encoding="utf-8") as file:
        file.write(port_lines)
        file.write(path_lines)
        if exit_lines:
            file.write(exit_lines)
        if bridge_lines:
            file.write(bridge_lines)
    return tmpdir, path
