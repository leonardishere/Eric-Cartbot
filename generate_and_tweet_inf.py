# generate_and_tweet_inf.py will generate random tweets and tweet them indefinitely
# note: because of the whole time.sleep() thread blocking issue, none of the print statements will actually print

try:
    debug = True
    if debug:
        print('in generate_and_tweet.py')
    import time
    from textgenrnn import textgenrnn
    from helper import clean_tweet
    import tweepy as tp
    from keys import keys
    import json

    if debug:
        print('opening auth & api')
    auth = tp.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_secret'])
    api = tp.API(auth)

    if debug:
        print('deserializing model')
    textgen = textgenrnn(
        weights_path='models/colaboratory_weights (2).hdf5',
        vocab_path='models/colaboratory_vocab (2).json',
        config_path='models/colaboratory_config (2).json'
    )

    if debug:
        print('generating text')
    num_tweets_attempted = 0
    num_tweets_tweeted = 0
    while True:
        line = textgen.generate(return_as_list=True)[0]
        line = clean_tweet(line)
        if debug:
            print('({},{}): {}'.format(num_tweets_attempted, num_tweets_tweeted, line))
        num_tweets_attempted = num_tweets_attempted + 1
        delay = 15*60
        try:
            api.update_status(line)
            num_tweets_tweeted = num_tweets_tweeted + 1
        except tp.error.TweepError as err:
            delay = 1
            err_code = json.loads(str(err).replace("'", '"'))[0]['code']
            if err_code == 186:
                if debug:
                    print('TweepError: status too long on "{}", length={}'.format(line, len(line)))
            elif err_code == 187:
                if debug:
                    print('TweepError: duplicate status on "{}"'.format(line))
            else:
                #if debug:
                print('unknown error: {}'.format(str(err)))
                delay = 30*60
        time.sleep(delay)

except Exception as err:
    print('Exception: {}'.format(str(err)))
