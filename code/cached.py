import os
import dill
import pathlib


def cached(filename, overwrite=False):
    path = pathlib.Path(os.path.dirname(filename))
    path.mkdir(parents=True, exist_ok=True)

    def decorator(func):
        def new_func(*args, **kwargs):
            if overwrite or not os.path.exists(filename):
                with open(filename, "wb") as f:
                    dill.dump(func(*args, **kwargs), f)
            with open(filename, "rb") as f:
                return dill.load(f)
        return new_func
    
    return decorator
