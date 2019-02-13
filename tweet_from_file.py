# tweet_from_file.py will tweet the contents of a file line by line
# the file was created with an rnn

debug = True
if debug:
    print('in tweet_from_file.py')
import tweepy as tp
import time
import os
from keys import keys
import json

if debug:
    print('opening auth & api')
auth = tp.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_secret'])
api = tp.API(auth)

if debug:
    print('opening file')
filename = 'generated/colaboratory_gentext_20190202_213155.txt'
f = open(filename, "r")
lines = f.readlines()
f.close()

if debug:
    print('printing all lines')
time.sleep(5)
for line in lines:
    delay = 5
    try:
        api.update_status(line)
    except tp.error.TweepError as err:
        delay = 0.1
        err_code = json.loads(str(err).replace("'", '"'))[0]['code']
        if err_code == 186:
            print('TweepError: status too long on "{}", length={}'.format(line, len(line)))
        elif err_code == 187:
            print('TweepError: duplicate status on "{}"'.format(line))
    time.sleep(delay)

if debug:
    print('end program')
