import tweepy

# personal details
consumer_key ="sc"
consumer_secret ="a"
access_token ="a"
access_token_secret ="b"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Auth working")
except:
    print("not working")

# update the status
#api.update_status(status ="Hello Everyone !")
