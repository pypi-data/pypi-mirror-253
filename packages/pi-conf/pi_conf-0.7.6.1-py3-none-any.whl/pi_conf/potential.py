"""Config"""
import csv
import logging
import os
from typing import Dict, List, Union

import toml
from platformdirs import site_config_dir

appname = "chatbot"


class AttrDict(dict):
    """An attr dict that allows referencing by attribute
    Example:
        cfg = AttrDict({"a":1, "b":{"c":3}})
        cfg.a.b.c == cfg["a"]["b"]["c"] # True
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

    def keys_exists(self, element, *keys):
        """
        Check if *keys (nested) exists in `element` (dict).
        """
        if not isinstance(element, dict):
            raise AttributeError("keys_exists() expects dict as first argument.")
        if len(keys) == 0:
            raise AttributeError(
                "keys_exists() expects at least two arguments, one given."
            )

        _element = element
        for key in keys:
            try:
                _element = _element[key]
            except KeyError:
                return False
        return True

    @staticmethod
    def from_dict(d: dict):
        """Make an AttrDict object without any keys
        that will overwrite the normal functions of a

        Args:
            d (dict): _description_

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        def _from_list(l):
            ### TODO change to generic iterable
            new_l = []
            for pot_dict in l:
                if isinstance(pot_dict, dict):
                    new_l.append(AttrDict.from_dict(pot_dict))
                elif isinstance(pot_dict, list):
                    new_l.append(_from_list(pot_dict))
                else:
                    new_l.append(pot_dict)
            return new_l
        d = Config(**d)
        for k, v in d.items():
            if k in _attr_dict_dont_overwrite:
                raise Exception(
                    f"Error! config key={k} would overwrite a default dict attr/func"
                )
            if isinstance(v, dict):
                d[k] = AttrDict.from_dict(v)
            elif isinstance(v, list):
                d[k] = _from_list(v)
        return d

    @staticmethod
    def get_keys_from_string(key_str: str) -> List[str]:
        """Get keys from string
        Keys are separated by periods, and can be quoted with single quotes
        . Keys with a period must be wrapped in single quotes.
        Examples:
        "model.name.zot.foo" -> ['model', 'name', 'zot', 'foo']
        "'model'.'name'.zot.foo" -> ['model', 'name', 'zot', 'foo']
        "'model.name'.zot.foo" -> ['model.name', 'zot', 'foo']
        """
        l = next(
            csv.reader([key_str], delimiter=".", skipinitialspace=True, quotechar="'")
        )
        return [x.strip('"').strip("'") for x in l]


class Config(AttrDict):
    pass


cfg = Config()  ## our config

_attr_dict_dont_overwrite = set([func for func in dir(dict) if getattr(dict, func)])


def set_log_level(level: str, logger_name: str = None):
    """Set logging to the specified level

    Args:
        level (str): log level
    """
    level = level.upper() if level else ""
    if not level:
        return
    logger = logging.getLogger(logger_name)
    logger_name = "root" if not logger_name else logger_name
    prev_level = logger.getEffectiveLevel()
    if level != prev_level:
        logger.setLevel(level)
        logger.debug(f"{logger_name} logging set to {level.upper()}")
    else:
        logger.debug(f"{logger_name} logger already set to {level.upper()}")
    return prev_level


def read_config_dir(config_file_or_appname: str) -> Config:
    """Read the config.toml file from the config directory
        This will be read the first config.toml found in following directories
            - ~/.config/<appname>/config.toml
            - <system config directory>/<appname>/config.toml

    Args:
        config_file_or_appname (str): App name for choosing the config directory

    Returns:
        AttrDict: the parsed config file in a dict format
    """
    check_order = [
        config_file_or_appname,
        f"~/.config/{config_file_or_appname}/config.toml",
        f"{site_config_dir(appname=config_file_or_appname)}/config.toml",
    ]
    for potential_config in check_order:
        potential_config = os.path.expanduser(potential_config)
        if os.path.isfile(potential_config):
            logging.debug(f"{appname} opening {potential_config}")
            with open(potential_config, "r") as fp:
                str_file = fp.read()
                cfg = toml.loads(str_file)
            return Config.from_dict(cfg)
    logging.debug(f"No config.toml found. Using blank config")
    return Config.from_dict({})


def set_database_config(appname_path_dict: Union[str, Dict]) -> Config:
    """Set the config.toml to use

    Args:
        appname_path_dict (str): Set the config for SQLAlchemy Extensions.
        Can be passed with the following.
            Dict: updates cfg with the given dict
            str: a path to a .toml file
            str: appname to search for the config.toml in the the application config dir

    Returns:
        Config: A config object (an attribute dictionary)
    """
    cfg.clear()
    if isinstance(appname_path_dict, dict):
        newcfg = Config.from_dict(appname_path_dict)
    else:
        newcfg = read_config_dir(appname_path_dict)
    cfg.update(newcfg)
    return cfg


## Overwrite logging level from environment variables if specified
set_log_level(os.getenv("CB_LOGLEVEL", None))

## Init our cfg
set_database_config(appname)

## Set our log level from config if specified if has not been overwritten from cmd line
if "CB_LOGLEVEL" not in os.environ:
    set_log_level(cfg.get("logging", {}).get("level"))



def _get_importer_project_name():
    """Get the name of the project that imported this module
    meant to be used from within a module to get the name of the project automtically"""

    for i in range(len(inspect.stack())):
        frame = inspect.stack()[i]
        module = inspect.getmodule(frame[0])
        if module:
            module_path = os.path.abspath(module.__file__)
            n = os.path.basename(os.path.dirname(module_path))
            if n not in ["pi_conf", "tests", "unittest"]:
                return n
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    if module:
        module_path = os.path.abspath(module.__file__)
        # Parse this path according to your project's structure
        return os.path.basename(os.path.dirname(module_path))
    return None
