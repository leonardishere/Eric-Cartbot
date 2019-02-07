# test_tweet.py is used to test the ability to tweet by tweeting
# there is nothing specific about what should be tweeted

debug = True
if debug:
    print('in test_tweet.py')
import tweepy as tp
import time
import os
from keys import keys

if debug:
    print('opening auth & api')
auth = tp.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_secret'])
api = tp.API(auth)

if debug:
    print('posting new status')
#new_status = 'Hello! I\'m Eric Cartbot #ArtificialIntelligence #ComputationalCreativity #TwitterBot'
new_status = 'There is nothing to see here. Move along, folks'
try:
    api.update_status(new_status)
except tp.error.TweepError as err:
    print('TweepError: {}'.format(err))
    print('\t' + new_status)

if debug:
    print('end program')
