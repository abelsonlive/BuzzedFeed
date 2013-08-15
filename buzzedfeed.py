# from Marky import marky
from pymarkovchain import MarkovChain
import json
import re
import tweepy
import string

regex = re.compile('[%s]' % re.escape(string.punctuation))

auth = tweepy.OAuthHandler("untwGScsHBSgfScqldjbFQ", "8ZwFR5LMaMhfBEUVlhi7ce6BI71pVy7y3y8MLITA")
auth.set_access_token("1674196790-DRDVZ4wyKGQjsjrmxu7T54ZhJO73Nzkos8n2EVf", "F1rMCVDeb7caSVmiiaOcOm4AYbn0R7A4lGxIcnUpE")
api = tweepy.API(auth)
data = json.load(open("results-initial.json"))
text = "\n".join([d['title'] for d in data if d is not ""]).lower()
text = regex.sub("", text)
mc = MarkovChain("./markov")
mc.generateDatabase(text)
tweeted = False
while not tweeted:
  tweet = mc.generateString().title()
  print tweet
  answer = raw_input("Tweet this text? (yes|no|edit) ")
  if answer == "yes":
    api.update_status(tweet)
    print "TWEETED: " + tweet
    tweeted = True
  elif answer == "edit":
    tweet = raw_input("Enter in the edited text: ")
    api.update_status(tweet)
    print "TWEETED: " + tweet
    tweeted = True



