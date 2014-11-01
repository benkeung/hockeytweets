import twitter
import secrets
import time

MAX_COUNT = 200

class Tweeter(object):

    def __init__(self):
        self._since_id_dict = dict()

    def authenticate(self):
        api = twitter.Api(
            consumer_key=secrets.consumer_key,
            consumer_secret=secrets.consumer_secret,
            access_token_key=secrets.access_token_key,
            access_token_secret=secrets.access_token_secret)
        return api

    def get_tweets(self, user, api):
        since_id = self.__get_since_id(user)
        tweets = api.GetUserTimeline(screen_name=user, count=MAX_COUNT,
                                    since_id=since_id)

        if tweets:
            last_since_id = tweets[0].id
            self.__set_since_id(user, last_since_id)

    # TODO: Need to persist this data
    def __get_since_id(self, user):
        return self._since_id_dict.get(user)

    def __set_since_id(self, user, since_id):
        self._since_id_dict[user] = since_id


if __name__ == "__main__":
    tweeter = Tweeter();
    api = tweeter.authenticate()
    tweets = tweeter.get_tweets("VanCanucks", api)
    time.sleep(60)
    print "\n\n\nT\n\n\n"
    tweets = tweeter.get_tweets("VanCanucks", api)
