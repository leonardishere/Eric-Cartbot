# Eric Cartbot
![Awesomo](https://raw.githubusercontent.com/leonardishere/Eric-Cartbot/master/pfp_awesomo.png)  
Eric Cartbot, is a Twitter Bot that tweets in the style of Eric Cartman.  
The twitter account, @defnotan (short for Defnotan Androyd), can be found [here](https://twitter.com/defnotan). For those that don't understand the reference of the profile picture, "AWESOM-O" is the fifth episode of Season Eight in which Cartman disguises himself as a robot.

### Libraries used:
* [requests](http://docs.python-requests.org/en/master/) (to download the Southpark script)
* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) (to scrape the Southpark script)
* [textgenrnn](https://github.com/minimaxir/textgenrnn) (to train the model and generate text)  
    * textgenrnn is built off of [tensorflow](https://www.tensorflow.org/) and [keras](https://keras.io/)
* [tweepy](http://www.tweepy.org/) (to tweet)

Thanks to all developers of these libraries and all libraries that they're built off of.

### How To Replicate
+ Sign up for a [Twitter developer](https://developer.twitter.com/) account
+ Edit [keys_changeme.py](https://github.com/leonardishere/Eric-Cartbot/blob/master/keys_changeme.py)
+ Scrape some data using [scraper.py](https://github.com/leonardishere/Eric-Cartbot/blob/master/scraper.py) as a reference
+ Use the Colaboratory notebook from [textgenrnn](https://github.com/minimaxir/textgenrnn) to generate a model
+ Edit [generate_and_tweet_once.py](https://github.com/leonardishere/Eric-Cartbot/blob/master/generate_and_tweet_once.py) and [generate_and_tweet_inf.py](https://github.com/leonardishere/Eric-Cartbot/blob/master/generate_and_tweet_inf.py) to use the new model
+ Tweet tweet

### Legal
I'm not a lawyer, but I'm almost certain that all Southpark related media is property of Southpark and Comedy Central.  

This is a purely academic project with no money making intent.   

Somebody please enlighten me on the legality of training a machine learning model on the Southpark script and using it to generate similar text.  
