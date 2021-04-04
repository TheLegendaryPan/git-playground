from flask_login.utils import login_required, login_user, logout_user
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id):  ##constructor!
        self.id = id 
    
    ## set id = self. then read or write
    