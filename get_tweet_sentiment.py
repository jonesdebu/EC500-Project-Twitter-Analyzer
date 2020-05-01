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

    # Attempt authentication
        try:
            # Create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # Set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # Create tweepy API object to fetch tweets
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

                if tweet.retweet_count > 0: 
                    # If tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            return tweets 
  
        except tweepy.TweepError as e: 
            # Print error (if any) 
            print("Error: " + str(e))

def main():
    api = TwitterClient()
    tweets = api.get_tweets(query = 'Tom Brady', count = 200) 

    # Picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 

    # Percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 

    # Picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 

    # Percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
  
    # Printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 
  
    # Printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text']) 
    

if __name__ == '__main__':
    main()
