from flask import Flask, request
import cgi
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <!--Define dimensions of text box-->
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540 px;
                font: 16px sans-serif;
                border.radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form action="/" method='post'>
            <label>
                <!--Small one line text box-->
                Rotate by:
                <input type="text" name="rot" value="0"/><br>
            </label>
            <!--Large text field-->
            <textarea name="text">{0}</textarea><br>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

#Encrypts text and prints output to textarea input field
@app.route('/', methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    
    caesar_string = rotate_string(str(text), int(rot))
    return form.format(caesar_string)

#Creates initial form at root
@app.route('/')
def index():
    return form.format('')

app.run()