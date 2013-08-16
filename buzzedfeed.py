# from Marky import marky
from pymarkovchain import MarkovChain
import json
import re, sys
import string

# read in data and clean
data = json.load(open("listicles.json"))
text = "\n".join([d['title'] for d in data if d is not ""]).lower()
regex = re.compile('[%s]' % re.escape(string.punctuation))
text = regex.sub(" b", text)

# generate MC data
mc = MarkovChain("./markov")
mc.generateDatabase(text)
f = open("potential_tweets.txt", "a")

# generate and evaluate tweets
while 1:
  try:
    seed = sys.argv[1]
  except:
    seed = None
  if seed is not None:
    tweet = mc.generateStringWithSeed(seed).title()
  else:
    tweet = mc.generateString().title()
  print tweet
  answer = raw_input("Tweet this text? (yes|no|edit) ")
  if answer == "yes":
    f.write(tweet)
    break
  elif answer == "edit":
    tweet = raw_input("Enter in the edited text: ")
    f.write(tweet)
    break



