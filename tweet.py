## credentials contain:
# customer_key        = "XXX"
# customer_secret     = "XXX"
# access_token        = "XXX"
# access_token_secret = "XXX"
#from twitter_credentials.py import *
import tweepy
print(tweepy.__version__)
import twitter_credentials
userID = "vichupedia"

# Authorize our Twitter credentials
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name=userID,
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

for info in tweets[:3]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")

all_tweets = []
all_tweets.extend(tweets)
oldest_id = tweets[-1].id
while True:
    tweets = api.user_timeline(screen_name=userID,
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           max_id = oldest_id - 1,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    if len(tweets) == 0:
        break
    oldest_id = tweets[-1].id
    all_tweets.extend(tweets)
    print('N of tweets downloaded till now {}'.format(len(all_tweets)))

#tweets.full_text.encode("utf-8")

#transform the tweepy tweets into a 2D array that will populate the csv
from pandas import DataFrame
outtweets = [[tweet.id_str,
              tweet.created_at,
              tweet.favorite_count,
              tweet.retweet_count,
              tweet.full_text.encode("utf-8").decode("utf-8")]
             for idx,tweet in enumerate(all_tweets)]
df = DataFrame(outtweets,columns=["id","created_at","favorite_count","retweet_count", "text"])
df.to_csv('%s_tweets.csv' % userID,index=False)
df.head(3)
