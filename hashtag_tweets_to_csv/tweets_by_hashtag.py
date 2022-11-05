import configparser
import tweepy
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# search tweets
keywords = '#influencer'
limit = 1000
tweets = tweepy.Cursor(api.search_tweets, q = keywords,
     count = 100, tweet_mode = 'extended').items(limit)

# user tweets
# user = 'elonmusk'
# limit = 2000

# tweets = tweepy.Cursor(api.user_timeline,screen_name = user,
#     count = 200, tweet_mode = 'extended').items(limit)


# tweets = api.user_timeline(screen_name = user,
#     count = limit, tweet_mode = 'extended')

# creat DataFrame
columns = ['user', 'tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)
df.to_csv('inflencer_tweets.csv')