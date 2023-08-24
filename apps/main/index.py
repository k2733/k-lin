from blueprints import main
from flask import redirect, render_template,request, session, json,jsonify, url_for
from datetime import datetime as dt, timezone,timedelta
import requests

try:
    @main.route('/home')
    def home():
        # page=requests.get('https://v2.jinrishici.com/info')
        # print(page)
        return render_template("/home.html")
except Exception as e:
    raise e
    