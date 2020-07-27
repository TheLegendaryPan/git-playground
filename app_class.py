from flask import Flask, render_template, request, redirect, url_for
#import session_items as session
import requests
import os
import trelloapp
import json

app_class = Flask(__name__)
app_class.config.from_object('flask_config.Config')

@app_class.route('/') #redirect root to the url or route mapped to the index function
def root():
    return redirect(url_for('getAll')) ## replaced index

### Module 2 stuff ### 

@app_class.route('/items/get_all_cards', methods = ["GET"])
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

@app_class.route('/complete_item', methods = ['POST', 'GET'])
def complete_item():
    if request.method == 'POST':
        card_name = request.form['card_name']
        card_id = request.form['card_id']
        
        trelloapp.move_card_to_done(card_id)
    return redirect("/")

@app_class.route('/back_todo_item', methods = ['POST', 'GET'])
def back_todo_item():
    if request.method == 'POST':
        card_name = request.form['card_name']
        card_id = request.form['card_id']
        
        trelloapp.move_card_to_do(card_id)
    return redirect("/")

@app_class.route('/items/create_item', methods = ['POST', 'GET'])
def create_item():
    return render_template('CreateCard.html')

@app_class.route('/items/adding_new_item', methods = ['POST', 'GET'])
def adding_new_item():
    if request.method == 'POST':
        card_name=request.form['card_name']
        trelloapp.create_new_card(card_name)
    return redirect("/")


if __name__ == '__main__':
    app_class.run(debug=True)

