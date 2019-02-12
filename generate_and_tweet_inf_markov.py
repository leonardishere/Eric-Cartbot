# generate_and_tweet_inf_markov.py will generate random tweets via markov and tweet them indefinitely
# note: because of the whole time.sleep() thread blocking issue, none of the print statements will actually print

try:
    debug = True
    if debug:
        print('in generate_and_tweet_inf_markov.py')
    import time
    import tweepy as tp
    from keys import keys
    import json
    import markovify

    if debug:
        print('opening auth & api')
    auth = tp.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_secret'])
    api = tp.API(auth)

    if debug:
        print('training model')
    with open("data/cartman_only.dat") as f:
        text = f.read()
    text_model = markovify.Text(text, state_size=3)

    def generate_line_error_free():
        line = None
        while line is None:
            line = text_model.make_short_sentence(280)
        return line

    if debug:
        print('generating text')
    num_tweets_attempted = 0
    num_tweets_tweeted = 0
    while True:
        line = generate_line_error_free()
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
