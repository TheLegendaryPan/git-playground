from flask_login import current_user
from functools import wraps
from flask import abort
from user import User, Role

def accesscheck(func):
    @wraps(func)
    def rolecheck(*args, **kwargs):  
        
        user = User(current_user.get_id())
        if user.get_role() == Role.Writer:
            return func(*args, **kwargs)
        else:
            abort(403, "Please login using Read-Write account")

    return rolecheck