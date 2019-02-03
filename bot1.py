import tweepy as tp
import time
import os
#import keys from keys
from keys import keys

auth = tp.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_secret'])
api = tp.API(auth)

new_status = 'Hello! I\'m Eric Cartbot #ArtificialIntelligence #ComputationalCreativity #TwitterBot'
try:
    api.update_status(new_status)
except tp.error.TweepError as err:
    print('TweepError: {}'.format(err))
    print('\t' + new_status)
