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
To build and run the app via Docker. You can use the following commands for production and development instances. Note local .env file is passed in during Docker run. 

Production: 
$ docker build --target production --tag todo-app:prod .
$ docker run -d -p 5000:5001 --env-file .env todo-app:prod
http://localhost:5000/items/get_all_cards

Development:
$ docker build --target development --tag todo-app:dev .
$ docker run -d -p 5002:5000 --env-file .env todo-app:dev
http://localhost:5002/items/get_all_cards

With mount bind on docker run: 
$ docker run -d -p 5000:5001 --mount type=bind,source="$(pwd)",target=/app --env-file .env todo-app:prod

$ docker run -d -p 5002:5000 --mount type=bind,source="$(pwd)",target=/app --env-file .env todo-app:dev

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
## MONGODB Credentials and Removal of Trello Post Module 9:
Please note Trello has been been replaced by MongoDB instance and login credential are encrypted via Travis CI. 
Locally this is also defined under .env files when passed in as a variable $MONGO_LOGIN

## Please note that following Module 10 github authenticiation and authorization is added for all routes for the app. 
Ensure to setup your Github OAuth App via github developer settings. All git IDs by default will retain ReadOnly access
to the app. 

```
## Migration to Azure Cloud:
The App as of Module 11 have been migrated over to Azure Cloud. This includes moving resources such as DB from MongoDB to cosmos DB on Azure. 
