from flask import Flask, render_template, request, jsonify
import flask_restful
from sentiment import TwitterClient
from collections import Counter, defaultdict
from geolocation import listener
from geolocation import geolocation
import os
import shutil


app = Flask(__name__)
app.config["DEBUG"] = True

api = TwitterClient()   #so api can be used in multiple functions without creating a new api
search_term = 'Twitter' #default search term (quick solution to use in sentiment and geolocation)

@app.route('/', methods=['GET'])
def home():
    try:
        return render_template('index.html')
    except:
        print('Failed to render template: index.html')

@app.route('/get_tweets', methods = ['GET', 'POST'])
def hastag_tweets():
    try:
        if request.method =='GET':
            return render_template('search_form.html')

        elif request.method == 'POST':
            #tweets
            form_text = request.form["text"]    # get form text
            search_term = form_text.upper()  # process form text
            data_set = api.get_tweets(search_term, 10)
            geolocation(search_term)
            shutil.move('heatmap_result.html', 'templates')
            return render_template(
            'tweet_results.html', response=data_set
            #response = data_set
            )
    except:
        print('Function: hashtag_tweets failed to run')

@app.route('/heatmap_result', methods=['GET'])
def show_geo():
        try:

            return render_template(
            'heatmap_result.html'
            )
        except:
            print('Failed to generate heatmap')


if __name__ == "__main__":
    app.run(debug=True)
