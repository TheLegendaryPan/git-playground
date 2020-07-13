# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
```bash
$ source setup.sh
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ flask run
```

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