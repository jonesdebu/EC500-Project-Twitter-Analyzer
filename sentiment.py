import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient(object):

    def __init__(self):
        # Consumer keys and access tokens
        consumer_key = 'Ij5a4mBmBvNp4aiZ7F8uPhAWi'
        consumer_secret = 'DtrH2IGyq6KMds9zXzvsefd2knSee7K9xKqOdchvtTGuphCP2z'
        access_token = '931158103831216128-T4nbPvu1irazZ0t49MkZZqjT2xmQDSP'
        access_token_secret = 'y7WQZkM9jsiuQtmpopOc7rNctN910utOE3gDzyJaMYIgX'

    # Authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication failed.")

    # Function to classify sentiment using TextBlob
    def get_tweet_sentiment(self, tweet):  

        analysis = TextBlob(tweet)  

        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

    # Function to get tweets
    def get_tweets(self, query, count = 10): 

        tweets = [] 

        try: 
            fetched_tweets = self.api.search(q = query, count = count) 

            for tweet in fetched_tweets: 
                parsed_tweet = {} 
                parsed_tweet['text'] = tweet.text  
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

                # Handles tweet retweets
                if tweet.retweet_count > 0:  
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            return tweets 
  
        except tweepy.TweepError as e: 
            print("Error: " + str(e))

    # Function to get positive tweets
    def get_positive_tweets(self, tweets):

        positive_tweets = []

        for tweet in tweets:
            if tweet['sentiment'] == 'positive':
                positive_tweets.append(tweet)
        
        return positive_tweets

    # Function to get negative tweets
    def get_negative_tweets(self, tweets):

        negative_tweets = []

        for tweet in tweets:
            if tweet['sentiment'] == 'negative':
                negative_tweets.append(tweet)
        
        return negative_tweets

    # Function to get neutral tweets
    def get_neutral_tweets(self, tweets):

        neutral_tweets = []

        for tweet in tweets:
            if tweet['sentiment'] == 'neutral':
                neutral_tweets.append(tweet)
        
        return neutral_tweets

def main():
    api = TwitterClient()
    tweets = api.get_tweets(query = 'Tom Brady', count = 200)

    # Get positive tweets
    positive_tweets = api.get_positive_tweets(tweets) 

    # Percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(positive_tweets)/len(tweets))) 

    # Get negative tweets 
    negative_tweets = api.get_negative_tweets(tweets)

    # Percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(negative_tweets)/len(tweets)))

    # Get neutral tweets 
    neutral_tweets = api.get_neutral_tweets(tweets)

    # Percentage of neutral tweets 
    print("Neutral tweets percentage: {} %".format(100*len(neutral_tweets)/len(tweets)))  
  
    # Printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in positive_tweets[:10]: 
        print(tweet['text']) 
  
    # Printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in negative_tweets[:10]: 
        print(tweet['text'])

     # Printing first 5 neutral tweets 
    print("\n\nNeutral tweets:") 
    for tweet in neutral_tweets[:10]: 
        print(tweet['text']) 
    

if __name__ == '__main__':
    main()
