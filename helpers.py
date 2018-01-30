"""
Helper lib.
"""

from functools import wraps
from flask import session

def init_session(test):
    """ Decorator to init the session """
    @wraps(test)
    def wrap(*args, **kwargs):
        if "todo" not in session:
            session["todo"] = {}
        return test(*args, **kwargs)
    return wrap
