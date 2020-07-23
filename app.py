from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import requests
import os
import trelloapp
import json

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/') #redirect root to the url or route mapped to the index function
def root():
    return redirect(url_for('getAll')) ## replaced index

### Module 2 stuff ### 

@app.route('/items/get_all_cards', methods = ["GET"])
def getAll(): 
    resp = trelloapp.get_all_cards_from_todo_list()
    resp_list = trelloapp.get_all_cards_from_done_list()
    #print(resp)
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
        card_name = request.form['card_name']
        card_id = request.form['card_id']
        
        trelloapp.move_card_to_done(card_id)
    return "Card moved to Done, Please refresh page!"

@app.route('/back_todo_item', methods = ['POST', 'GET'])
def back_todo_item():
    if request.method == 'POST':
        card_name = request.form['card_name']
        card_id = request.form['card_id']
        
        trelloapp.move_card_to_do(card_id)
    return "Card moved to To Do, Please refresh page!"

@app.route('/items/create_item', methods = ['POST', 'GET'])
def create_item():
    return render_template('CreateCard.html')

@app.route('/items/adding_new_item', methods = ['POST', 'GET'])
def adding_new_item():
    if request.method == 'POST':
        card_name=request.form['card_name']
        trelloapp.create_new_card(card_name)
    return "Card added to To Do, Please refresh page!"

# return the list ID from resp_json_list for name "Done"
# call update function from trellop to update the listID for cardID

#@app.route('/ToDo/CreateCard')
#def create_card(list_id, card_name): 
#    url_card = f'https://api.trello.com/1/cards'
#    parameters = {"name": card_name, "idList": list_id, "key": APP_KEY, "token": APP_TOKEN}
#    response = requests.request("POST", url_card, params=parameters)
#    card_id = response.json()['id']
#    return card_id
 

if __name__ == '__main__':
    app.run(debug=True)

