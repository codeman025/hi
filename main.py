from flask import Flask # imports Flask class from flask module

app = Flask(__name__)#"app" will be created by the "Flask constructor"-"name" is a variable
app.config['DEBUG'] = True#the "debug" setting will be enabled, shows errors in browser, and host swapping?
@app.route("/")#decorator that creates a mapping between the path, in this case the root, or "/" and the funcction
def index():# function is ran when the webpage is at "/" aka the base page
    return "Hello World"

app.run()#passes the torch to Flask, this funcction loops forever so put it last, runs the server and requests

'''<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
    </body>
</html>'''