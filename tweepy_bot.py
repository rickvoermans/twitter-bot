import tweepy
import datetime
import app

auth = tweepy.OAuthHandler(app.api_key, app.api_secret)
auth.set_access_token(app.oauth_token, app.oauth_secret)
api = tweepy.API(auth)

# variable to keep track of amount of tweets:
num = 1


def send_tweet():
    global num

    today = datetime.datetime.now()
    final_text = "This is my daily update number: " + str(num) + "\nToday's date: " + today.strftime(
        '%m/%d/%Y %H:%M')

    api.update_status(final_text)

    num += 1

    print("successfully updated Twitter status today")
