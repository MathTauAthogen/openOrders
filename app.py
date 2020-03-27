from flask import Flask, render_template
app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()
#Note: Use os.getenv() to get values in the dotenv file.

@app.route('/')
def index():
    return render_template("StartPage")
