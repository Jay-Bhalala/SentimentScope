
import tweepy
import json

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Stream Listener class
class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        print(f"Tweet collected: {tweet['text']}")
        # save the tweet to a database or file
        return True

    def on_error(self, status):
        print(f"Error: {status}")
        return False

# Start streaming
if __name__ == "__main__":
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['Python', 'DataScience'], languages=['en'])
