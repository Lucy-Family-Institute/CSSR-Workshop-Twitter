"""
Author: Yang Xu(yxu6@nd.edu)
Purpose: Workshop for twitter data pulling, session 1.
         The code includes how to load credentials for twitter API, connect to twitter API, and pull tweets.
"""

import os, json
import yaml
import pandas as pd
import itertools
import tweepy
# import logging
import numpy as np

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# os.getcwd()

##### Load Credentials and connect to twitter API #####
with open("./Code/twitter_credential_true.yaml", 'r') as stream:
    BearerToken = yaml.safe_load(stream)['BearerToken']

# headers = {"Authorization": "Bearer {}".format(BearerToken)}
api = tweepy.Client(bearer_token=BearerToken)

##### get timeline of certain accounts #####
user_id = api.get_user(username='elonmusk')
user_timelines = api.get_users_tweets(id=user_id.data['id'],max_results=100)
next_token = user_timelines.meta['next_token']
user_timelines = api.get_users_tweets(id=user_id.data['id'],pagination_token=next_token,max_results=100)

target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
user_timelines = api.get_users_tweets(id=user_id.data['id'],expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)

type(user_timelines.includes)
user_timelines.includes.keys()
user_timelines.data[4]['context_annotations']
import pandas as pd
pd.DataFrame(user_timelines.data)

json.dumps(user_timelines.includes)
dir(user_timelines)
dir(user_timelines.data[0])
user_timelines.data[5].referenced_tweets

##### get tweets a certainuser liked #####

user_id = api.get_user(username='taylorswift13')
user_liked_tweets = api.get_liked_tweets(id=17919972, max_results=100)
next_token = user_timelines.meta['next_token']
user_liked_tweets = api.get_liked_tweets(id=user_id.data['id'],pagination_token=next_token,max_results=100)

target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
user_liked_tweets = api.get_liked_tweets(id=user_id.data['id'],expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)


##### search tweets Recommended for Essential and Elevated product tracks #####
search_query = "#GoIrish"
target_tweet_fields = ['public_metrics']
search_tweets = api.search_recent_tweets(query=search_query, expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)
search_tweets.data[].public_metrics

##### search tweets by a set of conditions in full archive (as early as 2006) !!! Academic Research product track only #####
search_query = '"Notre Dame" -is:retweet (@Marcus_Freeman1 OR "Freeman" OR "football")'
target_tweet_fields = ['public_metrics']
search_tweets = api.search_recent_tweets(query=search_query, expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)

dir(user_timelines)
dir(user_timelines.data[0])
json.dumps(temp.data[0]['data'])
