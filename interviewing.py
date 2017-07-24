"""
Alex-Antoine Fortin
Sunday, July 23rd 2017
Description
Web-app to record feedback about a candidate met during an interview at AmFam
"""
import flask, os
from datetime import date
from flask import Flask, session, render_template, redirect, url_for, abort
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'

@app.route('/interviewing', methods=['GET'])
def index():
    #It's the user's first visit to the website
    print 'This is a GET request'
    session['progress_count']=0
    return render_template( 'interviewing.html',
                            Progress=session['progress_count'],
                            DisplayName='Interviewing')

@app.route('/interviewing', methods=['POST'])
def interviewing():
    print 'This is a POST request. Count:{}.'.format(session['progress_count'])
    return render_template( 'interviewing.html',
                            Progress=session['progress_count'],
                            DisplayName='Interviewing')

# SERVING
if __name__ == '__main__':
    app.run(threaded=True)
