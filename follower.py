import tweepy
import twitter_credentials
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

for user in tweepy.Cursor(api.friends, screen_name="ashwanthkumar99").items():
    print('friend: ' + user.screen_name)

for user in tweepy.Cursor(api.followers, screen_name="ashwanthkumar99").items():
    print('follower: ' + user.screen_name)
