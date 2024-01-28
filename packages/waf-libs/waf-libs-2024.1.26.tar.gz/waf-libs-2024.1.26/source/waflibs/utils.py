"""
general utils
"""

import ipaddress
import json
import logging
import os
import pathlib
import shutil
import subprocess
import sys
import urllib

import dns.resolver

PROGRAM_NAME = os.path.basename(sys.argv[0])

PERSONAL_DOMAINS = [
    "fawong.com",
    "hlx.tw",
    "waf.hk",
    "xilef.org",
    "xn--i8s3q.xn--j6w193g",
]
DEV_DOMAINS = [
    "gyx.io",
    "waf.sexy",
]
COMMUNITY_DOMAINS = [
    "fastandfungible.com",
    "kirinas.com",
    "seris-choice.com",
    "xn--ij2bx6jt8qgte.com",
    "xn--lckwg.net",
]
PUBLIC_DOMAINS = [
    "fantasticrealty.uk",
    "faw.gg",
    "orientelectronic.net",
    "waf.gg",
]
PROJECT_DOMAINS = [
    "mymovielist.org",
    "mytvlist.org",
]
ADMIN_DOMAINS = [
    "aatf.us",
]
ALL_DOMAINS = (
    PERSONAL_DOMAINS
    + DEV_DOMAINS
    + COMMUNITY_DOMAINS
    + PUBLIC_DOMAINS
    + ADMIN_DOMAINS
    + PROJECT_DOMAINS
)

IP_CIDRS = []

logger = logging.getLogger(PROGRAM_NAME)
logger.debug(f"program name: {PROGRAM_NAME}")
logger.debug(f"logger name: {logger.name}")
logger.debug(f"logger level: {logger.level}")


def get_absolute_path(path):
    absolute_path = pathlibs.Path(os.path.expandvars(path))
    logger.debug(f"absolute path: {absolute_path}")

    return absolute_path


get_full_path = get_absolute_path
full_path = get_absolute_path


def get_env_var(var, default=None):
    env_var = os.environ.get(var, default)
    logger.debug(f"env var: {env_var}")

    return env_var


get_env = get_env_var


def get_cloudflare_credentials(config, real_domain=None):
    """get cloudflare credentials"""

    if real_domain:
        domain = real_domain.replace(".", "_")

        return config["cloudflare_credentials"][domain]
    else:
        return config["cloudflare_credentials"]["default"]


def get_default_domains(config, zone_type="public"):
    """get default domains"""

    try:
        zones = config["zones"]["default_domains"]
    except (KeyError, TypeError) as e:
        logger.debug(f"key error - {e}")
        zones = {}

    if zone_type in zones:
        return zones[zone_type]
    else:
        return DEFAULT_DOMAINS


get_cloudflare_config = get_cloudflare_credentials


def convert_origin(orig_name, orig_domain, shared=False):
    """convert domain origin to standard form"""

    full_name = orig_name.strip(".").strip()
    domain = orig_domain.strip(".").strip()

    if shared:
        return full_name.replace(domain, "")

    if full_name == domain:
        return "{}.".format(full_name)
    if full_name == "@":
        return "{}.".format(domain)

    split_name = full_name.split(".")[0:-2]
    if not split_name:
        return "{}.{}.".format(full_name, domain)
    else:
        hostname = ".".join(split_name)
        if domain:
            return "{}.{}.".format(full_name, domain)
        else:
            return "{}.".format(hostname)


def shell_command(
    cmd,
    cwd=None,
    dry_run=False,
    shell=False,
    check=False,
    capture_output=True,
    pipe=False,
    input=None,
    split=True,
):
    """execute shell command"""

    logger.debug(f"original shell command: {cmd}")
    command = cmd
    if split and type(command) is str:
        logger.debug("command is of type string... splitting")

        command = command.split(" ")

        logger.debug(f"shell command arr: {command}")
        logger.debug(f"shell command to execute: {' '.join(command)}")
    else:
        logger.debug(f"split is false and/or command type is not a string")

    if dry_run:
        return (
            "would return stdout",
            "would return stderr",
            "would return process",
        )
    else:
        if input:
            logger.debug(f"input is '{input}'")

        stdout = None
        stderr = None
        if pipe:
            stdout = subprocess.PIPE
            capture_output = False

        process = subprocess.run(
            command,
            text=True,
            cwd=cwd,
            shell=shell,
            capture_output=capture_output,
            check=check,
            input=input,
            stdout=stdout,
            stderr=stderr,
        )
        if capture_output:
            return (process.stdout.strip(), process.stderr.strip(), process)
        else:
            return (None, None, process)


run_command = shell_command


def print_cloudflare_errors(error):
    """print full cloudflare errors"""

    if len(error) > 0:
        for err in error:
            print(err)
    else:
        print(error)


print_cf_error = print_cloudflare_errors
print_cf_errors = print_cloudflare_errors


def divider(char="=", times=55):
    """generate text divider"""

    return char * times


def print_divider(char="=", times=30, stderr=False):
    """print text divider"""

    output = divider(char, times)

    if stderr:
        print(output, file=sys.stderr)
    else:
        print(output)


def dns_lookup(record, record_type):
    """lookup dns record"""

    return dns.resolver.query(record, record_type)


def write_json_file(contents, filename):
    """write json file to disk"""

    if type(filename) == str:
        f = open(filename, "w")
    else:
        f = filename
    f.write(json.dumps(contents, indent=2))
    f.close()


def get_domain(hostname):
    logger.debug(f"hostname: {hostname}")

    return ".".join(hostname.split(".")[-2:])


def stderrprint(*args, **kwargs):
    logger.debug(f"original kwargs: {kwargs}")

    if "newline" in kwargs and not kwargs["newline"]:
        kwargs["flush"] = True
        kwargs["end"] = ""
        kwargs.pop("newline")
    logger.debug(f"after kwargs: {kwargs}")

    print(*args, **kwargs, file=sys.stderr)


eprint = stderrprint
errprint = stderrprint
