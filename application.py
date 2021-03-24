import os
import sys

from flask import Flask, session, render_template, request, flash, redirect, abort, jsonify, current_app as app
from flask_session import Session
from datetime import datetime
import requests
import geojson
import json


app = Flask(__name__)

# fix windows terminal issue on my computer
if sys.platform.lower() == "win64":
    os.system('color')

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")
