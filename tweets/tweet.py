import twitter
import secrets

MAX_COUNT = 200

def authenticate():
    api = twitter.Api(
        consumer_key=secrets.consumer_key,
        consumer_secret=secrets.consumer_secret,
        access_token_key=secrets.access_token_key,
        access_token_secret=secrets.access_token_secret)
    return api

def get_tweets(user, api):
    tweets = api.GetUserTimeline(screen_name=user, count=MAX_COUNT)
    for t in tweets:
        print t.text

if __name__ == "__main__":
    api = authenticate()
    get_tweets("VanCanucks", api)
