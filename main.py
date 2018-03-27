from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width 540px;
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
        <form action = "/encrypted", method='POST'>
            <label>Rotate by:
                <input name='rot' type='text' value='0' />
            </label>
            <br>
            <br>
            <label>
                <textarea name='text'></textarea>
            </label>
            <br>
            <input type='submit' value='Submit'>
        </form>


    </body>
</html>"""

@app.route("/")
def index():
    return form

@app.route("/encrypted", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    rot = int(rot)
    text = request.form["text"]

    return rotate_string(text, rot)

app.run()