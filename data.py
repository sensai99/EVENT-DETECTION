import tweepy
import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
print("hello")

for tweet in tweepy.Cursor(api.search, q='#blacklivesmatter', since='2016-11-06', until='2016-11-07').items():

    print("hello")
    print("Name:", tweet.author.name.encode("utf-8"))
    print ("Screen-name:", tweet.author.screen_name.encode("utf-8"))
    print ("Tweet created:", tweet.created_at)
    print ("Tweet:", tweet.text.encode("utf-8"))
    print ("Retweeted:", tweet.retweeted)
    print ("Favourited:", tweet.favorited)
    print ("Location:", tweet.user.location.encode("utf-8"))
    print ("Time-zone:", tweet.user.time_zone)
    print ("Geo:", tweet.geo)
    print ("//////////////////")
