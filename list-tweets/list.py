import os
import tweepy

# importing the environment variables - is this safe? We'll see ...
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# setup authentication with twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def lambda_handler(event, context):
    print("Processing started")

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

    print("Processing ended")
 
