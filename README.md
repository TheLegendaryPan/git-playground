# DevOps Apprenticeship: Project Exercise

## Getting started

Please copy .env.template to .env and to run poetry install to install the essential dependencies needed for the to-do app. 

Once complete, you can use "poetry run flask run", "poery run pytest" to start the to-do app via flask and run through the test cases. 

"vagrant up" command can be used if you've vagrant and a vypervisor installed to bring up the environment in VM. 

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


```
## API Credentials and Trello Usage:  
APP_KEY and APP_TOKEN are stored on the local .env file, not uploaded during GIT push. This is invoked by: 
from dotenv import load_dotenv  
load_dotenv()

board_id and list_id are extracted from Trello website. 
https://trello.com/b/83tSYoun/fengs-to-do
Renaming above link to https://trello.com/b/83tSYoun/fengs-to-do.json to display full output in json format. 
Alternatively you can extract board, list and card id details using Postman. 

```
