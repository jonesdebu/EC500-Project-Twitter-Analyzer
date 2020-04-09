import tweepy

# Consumer keys and access tokens
consumer_key = 'Ij5a4mBmBvNp4aiZ7F8uPhAWi'
consumer_secret = 'DtrH2IGyq6KMds9zXzvsefd2knSee7K9xKqOdchvtTGuphCP2z'
access_token = '931158103831216128-T4nbPvu1irazZ0t49MkZZqjT2xmQDSP'
access_token_secret = 'y7WQZkM9jsiuQtmpopOc7rNctN910utOE3gDzyJaMYIgX'

# Twitter API authorization and initilization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)