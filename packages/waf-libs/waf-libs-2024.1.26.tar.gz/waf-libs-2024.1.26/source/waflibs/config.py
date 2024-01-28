#!/usr/bin/python
"""helpers to manipulate config file"""

import copy
import json

import yaml


def sanitize(config, deep_copy=True):
    """remove secrets from config file"""

    if deep_copy:
        config_copy = copy.deepcopy(config)
    else:
        config_copy = config

    secret_text = [
        "password",
        "passwords",
        "api_key",
        "api_keys",
        "token",
        "tokens",
    ]

    if hasattr(config_copy, "items"):
        config_dict = config_copy
    else:
        config_dict = vars(config_copy)
    for k, v in config_dict.items():
        if type(v) == dict:
            sanitize(v, deep_copy=False)
        else:
            for text in secret_text:
                if text in k:
                    config_dict[k] = "REDACTED"

    return config_dict


def parse_yaml_file(filename):
    """parse yaml config by filename"""

    with open(filename) as f:
        config = parse_yaml(f.read())

    return config


def parse_yaml(config):
    """parse yaml config"""

    return yaml.load(config, Loader=yaml.FullLoader)


def parse_json_file(filename):
    """parse json config by filename"""

    f = open(filename)
    config = parse_json(f.read())
    f.close()

    return config


def parse_json(config):
    """parse json config"""

    return json.loads(config)
