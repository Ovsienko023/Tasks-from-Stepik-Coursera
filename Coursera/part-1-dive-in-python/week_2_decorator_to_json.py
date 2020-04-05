import functools
import json


def to_json(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        oldd_func = func(*args, **kwargs) 
        mod_func = json.dumps(oldd_func)
        return mod_func
        
    return wrapper



