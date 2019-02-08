# generate_and_tweet_once.py will generate a random tweet and tweet it

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

    line = textgen.generate(return_as_list=True)[0]
    line = clean_tweet(line)
    if debug:
        print(line)
    try:
        api.update_status(line)
    except tp.error.TweepError as err:
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

except Exception as err:
    print('Exception: {}'.format(str(err)))
