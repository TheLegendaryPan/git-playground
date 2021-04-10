from flask import Flask, render_template, request, redirect, session, url_for, Response
import os
# from trelloapp import Trello
import json
from flask_login.utils import login_required, login_user, logout_user, current_user
from flask_login import UserMixin
from todo_item import TodoItem #replaced Trello
from view_model import ViewModel
import pymongo
from bson import ObjectId, json_util
from datetime import datetime
from dotenv import load_dotenv  #to invoke .env file
import os
from login_manager import create_login_manager 
import login_manager
from oauthlib.oauth2 import WebApplicationClient
import requests
from requests_oauthlib import OAuth2Session
from flask.json import jsonify
from user import User, Role


def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')  #added secret key back for module 10
    # added as part of module 10
    #login_disabled = os.getenv('LOGIN_DISABLED') == 'True'
    #app.config['LOGIN_DISABLED'] = login_disabled

    load_dotenv()
    MONGO_LOGIN = os.getenv("MONGO_LOGIN")  # take .env from dotenv
    MONGO_PASS = os.getenv("MONGO_PASS")  # take .env from dotenv
    GIT_CLIENT_ID = os.getenv("GIT_CLIENT_ID")  # take .env from dotenv
    GIT_CLIENT_SECRET = os.getenv("GIT_CLIENT_SECRET")  # take .env from dotenv

    myclient = pymongo.MongoClient('mongodb+srv://%s:%s@cluster0.pc757.mongodb.net/ToDo?retryWrites=true&w=majority' % (MONGO_LOGIN, MONGO_PASS))    
    mydb = myclient["ToDo"]
    mycollection = mydb["All Items"]

    login_manager = create_login_manager()
    login_manager.init_app(app)
    

    @app.route('/') 
    @login_required
    def root():
        return redirect(url_for('getAll')) 

    @app.route('/root/github/authorized')
    def login():
        # provder (github) sends the authorization code back
        code = request.args.get('code')
        client = WebApplicationClient(client_id=os.getenv("GIT_CLIENT_ID"), client_secret=os.getenv("GIT_CLIENT_SECRET"), code=code) 
        # client then sends he authorization code back to the providers token URL to exchange for token
        url,headers,body = client.prepare_token_request('https://github.com/login/oauth/access_token', client_secret = os.getenv("GIT_CLIENT_SECRET"), code=code)
        # parse the JSON response body post token validation, receives an access token or key        
        token_response = requests.post(url, headers=headers, data=body, auth=(os.getenv("GIT_CLIENT_ID"), os.getenv("GIT_CLIENT_SECRET")))
        # parse the token from the response
        token = client.parse_request_body_response(token_response.text)
        # save the token
        session['oauth_token'] = token
        # get user id details by passing above git token
        github = OAuth2Session(os.getenv("GIT_CLIENT_ID"), token=session['oauth_token'])
        # can see my details in response 200
        userinfo_response = jsonify(github.get('https://api.github.com/user').json())
        # prints out logged in user, TheLegendaryPan in this case!
        user_id = userinfo_response.json['login']
        print(userinfo_response.json['login'])

        user= User(user_id)
        login_user(user)
        
        return redirect(url_for('getAll'))


    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return Response('<p>Logged out</p>')

    @app.route('/items/get_all_cards', methods = ["GET"])
    @login_required
    def getAll(): 

        myclient = pymongo.MongoClient('mongodb+srv://%s:%s@cluster0.pc757.mongodb.net/ToDo?retryWrites=true&w=majority' % (MONGO_LOGIN, MONGO_PASS))    
        mydb = myclient["ToDo"]
        mycollection = mydb["All Items"]

        todo_resp = mycollection.find() # find method returns a cursor instance for iteration
    
        todo_list = [TodoItem.from_mongo_card(card) for card in todo_resp] ## returns list of dict

        # user authorization
        user_authorizaion = User(current_user.get_id())
        reader = user_authorizaion.get_role() == Role.Reader

        return render_template('all_items.html', todos = ViewModel(todo_list, reader))

    @login_required
    @app.route('/Items_Done', methods = ['POST', 'GET'])
    def Items_Done():
        if request.method == 'POST':
            if request.form['action'] == 'Mark as Done':
                card_name = request.form['card_name']
                card_id = request.form['card_id']
                myquery = {"_id": ObjectId(card_id)}
                newvalue = {"$set": {"status": "Done"}}
                mycollection.update_one(myquery, newvalue)
            elif request.form['action'] == 'Delete':
                card_id = request.form['card_id']
                myquery = {"_id": ObjectId(card_id)}
                mycollection.delete_one(myquery)

        return redirect("/")

    @login_required
    @app.route('/Items_To_Do', methods = ['POST', 'GET'])
    def Items_To_Do():
        if request.method == 'POST':
            if request.form['action'] == 'Mark as To Do':
                card_name = request.form['card_name']
                card_id = request.form['card_id']
                myquery = {"_id": ObjectId(card_id)}
                newvalue = {"$set": {"status": "To Do"}}
                mycollection.update_one(myquery, newvalue)
            elif request.form['action'] == 'Delete':
                card_id = request.form['card_id']
                myquery = {"_id": ObjectId(card_id)}
                mycollection.delete_one(myquery)
        return redirect("/")

    @login_required
    @app.route('/items/create_item_page', methods = ['POST', 'GET'])
    def create_item_page():
        return render_template('CreateCard.html')

    @login_required
    @app.route('/items/Items_To_Add', methods = ['POST', 'GET'])
    def Items_To_Add():
        if request.method == 'POST':
            card_name=request.form['card_name']
            mycollection.insert_one({"title":card_name, "status":"To Do", "update_time": datetime.now()})
        return redirect("/")
     

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)

    return app
