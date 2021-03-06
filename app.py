from flask import Flask, render_template, request, redirect, url_for
import os
from trelloapp import Trello
import json
from trello_class import TrelloItem
from view_model import ViewModel

def create_app():
    app = Flask(__name__)
#    app.config.from_object('flask_config.Config')  #can remove to delete secret key config

    @app.route('/') 
    def root():
        return redirect(url_for('getAll')) 

    @app.route('/items/get_all_cards', methods = ["GET"])
    def getAll(): 

        todo_resp = Trello().get_all_cards_from_board()
        todo_dict = json.loads(todo_resp)
        todo_list = [ TrelloItem.from_trello_card(card) for card in todo_dict ]

        return render_template('all_items.html', todos = ViewModel(todo_list))

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
     

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)

    return app
