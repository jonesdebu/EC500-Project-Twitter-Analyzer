from flask import Flask, render_template, request, jsonify, Markup
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
global search_term
global data_set

search_term = 'Twitter' #default search term (quick solution to use in sentiment and geolocation)
data_set = []

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

            #create chart
            neutral = 0
            positive = 0
            negative = 0
            print(range(len(data_set)))
            legend = 'Number of tweets'
            labels = ['Positive', 'Negative', 'Neutral']

            for i in range(len(data_set)):
                if data_set[i]['sentiment'] == 'neutral':
                    neutral += 1

                elif data_set[i]['sentiment'] == 'positive':
                    positive += 1

                elif data_set[i]['sentiment'] == 'negative':
                    negative += 1

            values = [positive, negative, neutral]
            print(positive)
            print(negative)
            print(neutral)


            geolocation(search_term)

            if os.path.exists('templates/heatmap_result.html'):
                os.remove('templates/heatmap_result.html')
                shutil.move('heatmap_result.html', 'templates')

            else:
                shutil.move('heatmap_result.html', 'templates') #need to add logic for case where heatmap_result.html alredy exists

            return render_template(
            'chart.html', response=data_set, values=values, labels=labels, legend=legend
            #response = data_set
            )
    except:
        print('Function: hashtag_tweets failed to run')

@app.route('/chart', methods=['GET'])
def create_chart():
    neutral = 0
    positive = 0
    negative = 0
    print(range(len(data_set)))
    labels = ['Positive', 'Negative', 'Neutral']

    for i in range(len(data_set)):
        if data_set[i]['sentiment'] == 'neutral':
            neutral += 1

        elif data_set[i]['sentiment'] == 'positive':
            positive += 1

        elif data_set[i]['sentiment'] == 'negative':
            negative += 1

    values = [positive, negative, neutral]
    print(positive)
    print(negative)
    print(neutral)

    return render_template('chart.html', values=values, labels=labels)


@app.route('/heatmap', methods=['GET'])
def show_geo():
        try:

            return render_template(
            'heatmap_result.html'
            )
        except:
            print('Failed to generate heatmap')


if __name__ == "__main__":
    app.run(debug=True)
