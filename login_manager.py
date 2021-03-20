from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user #added
from oauthlib.oauth2 import WebApplicationClient
import os
import pymongo
import requests
from dotenv import load_dotenv
from werkzeug.utils import redirect  #to invoke .env file

load_dotenv()
GIT_CLIENT_ID = os.getenv("GIT_CLIENT_ID")  # take .env from dotenv
GIT_CLIENT_SECRET = os.getenv("GIT_CLIENT_SECRET")  # take .env from dotenv

def create_login_manager():

    # flask_login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'


    @login_manager.unauthorized_handler
    def unauthenticated():
        print("blah")

        client = WebApplicationClient(client_id=os.getenv("GIT_CLIENT_ID"))
        uri = client.prepare_request_uri('https://github.com/login/oauth/authorize')
        return redirect(uri)

        pass # Add logic to redirect to the Github OAuth flow when unauthenticated

    @login_manager.user_loader
    def load_user(user_id):
        #return None
        return None

    return login_manager