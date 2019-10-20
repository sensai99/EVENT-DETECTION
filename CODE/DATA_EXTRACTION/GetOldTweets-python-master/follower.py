import tweepy
import twitter_credentials
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def user_info(username):
	friend_count  = 0
	follower_count  = 0
	friends, followers = [], []
	for user in tweepy.Cursor(api.friends, screen_name=username).items():
		friend_count += 1
		friends.append(user.screen_name)
		print(friend_count)
	    # print('friend: ' + user.screen_name)

	for user in tweepy.Cursor(api.followers, screen_name=username).items():
		follower_count  += 1
		followers.append(user.screen_name)
	    # print('follower: ' + user.screen_name)

	return friends, followers

def tweet_count(username) :
	user = api.get_user(username)
	return user.followers_count