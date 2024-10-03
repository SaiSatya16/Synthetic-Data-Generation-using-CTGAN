from flask import Flask, request, jsonify, render_template, redirect, url_for
from api import *
from model import *
#import cors
from flask_restful import Api
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdb.sqlite3'
db.init_app(app)
api.init_app(app)
app.app_context().push()
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

