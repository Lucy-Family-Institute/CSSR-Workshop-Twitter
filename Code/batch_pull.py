import pandas as pd
import tweepy
import os, json
import numpy as np
import time
import yaml
import pyarrow.orc as orc
# from datetime import timezone
os.getcwd()
# ROOT_DIR = '/Users/yxu6/Alego/CSSR-Workshop-Twitter/'
ROOT_DIR = os.path.split(os.getcwd())[0]
# os.chdir()

#%%
##### Load Credentials and connect to twitter API #####
with open(ROOT_DIR+"/Code/twitter_credential_true.yaml", 'r') as stream:
    BearerToken = yaml.safe_load(stream)['BearerToken']

# BearerToken = ""
api = tweepy.Client(bearer_token=BearerToken)

#%% RT_com
user_id = api.get_user(username='RT_com')
search_query = 'from:'+str(user_id.data['id'])
start_time = '2022-01-01T00:00:01Z'
end_time = '2022-08-24T23:59:59Z'
target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities','public_metrics']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,next_token=next_token,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)

# search_tweets_dict = search_tweets._asdict()
dir(search_tweets)

with open(ROOT_DIR+'/Data/RT_com_data.json', 'a', encoding='utf-8') as f:
    for tweet in search_tweets.data:
        f.write(json.dumps(tweet.data))
        f.write('\n')

for key, value in search_tweets.includes.items():
    print(key)
    with open(ROOT_DIR+'/Data/RT_com_includes_'+key+'.json', 'a', encoding='utf-8') as f:
        for item in value:
            f.write(json.dumps(item.data))
            f.write('\n')

with open(ROOT_DIR+'/Data/RT_com_meta.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(search_tweets.meta))
    f.write('\n')

with open(ROOT_DIR+'/Data/RT_com_errors.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(search_tweets.errors))
    f.write('\n')


if 'next_token' in search_tweets.meta:
    next_token = search_tweets.meta['next_token']
n = 100

while next_token is not None:
    search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,next_token=next_token,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)

    if search_tweets.data is not None:
        with open(ROOT_DIR+'/Data/RT_com_data.json', 'a', encoding='utf-8') as f:
            for tweet in search_tweets.data:
                f.write(json.dumps(tweet.data))
                f.write('\n')

        for key, value in search_tweets.includes.items():
            with open(ROOT_DIR+'/Data/RT_com_includes_'+key+'.json', 'a', encoding='utf-8') as f:
                for item in value:
                    f.write(json.dumps(item.data))
                    f.write('\n')

        with open(ROOT_DIR+'/Data/RT_com_meta.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(search_tweets.meta))
            f.write('\n')

        with open(ROOT_DIR+'/Data/RT_com_errors.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(search_tweets.errors))
            f.write('\n')

        if 'next_token' in search_tweets.meta:
            next_token = search_tweets.meta['next_token']
            time.sleep(1)
        else: next_token = None
        n += 100
        print("RT_com tweets pulled: %s" %n)

data_columns = ['author_id', 'context_annotations', 'conversation_id', 'created_at','entities', 'id', 'in_reply_to_user_id', 'public_metrics','referenced_tweets', 'text', 'Copyright']
error_columns = ['parameter', 'resource_id', 'value', 'detail', 'title', 'resource_type','type', 'section']


#%% Kyiv Post
user_id = api.get_user(username='KyivPost')

search_query = 'from:'+str(user_id.data['id'])
start_time = '2022-01-01T00:00:01Z'
end_time = '2022-08-24T23:59:59Z'

target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities','public_metrics']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)

# search_tweets_dict = search_tweets._asdict()
dir(search_tweets)

with open(ROOT_DIR+'/Data/KyivPost_data.json', 'a', encoding='utf-8') as f:
    for tweet in search_tweets.data:
        f.write(json.dumps(tweet.data))
        f.write('\n')

for key, value in search_tweets.includes.items():
    print(key)
    with open(ROOT_DIR+'/Data/KyivPost_includes_'+key+'.json', 'a', encoding='utf-8') as f:
        for item in value:
            f.write(json.dumps(item.data))
            f.write('\n')

with open(ROOT_DIR+'/Data/KyivPost_meta.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(search_tweets.meta))
    f.write('\n')

with open(ROOT_DIR+'/Data/KyivPost_errors.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(search_tweets.errors))
    f.write('\n')


if 'next_token' in search_tweets.meta:
    next_token = search_tweets.meta['next_token']
n = 100
while next_token is not None:
    search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,next_token=next_token,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)

    if search_tweets.data is not None:
        with open(ROOT_DIR+'/Data/KyivPost_data.json', 'a', encoding='utf-8') as f:
            for tweet in search_tweets.data:
                f.write(json.dumps(tweet.data))
                f.write('\n')

        for key, value in search_tweets.includes.items():
            print(key)
            with open(ROOT_DIR+'/Data/KyivPost_includes_'+key+'.json', 'a', encoding='utf-8') as f:
                for item in value:
                    f.write(json.dumps(item.data))
                    f.write('\n')

        with open(ROOT_DIR+'/Data/KyivPost_meta.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(search_tweets.meta))
            f.write('\n')

        with open(ROOT_DIR+'/Data/KyivPost_errors.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(search_tweets.errors))
            f.write('\n')

        if 'next_token' in search_tweets.meta:
            next_token = search_tweets.meta['next_token']
        else: next_token = None
        time.sleep(1)
        n += 100
        print("KyivPost tweets pulled: %s" %n)
