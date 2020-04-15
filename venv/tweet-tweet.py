# You will need to PIP INSTALL tweepy for this to work and also create a twitter API.
import time

import tweepy

consumer_key = 'OxKVLR2o6fU51RWE1oJlJOrZS'
consumer_secret = 'BH84lUIN4VC0mVM3PR0VxPC2RqUlR1WFayOEQnV3HutW5KT3eZ'
access_token = '344612441-NerSQT9uogWAuRtCpROL7xmsBui6sIwzb3zHMPO6'
access_token_secret = 'EfzIVCuHllimOg7ZIos2wTtXFvYmRjUYEvqBSGoMMdbIB'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)  # prints your name.
print(user.screen_name)
print(user.followers_count)

search = "MKBHD"
numberOfTweets = 2


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(300)


# Generous follower bot
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Prachee Javiya':  # or follower.follow_count > 1000
        print(follower.name)
        follower.follow()

# Be a narcissist and love your own tweets. or retweet anything with a keyword!
for tweet in (tweepy.Cursor(api.search, search).items(numberOfTweets)):
    try:
        tweet.favorite()  # or tweet.retweet()
        print('Liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
