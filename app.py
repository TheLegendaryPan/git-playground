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

## All route from below up to module is NO LONGER applicable since replacing index 
## with getAll from Module 2. Keep for reference No longer calling session.py
@app.route('/items', methods = ["GET", "POST", "PUT"])
def index():
    if request.method == 'POST':
        new_item = session.add_item(request.form['Title'])  ## Title is the name used in new.html
##      session._DEFAULT_ITEMS.append(new_item) #append to list instead calling session
        return redirect(url_for('index'))
### tried using PUT doesnt save input from form :(
    elif request.method == 'PUT':
        found_id = session.get_item(id)
        passed_id = request.form['Id']
        updated_status = request.form['Status_update']
        a = session.get_item(found_id)
        item = {'id': passed_id, 'status': updated_status, 'title': a['title']}
        update_item = session.save_item(item['id'])
        return redirect(url_for('index'))
    return render_template('index.html', Items=session.get_items())

@app.route('/items/new')
def new():
    return render_template('new.html')

@app.route('/GetItem/<id>') ## Trying to update the item
def show(id):
    found_id = session.get_item(id)
    return render_template('show.html', Items=found_id)   ##Items=found_id is to pass found_id to the variable called Items

@app.route('/GetItem/<id>/delete')
def delete(id):
    found_id = session.get_item(id)
    print(found_id, type(found_id))
    item = session.delete_item(found_id['id'])
    return redirect(url_for('index'))

@app.route('/GetItem/<id>/update', methods = ["GET", "POST"])
def update(id):
    found_id = session.get_item(id)
    return render_template('update.html', Items=found_id)

##FIXED BELOW. THANKS!

@app.route('/items/updated', methods = ["GET", "POST"])
def updated():
    if request.method == 'POST':
        passed_id = int(request.form['Id'])
        updated_status = request.form['Status_update']
        a = session.get_item(passed_id)
        item = {'id': passed_id, 'status': updated_status, 'title': a['title']}
        update_item = session.save_item(item)
        return redirect(url_for('index'))


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
    return "Card moved to Done, Please check Trello!"

@app.route('/back_todo_item', methods = ['POST', 'GET'])
def back_todo_item():
    if request.method == 'POST':
        card_name = request.form['card_name']
        card_id = request.form['card_id']
        
        trelloapp.move_card_to_do(card_id)
    return "Card moved to To Do, Please check Trello!"

# return the list ID from resp_json_list for name "Done"
# call update function from trellop to update the listID for cardID



# list ID, card ID, card Name

#getAll()

#pass the list name and card name into complete_item
#@app.route('/items/complete_item', methods = ["GET"])
#def update_to_done():
#    resp = trellopapp.



# #Module2 project #
# APP_KEY = os.environ.get('APP_KEY')
# APP_TOKEN=os.environ.get('APP_TOKEN')
# board_id= '83tSYoun'
# url = 'https://api.trello.com/1/cards/{id}'
# headers = {"Accept": "application/json"}
# query = {"key": APP_KEY, "token": APP_TOKEN}

# response=requests.request("GET", url, headers=headers, params=query)
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

#CONTROL K U / CONTROL K C
# def get_card_from_list(card_id):
#    parameters = {"key": APP_KEY, "token": APP_TOKEN}
#    response = request.get(url, % card_id, params=parameters)

#    if response.status_code == 200: 
#        resp = response.json()
#        myToDo = []
#        for result in resp['all']:
#            myToDo.append({
#                'CardID': result["idList"],
#                'CardName': result["name"]
#            })
#        return render_template("trello-api.html", myToDo=myToDo)
#    else: 
#        return f"There is a problem with the request" 

#@app.route('/ToDo/CreateCard')
#def create_card(list_id, card_name): 
#    url_card = f'https://api.trello.com/1/cards'
#    parameters = {"name": card_name, "idList": list_id, "key": APP_KEY, "token": APP_TOKEN}
#    response = requests.request("POST", url_card, params=parameters)
#    card_id = response.json()['id']
#    return card_id
 

if __name__ == '__main__':
    app.run(debug=True)

