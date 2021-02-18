from flask import Flask, render_template, request, redirect, url_for
import os
# from trelloapp import Trello
import json
from todo_item import TodoItem #replaced Trello
from view_model import ViewModel
import pymongo
from bson import ObjectId, json_util
from datetime import datetime

def create_app():
    app = Flask(__name__)
    # app.config.from_object('flask_config.Config')  #removed secret key config

    myclient = pymongo.MongoClient("mongodb+srv://fpan:victor2021@cluster0.pc757.mongodb.net/ToDo?retryWrites=true&w=majority")    
    mydb = myclient["ToDo"]
    mycollection = mydb["All Items"]

    @app.route('/') 
    def root():
        return redirect(url_for('getAll')) 

    @app.route('/items/get_all_cards', methods = ["GET"])
    def getAll(): 

        myclient = pymongo.MongoClient("mongodb+srv://fpan:victor2021@cluster0.pc757.mongodb.net/ToDo?retryWrites=true&w=majority")    
        mydb = myclient["ToDo"]
        mycollection = mydb["All Items"]

        todo_resp = mycollection.find() # find method returns a cursor instance for iteration
    
        todo_list = [TodoItem.from_mongo_card(card) for card in todo_resp] ## returns list of dict

        return render_template('all_items.html', todos = ViewModel(todo_list))

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


    @app.route('/items/create_item_page', methods = ['POST', 'GET'])
    def create_item_page():
        return render_template('CreateCard.html')

    @app.route('/items/Items_To_Add', methods = ['POST', 'GET'])
    def Items_To_Add():
        if request.method == 'POST':
            card_name=request.form['card_name']
            mycollection.insert_one({"title":card_name, "status":"To Do", "update_time": datetime.now()})
        return redirect("/")
     

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)

    return app
