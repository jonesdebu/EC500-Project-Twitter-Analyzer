import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv
from geopy.geocoders import Nominatim
import gmplot


geolocator = Nominatim()

#Enter Twitter API Key information
consumer_key = 'Ij5a4mBmBvNp4aiZ7F8uPhAWi'
consumer_secret = 'DtrH2IGyq6KMds9zXzvsefd2knSee7K9xKqOdchvtTGuphCP2z'
access_token = '931158103831216128-T4nbPvu1irazZ0t49MkZZqjT2xmQDSP'
access_token_secret = 'y7WQZkM9jsiuQtmpopOc7rNctN910utOE3gDzyJaMYIgX'

coordinates = {'latitude': [], 'longitude': []}


class listener(StreamListener):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 20

    def on_data(self, data):
        try:
            json_data = json.loads(data)
            location = json_data['user']['location']
            if location:
                result = geolocator.geocode(location)
                if result:
                    coordinates['latitude'].append(result.latitude)
                    coordinates['longitude'].append(result.longitude)
                    print(coordinates)
                    self.counter = self.counter +1
                    print(self.counter)
                    if self.counter < self.limit:
                        return True
                    else:
                        return False
        except:
            pass

    def on_error(self, status):
        if status == 420:
            return False


def geolocation(keyword):
    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=[keyword])
        gmap = gmplot.GoogleMapPlotter(30, 0, 3)
        gmap.heatmap(coordinates['latitude'], coordinates['longitude'], radius=20)
        gmap.apikey = "AIzaSyAkNVgQPMhvAd4rh0Po4ckiwwSTSCCMwhE"
        gmap.draw("heatmap_result.html")
    except:
        print("error")

geolocation("Boston")
