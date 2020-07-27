from flask import Flask, render_template, request, redirect, url_for
import os
import trelloapp_class as tre
import json

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/') #redirect root to the url or route mapped to the index function
def root():
    return redirect(url_for('getAll')) ## replaced index

### Module 2 stuff ### 
@app.route('/items/get_all_cards', methods = ["GET"])
def getAll(): 

    resp = tre.Trello().get_all_cards_from_todo_list()
    resp_list = tre.Trello().get_all_cards_from_done_list()
    resp_json = json.loads(resp)
    resp_json_list = json.loads(resp_list)
    for cards in resp_json:   
        print(cards['name'])
    for lists in resp_json_list:   
        print(lists['id'] + lists['name'])
    return render_template('all_items.html', cards_from_todo = resp_json, cards_from_done = resp_json_list)

@app.route('/complete_item', methods = ['POST', 'GET'])
def complete_item():
    if request.method == 'POST':
        if request.form['action'] == 'Mark as Done':
            card_name = request.form['card_name']
            card_id = request.form['card_id']
            tre.Trello().move_card_to_done(card_id)
        elif request.form['action'] == 'Delete':
            card_id = request.form['card_id']
            tre.Trello().delete_card(card_id)
    return redirect("/")

@app.route('/back_todo_item', methods = ['POST', 'GET'])
def back_todo_item():
    if request.method == 'POST':
        if request.form['action'] == 'Mark as To Do':
            card_name = request.form['card_name']
            card_id = request.form['card_id']   
            tre.Trello().move_card_to_do(card_id)
        elif request.form['action'] == 'Delete':
            card_id = request.form['card_id']
            tre.Trello().delete_card(card_id)
    return redirect("/")

@app.route('/items/create_item', methods = ['POST', 'GET'])
def create_item():
    return render_template('CreateCard.html')

@app.route('/items/adding_new_item', methods = ['POST', 'GET'])
def adding_new_item():
    if request.method == 'POST':
        card_name=request.form['card_name']
        tre.Trello().create_new_card(card_name)
    return redirect("/")

def create_app():
    app = Flask(__name__)
    @app.route('/test')
    def test():
        return ('shell test')
    return app
    

# class ViewModel:
#     def __init__(self, cards_from_todo):
#         self.cards_from_todo=cards_from_todo

#     @property
#     def cards_from_todo(self):
#         return self.cards_from_todo

# item_view_model = ViewModel(cards_from_todo)
# render_template('all_items2.html', view_model=item_view_model)

if __name__ == '__main__':
    app.run(debug=True)

