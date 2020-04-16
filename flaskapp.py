from flask import Flask, render_template, request, jsonify
import flask_restful
from get_tweet_sentiment import TwitterClient

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/get_tweets', methods = ['GET', 'POST'])
def hastag_tweets():
    if request.method =='GET':
        return render_template('search_form.html')

    elif request.method == 'POST':
        api = TwitterClient()
        form_text = request.form["text"]    # get form text
        search_term = form_text.upper()  # process form text
        data_set = api.buildTestSet(search_term)

        return render_template(
        'tweet_results.html',
        response = data_set
        )

app.run()
