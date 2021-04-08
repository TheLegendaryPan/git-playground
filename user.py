from flask_login.utils import login_required, login_user, logout_user
from flask_login import UserMixin
from enum import Enum

class Role(Enum):
    Reader = 'ReadOnly'
    Writer = 'ReadWrite'

write_access = ['TheLegendaryPan']

class User(UserMixin):
    def __init__(self, id):  ##constructor!
        self.id = id 
    
    #r return the id used for current user
    def get_id(self):
        return self.id

    ## for part 2, hard code the ID to LegendaryPan. 
    ## set id = self. then read or write
    def get_role(self):
        return Role.Writer if self.id in write_access else Role.Reader
    

