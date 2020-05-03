from flask import Flask
from datetime import datetime


def format_datetime(d_time):
#    """Use datetime to create specific string"""

    return d_time.strftime("%a, %d %b %Y %H:%M:%S GMT")


def dtime_to_uxtime(d_time):
    """fornat datetime to unix time format"""

    d_time.timestamp()

    return datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

app = Flask(__name__)


@app.route('/api/timestamp/')
def show_none():
        return {"unix": int(1000*datetime.now().timestamp()), "utc" : format_datetime(datetime.now())} 
    

@app.route('/api/timestamp/<date_string>')
def show_timestamp(date_string):
    print(f'essa é a var date_string: {date_string}')
    return '' 

app.run
