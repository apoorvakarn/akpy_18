# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:32:09 2018 by Apoorva Karn """
#%% sentiment analysis
import tweepy          # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = 'oDqc5zewG8IoLIeLUuvcAB43g'
CONSUMER_SECRET = 'OEEWeaquF2P0z6LbXSeCQoMCOngTlsZFeXiDvfcH08NHtfYP9z'

# Access:
ACCESS_TOKEN  = '	964059262887526401-nJdNQwaiYqfLeHABH3WvcYOghrgQRjo'
ACCESS_SECRET = '	neflj1R8mUfeEMOukDMtYRMDx2uIOg2UYsZbctmtCZI55'

from credentials import *    # This will allow us to use the keys as variables

# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

# We create an extractor object:
extractor = twitter_setup()

# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name="ivy", count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

# We print the most recent 5 tweets:
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.text)
    print()

# We create a pandas dataframe as follows:
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# We display the first 10 elements of the dataframe:
display(data.head(10))
