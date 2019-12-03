import twitter
import json
from pymongo import MongoClient

api = twitter.Api(consumer_key="M8bGm8c5fIMENbsbMKcxtKAce",
                  consumer_secret="r0iJ6Eff9UARPAZQt0BNJGAg0T6w6vM9K6leL9AErwj2v831yL",
                  access_token_key="4916681190-50Ptag1hiDJrgfC0tUtyivmsbqK4LP2XyWKegAu",
                  access_token_secret="Eq9WzWfEDx4UAXVPy994gZcFSN5IaerqIhmpGKMeHSgzy")

client = MongoClient('mongodb://127.0.0.1:27017',
        username='bdb',
        password='bigdatabois',
        authSource='admin')

db = client.admin
twitdb = client['twitdb']
cringecol = twitdb['cringe']

presidentsDict = {'Bennet':[], 'Biden':[], 'Bloomberg':[], 'Booker':[], 'Bullock':[], 'Buttgieg':[], 'Castro':[], 'Delaney':[], 'Gabbard':[], 'Harris':[], 'Klobuchar':[], 'Patrick':[], 'Sanders':[], 'Sestak':[], 'Steyer':[], 'Warren':[], 'Williamson':[], 'Yang':[], 'Trump':[], 'Walsh':[], 'Weld':[]}

for name in presidentsDict:
    presidentsDict[name] = api.GetSearch(term=name+'&cringe')

for president in presidentsDict:
    for tweet in presidentsDict[president]:
        tweet_data = {
            '_id': tweet.id,
            'id':tweet.id,
            'president':president,
            'quoted_status_id':tweet.quoted_status_id,
            'text':tweet.text,
            'favorite_count':tweet.favorite_count,
            'retweet_count':tweet.retweet_count,
            'lang':tweet.lang,
            'user_id':tweet.user.id,
            'user_name':tweet.user.name,
            'user_screen_name':tweet.user.screen_name,
            'user_verified':tweet.user.verified
        }
        cringecol.update_one({'_id': tweet_data['_id']}, {"$set": tweet_data}, upsert=True)


'''
biden = presidentsDict['Biden']
biden[0].__dict__.keys() # gets the keys in twitter.models.Status object
'''
