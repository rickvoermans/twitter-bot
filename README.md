# twitter-bot
This project contains a Twitter bot that is able to send and read messages. It connects to the Twitter API via Tweepy, a Python package found on [PiPy](https://pypi.org/project/tweepy/). I also used the package [schedule](https://pypi.org/project/schedule/) to be able to make the bot tweet about daily updates like the weather or date.

## configuration
In the [env/](https://github.com/rickvoermans/twitter-bot/tree/master/env) directory there is a app.py. This file contains my variables to connect with the Twitter API. For security reasons, I created another file config.py which looks like this:

```python
# configuration keys to access Twitter API with Tweepy
api_key = 'API KEY FROM TWITTER API'
api_secret = 'API SECRET FROM TWITTER API'

oauth_token = 'OAUTH TOKEN FROM TWITTER API'
oauth_secret = 'OAUTH SECRET FROM TWITTER API'
```

I excluded this from my Github but as you can see in app.py, I imported this so I can still use it. For extra security, you could retrieve your Auth **token** and **secret** instead of hardcoding them into a file. 