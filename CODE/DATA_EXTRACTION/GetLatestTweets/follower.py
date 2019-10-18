import tweepy
import twitter_credentials
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

friend_count  = 0
follower_count  = 0

def user_info(username):
	friends, followers = [], []
	for user in tweepy.Cursor(api.friends, screen_name="KIRANSAI7777").items():
		# friends.append(user.screen_name)
	    print('friend: ' + user.screen_name)
	    print('count: ' + str(user.followers_count))

	for user in tweepy.Cursor(api.followers, screen_name="KIRANSAI7777").items():
		# follower_count  += 1
		followers.append(user.screen_name)
	    # print('follower: ' + user.screen_name)

	print(len(friends))
	return friends, followers

# a,b = user_info("sai")

user = api.get_user('KIRANSAI7777')
# print(user.screen_name)
print(user.followers_count)