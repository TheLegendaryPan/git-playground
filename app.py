from flask import Flask, render_template, request, redirect, url_for
import os
# from trelloapp import Trello
import json
from todo_item import TodoItem #replaced Trello
from view_model import ViewModel
import pymongo
from bson import ObjectId, json_util
from datetime import datetime

# from flask_pymongo import PyMongo

myclient = pymongo.MongoClient("mongodb+srv://fpan:victor2021@cluster0.pc757.mongodb.net/ToDo?retryWrites=true&w=majority")    
mydb = myclient["ToDo"]
mycollection = mydb["All Items"]

#   alternative mongo db connection using flask_pymongo
#   app.config['MONGO_URI'] = 'mongodb+srv://fpan:victor2021>@cluster0.pc757.mongodb.net/ToDo?retryWrites=true&w=majority'
#   mongo.init_app(app)

        #test insert and delete into DB works
        #mycollection.insert_one({"_id":0, "title":"test insert into DB", "status":"To Do"})
        #mycollection.delete_one({"_id":0, "title":"test insert into DB", "status":"To Do"})

def create_app():
    app = Flask(__name__)
#   app.config.from_object('flask_config.Config')  #removed secret key config

    @app.route('/') 
    def root():
        return redirect(url_for('getAll')) 

    @app.route('/items/get_all_cards', methods = ["GET"])
    def getAll(): 

    #    removed below trello api data
    #    todo_resp = Trello().get_all_cards_from_board()
    #    todo_dict = json.loads(todo_resp)
    #    todo_list = [ TrelloItem.from_trello_card(card) for card in todo_dict ]
    #    return render_template('all_items.html', todos = ViewModel(todo_list))

         todo_resp = mycollection.find() 
         print("Todo_resp")
         print(todo_resp) # find method returns a cursor instance for iteration
        
         todo_list = [TodoItem.from_mongo_card(card) for card in todo_resp]
      #   for doc in todo_resp:
      #   todo_list.append(doc) # converting the cursor response into a list

         return render_template('all_items.html', todos = ViewModel(todo_list))

    @app.route('/Items_Done', methods = ['POST', 'GET'])
    def Items_Done():
    #    if request.method == 'POST':
    #        if request.form['action'] == 'Mark as Done':
    #            card_name = request.form['card_name']
    #            card_id = request.form['card_id']
    #            Trello().move_card_to_done(card_id)
    #        elif request.form['action'] == 'Delete':
    #            card_id = request.form['card_id']
    #            Trello().delete_card(card_id)
    #            
        if request.method == 'POST':
            if request.form['action'] == 'Mark as Done':
                card_name = request.form['card_name']
                card_id = request.form['card_id']
                print("Card ID")
                print(card_id)
                myquery = {"_id": ObjectId(card_id)}
                print(myquery)
                newvalue = {"$set": {"status": "Done"}}
                mycollection.update_one(myquery, newvalue)
            elif request.form['action'] == 'Delete':
                card_id = request.form['card_id']
                myquery = {"_id": ObjectId(card_id)}
                mycollection.delete_one(myquery)

        return redirect("/")

    @app.route('/Items_To_Do', methods = ['POST', 'GET'])
    def Items_To_Do():
      #  if request.method == 'POST':
      #      if request.form['action'] == 'Mark as To Do':
      #          card_name = request.form['card_name']
      #          card_id = request.form['card_id']   
      #          Trello().move_card_to_do(card_id)
      #      elif request.form['action'] == 'Delete':
      #          card_id = request.form['card_id']
      #          Trello().delete_card(card_id)
      #  return redirect("/")

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
        #if request.method == 'POST':
        #    card_name=request.form['card_name']
        #    Trello().create_new_card(card_name)
        # return redirect("/")

        if request.method == 'POST':
            card_name=request.form['card_name']
            mycollection.insert_one({"title":card_name, "status":"To Do", "update_time": datetime.now()})
        return redirect("/")
     

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)

    return app
