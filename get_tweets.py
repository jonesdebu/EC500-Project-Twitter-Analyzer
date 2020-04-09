import re
import tweepy
from tweepy import OAuthHandler


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

    def buildTestSet(self, search_keyword):
        try:
            tweets_fetched = self.api.GetSearch(search_keyword, count=100)
            print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
            return [{"text":status.text, "label":None} for status in tweets_fetched]
        except:
            print("Unfortunately, something went wrong..")
            return None

def main():
    api = TwitterClient()
    search_term = input("Enter a search word:")
    testDataSet = api.buildTestSet(search_term)
    print(testDataSet[0:4])

if __name__ == '__main__':
    main()


