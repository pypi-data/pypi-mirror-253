from typing import Callable
from IPython.core.magic import register_cell_magic
import os
import datetime
import json

import yaml
import pandas as pd

from .dataframes import write_df, read_df

cache_path = "/.cache"
cache_param_path = "/cache.yaml"
base_param = {}
actual_path = ""


def cache_reset(path: str) -> None:
    """Init or reset the cache at given path."""

    global actual_path
    actual_path = path

    if not os.path.exists(actual_path + cache_path):
        os.mkdir(actual_path + cache_path)

    f = open(actual_path + cache_path + cache_param_path, "w")
    yaml.dump(__init_config(), f)
    f.close()


def set_path(path: str) -> None:
    """Simply set the path of an existing cache, in order to be accessible later."""
    global actual_path
    actual_path = path


def cache_it(name: str, args, kwargs, obj: any, ttl: int = None) -> None:
    """Add or update a cache content"""

    # Set a precise name
    for arg in args: name += '_' + str(arg)
    for arg in kwargs: name += '_' + str(arg) + '-' + str(kwargs[arg])   

    # Get obj type
    obj_type = ""
    if isinstance(obj, pd.DataFrame):
        obj_type = "dataframe"
    elif isinstance(obj, str):
        obj_type = "string"
    elif isinstance(obj, dict):
        obj_type = 'dict'
    else:
        raise Exception(f"[CACHE] Unknown type {type(obj)}")

    # Load and update config
    config = __load_config()
    config[name] = {
        "cache_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ttl": config["default_ttl"] if ttl == None else ttl,
        "type": obj_type,
    }

    # Save the value
    path = actual_path + cache_path + "/" + name
    if obj_type == "dataframe":
        write_df(obj, path)
    elif obj_type == 'string':
        f = open(path, 'w')
        f.write(str(obj))
        f.close()
    elif obj_type == 'dict':
        f = open(path, 'w')
        f.write(json.dumps(obj))
        f.close()

    # Update config
    __save_config(config)


def cache_load(name: str, args, kwargs) -> any:
    """Load a content from the cache. It has to exists."""

    # Load config
    config = __load_config()

    # Set a precise name
    for arg in args: name += '_' + str(arg)
    for arg in kwargs: name += '_' + str(arg) + '-' + str(kwargs[arg])   

    # Read cache
    path = actual_path + cache_path + "/" + name
    if config[name]["type"] == "dataframe":
        to_return = read_df(path)
    elif config[name]["type"] == "string":
        f = open(path, 'r')
        to_return = f.read()
        f.close()
    elif config[name]["type"] == "dict":
        f = open(path, 'r')
        to_return = json.loads(f.read())
        f.close()
        

    return to_return


def cache_update_needed(name: str, args, kwargs) -> bool:
    """Tells if the given cached content is out of date or not."""

    # Load config
    config = __load_config()

    # Set a precise name
    for arg in args: name += '_' + str(arg)
    for arg in kwargs: name += '_' + str(arg) + '-' + str(kwargs[arg])   

    if not name in config:
        return True

    # Times
    now = datetime.datetime.now()
    config_time = datetime.datetime.strptime(config[name]["cache_date"], "%Y-%m-%d %H:%M:%S")
    delta_max = datetime.timedelta(hours=config[name]["ttl"])
    delta = now - config_time

    return delta_max <= delta


def cache_creation_needed(path: str) -> bool:
    """Tells if the given cached content is out of date or not."""

    global cache_path, cache_param_path
    return not os.path.exists(path + cache_path) and not os.path.exists(path + cache_path + cache_param_path)


def clean_other_caches() -> None:
    """Parse through the config in order to delete cashes that are too old."""
    global actual_path
    global cache_path


    # Load config
    config = __load_config()
    avoid_config = ['creation_date', 'default_ttl', 'index']
    to_del = []

    for key in config: 
        if key in avoid_config: continue

        # Times
        now = datetime.datetime.now()
        config_time = datetime.datetime.strptime(config[key]["cache_date"], "%Y-%m-%d %H:%M:%S")
        delta_max = datetime.timedelta(hours=config[key]["ttl"])
        delta = now - config_time

        # In case too old, delete file
        if delta_max <= delta:
            path = actual_path + cache_path + "/" + key
            os.remove(path)
            to_del.append(key)
    
    # Remove the keys from object
    for key in to_del:
        del config[key]
    __save_config(config)
        


def deco_cache_it(path: str = ".", ttl: int = 24) -> Callable:
    if cache_creation_needed(path):
        cache_reset(path)
        print(f"[CACHE] Creation at {path}")
    else:
        set_path(path)
        print(f"[CACHE] Existing at {path}")

    def inner(fct):
        def wrapper(*args, **kwargs):
            clean_other_caches()
            
            if cache_update_needed(fct.__name__, args, kwargs):
                result = fct(*args, **kwargs)
                cache_it(fct.__name__, args, kwargs, result, ttl)
                return result
            return cache_load(fct.__name__, args, kwargs)

        return wrapper

    return inner



@register_cell_magic
def magic_cache_it(line, cell=None):
    """Run a cell only if the given variables are not in cache. Fetch them otherwise"""

    path = "."

    if cache_creation_needed(path):
        cache_reset(path)
        print(f"[CACHE] Creation at {path}")
    else:
        set_path(path)
        print(f"[CACHE] Existing at {path}")

    cache_ready = True
    for var in line.split(" "):
        # Does a cache exists for this var?
        cache_ready = not cache_update_needed(var)
        if not cache_ready:
            break

    if not cache_ready:
        # Execute the cell
        get_ipython().ex(cell)
        # Save the result
        get_ipython().ex(f"u.cache_it('{var}', {var})")
        print("[CACHE] Cell has been executed, and result put in the cache")
    else:
        get_ipython().ex(f"{var} = u.cache_load('{var}')")
        print("[CACHE] Variables loaded from cache")



### PRIVATE FUNCTIONS ###


def __init_config() -> any:
    return {"creation_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "default_ttl": 24, "index": 1}


def __load_config() -> any:
    global actual_path
    f = open(actual_path + cache_path + cache_param_path, "r")
    obj = yaml.safe_load(f)
    f.close()
    return obj


def __save_config(config) -> None:
    global actual_path
    f = open(actual_path + cache_path + cache_param_path, "w")
    yaml.dump(config, f)
    f.close()