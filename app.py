from flask import Flask, render_template, request, redirect, url_for
import os
from trelloapp_class import Trello
import json
from trello_item import TrelloItem

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/') 
def root():
    return redirect(url_for('getAll')) ## replaced index

@app.route('/items/get_all_cards', methods = ["GET"])
def getAll(): 

    todo_resp = Trello().get_all_cards_from_todo_list()
    todo_dict = json.loads(todo_resp)
    todo_list = [ TrelloItem.from_trello_card(todo) for todo in todo_dict ]

    done_resp = Trello().get_all_cards_from_done_list()
    done_dict = json.loads(done_resp)
    done_list = [ TrelloItem.from_trello_card(todo) for todo in done_dict ]

    return render_template('all_items.html', cards_from_todo = todo_list, cards_from_done = done_list)

@app.route('/Items_Done', methods = ['POST', 'GET'])
def Items_Done():
    if request.method == 'POST':
        if request.form['action'] == 'Mark as Done':
            card_name = request.form['card_name']
            card_id = request.form['card_id']
            Trello().move_card_to_done(card_id)
        elif request.form['action'] == 'Delete':
            card_id = request.form['card_id']
            Trello().delete_card(card_id)
    return redirect("/")

@app.route('/Items_To_Do', methods = ['POST', 'GET'])
def Items_To_Do():
    if request.method == 'POST':
        if request.form['action'] == 'Mark as To Do':
            card_name = request.form['card_name']
            card_id = request.form['card_id']   
            Trello().move_card_to_do(card_id)
        elif request.form['action'] == 'Delete':
            card_id = request.form['card_id']
            Trello().delete_card(card_id)
    return redirect("/")

@app.route('/items/create_item_page', methods = ['POST', 'GET'])
def create_item_page():
    return render_template('CreateCard.html')

@app.route('/items/Items_To_Add', methods = ['POST', 'GET'])
def Items_To_Add():
    if request.method == 'POST':
        card_name=request.form['card_name']
        Trello().create_new_card(card_name)
    return redirect("/")

def create_app():
    app = Flask(__name__)
    @app.route('/test')
    def test():
        return ('shell test')
    return app
    


if __name__ == '__main__':
    app.run(debug=True)

