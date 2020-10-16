# main program for the bot
import schedule
from tweepy_bot import send_tweet

# run the func send_tweet()
schedule.every(1).days.at("12:00").do(send_tweet)

while True:
    schedule.run_pending()
