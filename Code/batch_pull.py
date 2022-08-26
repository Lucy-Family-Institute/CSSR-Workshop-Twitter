import pandas as pd
import tweepy
import os, json
import numpy as np
import time
import yaml
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
search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)

data_columns = ['author_id', 'context_annotations', 'conversation_id', 'created_at','entities', 'id', 'in_reply_to_user_id', 'public_metrics','referenced_tweets', 'text', 'Copyright']
error_columns = ['parameter', 'resource_id', 'value', 'detail', 'title', 'resource_type','type', 'section']
pd.DataFrame(search_tweets.data,dtype='object',columns=data_columns).to_csv(ROOT_DIR+'./Data/RT_com_data.csv',sep='\t', mode='a',index=False)
if 'user' in search_tweets.includes:
    pd.DataFrame(search_tweets.includes['users'],dtype='object').to_csv(ROOT_DIR+'./Data/RT_com_referenced_user.csv',sep='\t', mode='a',index=False)
if 'tweets' in search_tweets.includes:
    pd.DataFrame(search_tweets.includes['tweets'],dtype='object').to_csv(ROOT_DIR+'./Data/RT_com_referenced_tweets.csv',sep='\t', mode='a',index=False)
pd.DataFrame(search_tweets.errors,dtype='object',columns=error_columns).to_csv(ROOT_DIR+'./Data/RT_com_errors.csv',sep='\t', mode='a',index=False)
pd.DataFrame(search_tweets.meta,index=[0],dtype='object').to_csv(ROOT_DIR+'./Data/RT_com_meta.csv',sep='\t', mode='a',index=False)
next_token = search_tweets.meta['next_token']
n = 100
while next_token is not None:
    search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,next_token=next_token,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)
    pd.DataFrame(search_tweets.data,dtype='object',columns=data_columns).to_csv(ROOT_DIR+'./Data/RT_com_data.csv',sep='\t', mode='a',index=False)
    if 'user' in search_tweets.includes:
        pd.DataFrame(search_tweets.includes['users'],dtype='object').to_csv(ROOT_DIR+'./Data/RT_com_referenced_user.csv',sep='\t',mode='a',index=False)
    if 'tweets' in search_tweets.includes:
    pd.DataFrame(search_tweets.includes['tweets'],dtype='object').to_csv(ROOT_DIR+'./Data/RT_com_referenced_tweets.csv',sep='\t', mode='a',index=False)
    pd.DataFrame(search_tweets.errors,dtype='object',columns=error_columns).to_csv(ROOT_DIR+'./Data/RT_com_errors.csv',sep='\t', mode='a',index=False)
    pd.DataFrame(search_tweets.meta,index=[0],dtype='object').to_csv(ROOT_DIR+'./Data/RT_com_meta.csv',sep='\t', mode='a',index=False)
    next_token = search_tweets.meta['next_token']
    time.sleep(1)
    n += 100
    print("RT_com tweets pulled: %s" %n)
    # if (n==2500):
        # break


#%% Kyiv Post
user_id = api.get_user(username='KyivPost')

search_query = 'from:'+str(user_id.data['id'])
start_time = '2022-01-01T00:00:01Z'
end_time = '2022-08-24T23:59:59Z'

target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities','public_metrics']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)

data_columns = ['author_id', 'context_annotations', 'conversation_id', 'created_at','entities', 'id', 'in_reply_to_user_id', 'public_metrics','referenced_tweets', 'text', 'Copyright']
error_columns = ['parameter', 'resource_id', 'value', 'detail', 'title', 'resource_type','type', 'section']
pd.DataFrame(search_tweets.data,dtype='object',columns=data_columns).to_csv(ROOT_DIR+'./Data/KyivPost_data.csv',sep='\t', mode='a',index=False)
if 'user' in search_tweets.includes:
    pd.DataFrame(search_tweets.includes['users'],dtype='object').to_csv(ROOT_DIR+'./Data/KyivPost_referenced_user.csv',sep='\t',sep='\t', mode='a',index=False)
if 'tweets' in search_tweets.includes:
    pd.DataFrame(search_tweets.includes['tweets'],dtype='object').to_csv(ROOT_DIR+'./Data/KyivPost_referenced_tweets.csv',sep='\t', mode='a',index=False)
pd.DataFrame(search_tweets.errors,dtype='object',columns=error_columns).to_csv(ROOT_DIR+'./Data/KyivPost_errors.csv',sep='\t', mode='a',index=False)
pd.DataFrame(search_tweets.meta,index=[0],dtype='object').to_csv(ROOT_DIR+'./Data/KyivPost_meta.csv',sep='\t', mode='a',index=False)
next_token = search_tweets.meta['next_token']
n = 100
while next_token is not None:
    search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,next_token=next_token,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)
    pd.DataFrame(search_tweets.data,dtype='object',columns=data_columns).to_csv(ROOT_DIR+'./Data/KyivPost_data.csv',sep='\t', mode='a',index=False)
    if 'user' in search_tweets.includes:
        pd.DataFrame(search_tweets.includes['users'],dtype='object').to_csv(ROOT_DIR+'./Data/KyivPost_referenced_user.csv',sep='\t',sep='\t', mode='a',index=False)
    if 'tweets' in search_tweets.includes:
        pd.DataFrame(search_tweets.includes['tweets'],dtype='object').to_csv(ROOT_DIR+'./Data/KyivPost_referenced_tweets.csv',sep='\t', mode='a',index=False)
    pd.DataFrame(search_tweets.errors,dtype='object',columns=error_columns).to_csv(ROOT_DIR+'./Data/KyivPost_errors.csv',sep='\t', mode='a',index=False)
    pd.DataFrame(search_tweets.meta,index=[0],dtype='object').to_csv(ROOT_DIR+'./Data/KyivPost_meta.csv',sep='\t', mode='a',index=False)
    next_token = search_tweets.meta['next_token']
    time.sleep(1)
    n += 100
    print("KyivPost tweets pulled: %s" %n)
    # if (n==2500):
        # break
