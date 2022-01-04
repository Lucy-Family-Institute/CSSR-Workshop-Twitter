"""
The script is used to
"""

import requests, os, json, time
import yaml
import pandas as pd
import itertools
import tweepy
import logging
import numpy as np

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

os.getcwd()

##### Credentials #####
with open("./Code/twitter_credential.yaml", 'r') as stream:
    BearerToken = yaml.safe_load(stream)['BearerToken']

headers = {"Authorization": "Bearer {}".format(BearerToken)}

##### Search Tweets !Academic Research product track only #####

api = tweepy.Client(bearer_token=BearerToken)
user_id = api.get_user(username='taylorswift13')
temp = api.get_liked_tweets(id=17919972, max_results=100)
type(temp)
json.dumps(temp.data[0]['data'])
