"""
Author: Yang Xu(yxu6@nd.edu)
Purpose: Workshop for twitter data pulling, session 1.
         The code includes how to load credentials for twitter API, connect to twitter API, request and pull tweets.
"""

#%%
# Loading Packages
import pandas as pd
import tweepy
import os, json
import numpy as np
import time
import yaml
# from datetime import timezone
os.getcwd()
ROOT_DIR = os.path.split(os.getcwd())[0]
# or use below
ROOT_DIR = 'path/to/where/read/or/load/files'
# os.chdir()

#%%
##### Load Credentials and connect to twitter API #####
with open(ROOT_DIR+"/Code/twitter_credential_true.yaml", 'r') as stream:
    BearerToken = yaml.safe_load(stream)['BearerToken']
# or put token below
BearerToken = 'copy/token/from/Developer Account Portal'
api = tweepy.Client(bearer_token=BearerToken)

#%%
##### get timeline of certain accounts #####
## Go to twitter and find the user name
user_id = api.get_user(username='elonmusk')
user_timelines = api.get_users_tweets(id=user_id.data['id'],max_results=10)
user_timelines

#%%
## Check the response
user_timelines.data
user_timelines.errors
user_timelines.meta

## convert data to a dataframe
pd.DataFrame(user_timelines.data)

#%%
## Use next_token to pull another 100 tweets
next_token = user_timelines.meta['next_token']
user_timelines = api.get_users_tweets(id=user_id.data['id'],pagination_token=next_token,max_results=100)
pd.DataFrame(user_timelines.data)

#%%
## Use for loop to pull more than 100 tweets
tweets_object = []
user_timelines = api.get_users_tweets(id=user_id.data['id'],max_results=100)
tweets_object.append(user_timelines)
next_token = user_timelines.meta['next_token']

for n in [2,3]:
    user_timelines = api.get_users_tweets(id=user_id.data['id'],pagination_token=next_token,max_results=100)
    tweets_object.append(user_timelines)
    next_token = user_timelines.meta['next_token']

tweets_object[0].meta
tweets_object[1].meta
tweets_object[2].meta

#%%
## Request additional fields and referenced tweets
target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
user_timelines = api.get_users_tweets(id=user_id.data['id'],expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)
pd.DataFrame(user_timelines.data)
user_timelines.errors
user_timelines.meta
user_timelines.includes
# user_timelines.includes.keys()

pd.DataFrame(user_timelines.includes['users'],dtype='object')
pd.DataFrame(user_timelines.includes['tweets'],dtype='object')

#%%
##### get tweets a certain user liked #####
user_id = api.get_user(username='taylorswift13')
target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
user_liked_tweets = api.get_liked_tweets(id=user_id.data['id'],expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)
pd.DataFrame(user_liked_tweets.data,dtype='object')
pd.DataFrame(user_liked_tweets.data,dtype='object').iloc[0,1]
user_liked_tweets.errors

##### fetch another 100 tweets with next_token
next_token = user_liked_tweets.meta['next_token']
user_liked_tweets = api.get_liked_tweets(id=user_id.data['id'],expansions=expansions,tweet_fields=target_tweet_fields,pagination_token=next_token,max_results=100)
pd.DataFrame(user_liked_tweets.data,dtype='object')

#%%
##### search tweets Recommended for Essential and Elevated product tracks #####
##### !!!Only returns tweets matched in the last seven days
search_query = "#GoIrish"
target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities','public_metrics']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
search_tweets = api.search_recent_tweets(query=search_query, expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)
pd.DataFrame(search_tweets.data,dtype='object')

#%%
##### search tweets !!! Academic Research product track only #####
##### !!! search the full-archive of twitter, back to 2006
search_query = "#GoIrish"
target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities','public_metrics']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
search_tweets = api.search_all_tweets(query=search_query, expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)
pd.DataFrame(search_tweets.data,dtype='object')

#%%
##### search tweets by a set of conditions in the last 7 days Recommended for Essential and Elevated product tracks #####
search_query = '(#SCOTUS OR Supreme) Breyer -is:retweet'
target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities','public_metrics']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
search_tweets = api.search_recent_tweets(query=search_query, expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)
pd.DataFrame(search_tweets.data,dtype='object')

#%%
##### search tweets by a set of conditions in full archive (as early as 2006) !!! Academic Research product track only #####
search_query = '(#SCOTUS OR Supreme) Breyer -is:retweet'
target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities','public_metrics']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
## Note: the time format is YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339) with 24h-clock. UTC timezone.
start_time = '2022-01-21T00:00:01Z'
end_time = '2022-02-01T23:59:59Z'
search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)
pd.DataFrame(search_tweets.data,dtype='object')

#%%
##### request and save data simultaneously #####
search_query = '(#SCOTUS OR Supreme) Breyer -is:retweet'
##### time is submitted in UTC timezone.
start_time = '2022-01-21T00:00:01Z'
end_time = '2022-02-01T23:59:59Z'
search_tweets_counts = api.get_all_tweets_count(query=search_query,start_time=start_time,end_time=end_time)
search_tweets_counts.meta
# search_tweets_counts.meta['next_token']
# search_tweets_counts2 = api.get_all_tweets_count(query=search_query,start_time=start_time,end_time=end_time,next_token=search_tweets_counts.meta['next_token'])

target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities','public_metrics']
expansions = ['referenced_tweets.id','in_reply_to_user_id']


## method 1: saving data in dataframe directly
## pros: data is saved in a structured format, compression is better than method 2
## cons: need to predefine fields
search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)
data_columns = ['author_id', 'context_annotations', 'conversation_id', 'created_at',
       'entities', 'id', 'in_reply_to_user_id', 'public_metrics',
       'referenced_tweets', 'text', 'Copyright']
error_columns = ['parameter', 'resource_id', 'value', 'detail', 'title', 'resource_type',
       'type', 'section']
pd.DataFrame(search_tweets.data,dtype='object',columns=data_columns).to_csv(ROOT_DIR+'/Data/Breyer_data_2022_02.csv',sep='\t', mode='a',index=False)
pd.DataFrame(search_tweets.includes['users'],dtype='object').to_csv(ROOT_DIR+'/Data/Breyer_reference_users_2022_02.csv',sep='\t', mode='a',index=False)
pd.DataFrame(search_tweets.includes['tweets'],dtype='object').to_csv(ROOT_DIR+'/Data/Breyer_reference_tweets_2022_02.csv',sep='\t', mode='a',index=False)
pd.DataFrame(search_tweets.errors,dtype='object',columns=error_columns).to_csv(ROOT_DIR+'/Data/Breyer_errors_2022_02.csv',sep='\t', mode='a',index=False)
pd.DataFrame(search_tweets.meta,index=[0],dtype='object').to_csv(ROOT_DIR+'/Data/Breyer_meta_2022_02.csv',sep='\t', mode='a',index=False)
next_token = search_tweets.meta['next_token']
n = 100
while next_token is not None:
    search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,next_token=next_token,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)
    pd.DataFrame(search_tweets.data,dtype='object',columns=data_columns).to_csv(ROOT_DIR+'/Data/Breyer_data_2022_02.csv',sep='\t',mode='a',index=False,header=False,float_format='str')
    pd.DataFrame(search_tweets.includes['users'],dtype='object').to_csv(ROOT_DIR+'/Data/Breyer_reference_users_2022_02.csv',sep='\t',mode='a',index=False,header=False,float_format='str')
    pd.DataFrame(search_tweets.includes['tweets'],dtype='object').to_csv(ROOT_DIR+'/Data/Breyer_reference_tweets_2022_02.csv',sep='\t',mode='a',index=False,header=False,float_format='str')
    pd.DataFrame(search_tweets.errors,dtype='object').to_csv(ROOT_DIR+'/Data/Breyer_errors_2022_02.csv',sep='\t',mode='a',index=False,header=False,float_format='str')
    pd.DataFrame(search_tweets.meta,index=[0],dtype='object').to_csv(ROOT_DIR+'/Data/Breyer_meta_2022_02.csv',sep='\t',mode='a',index=False,header=False,float_format='str')
    next_token = search_tweets.meta['next_token']
    time.sleep(1)
    n += 100
    print("Tweets pulled: %s" %n)
    if (n==500):
        break

## method 2: save data in json format
## pros: pulled data is completely saved, no need to predefine the fields
## cons: json is inefficient in terms of compression
search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,next_token=next_token,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)

with open(ROOT_DIR+'/Data/Breyer_data.json', 'a', encoding='utf-8') as f:
    for tweet in search_tweets.data:
        f.write(json.dumps(tweet.data))
        f.write('\n')

for key, value in search_tweets.includes.items():
    # print(key)
    with open(ROOT_DIR+'/Data/Breyer_includes_'+key+'.json', 'a', encoding='utf-8') as f:
        for item in value:
            f.write(json.dumps(item.data))
            f.write('\n')

with open(ROOT_DIR+'/Data/Breyer_meta.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(search_tweets.meta))
    f.write('\n')

with open(ROOT_DIR+'/Data/Breyer_errors.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(search_tweets.errors))
    f.write('\n')


if 'next_token' in search_tweets.meta:
    next_token = search_tweets.meta['next_token']
n = 100

while next_token is not None:
    search_tweets = api.search_all_tweets(query=search_query,expansions=expansions,next_token=next_token,tweet_fields=target_tweet_fields,max_results=100,start_time=start_time, end_time=end_time)

    if search_tweets.data is not None:
        with open(ROOT_DIR+'/Data/Breyer_data.json', 'a', encoding='utf-8') as f:
            for tweet in search_tweets.data:
                f.write(json.dumps(tweet.data))
                f.write('\n')

        for key, value in search_tweets.includes.items():
            with open(ROOT_DIR+'/Data/Breyer_includes_'+key+'.json', 'a', encoding='utf-8') as f:
                for item in value:
                    f.write(json.dumps(item.data))
                    f.write('\n')

        with open(ROOT_DIR+'/Data/Breyer_meta.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(search_tweets.meta))
            f.write('\n')

        with open(ROOT_DIR+'/Data/Breyer_errors.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(search_tweets.errors))
            f.write('\n')

        if 'next_token' in search_tweets.meta:
            next_token = search_tweets.meta['next_token']
            time.sleep(1)
        else: next_token = None
        n += 100
        print("Breyer tweets pulled: %s" %n)

    if (n==500):
        break

#%%
##### read the saved data from method 1
raw_data = pd.read_csv(ROOT_DIR+'/Data/Breyer_data_2022_02.csv',on_bad_lines='warn',sep='\t')
raw_reference_tweets = pd.read_csv(ROOT_DIR+'/Data/Breyer_reference_tweets_2022_02.csv',sep='\t')
raw_reference_users = pd.read_csv(ROOT_DIR+'/Data/Breyer_reference_users_2022_02.csv',sep='\t')
## if there is no error message, below could be an empty file
raw_error = pd.read_csv(ROOT_DIR+'/Data/Breyer_errors_2022_02.csv',sep='\t')
raw_meta = pd.read_csv(ROOT_DIR+'/Data/Breyer_meta_2022_02.csv',sep='\t')

##### read the saved data from method 2
raw_data = pd.read_json(ROOT_DIR+'/Data/Breyer_data.json',orient='records',lines=True)
raw_includes_tweets = pd.read_json(ROOT_DIR+'/Data/Breyer_includes_tweets.json',orient='records',lines=True)
raw_includes_users = pd.read_json(ROOT_DIR+'/Data/Breyer_includes_users.json',orient='records',lines=True)
raw_meta = pd.read_json(ROOT_DIR+'/Data/Breyer_meta.json',orient='records',lines=True)
raw_errors = pd.read_json(ROOT_DIR+'/Data/Breyer_errors.json',orient='value',lines=True)
pd.melt(raw_errors).dropna(subset=['value']).value.apply(pd.Series)

#%%
##### request a certain amount of tweets with one line #####
search_tweets = tweepy.Paginator(api.search_all_tweets, search_query, expansions=expansions,tweet_fields=target_tweet_fields,max_results=100).flatten(limit=1000)
pd.DataFrame(search_tweets)

#%%
##### search tweets by a set of conditions in full archive (as early as 2006)
# !!! Academic Research product track only #####
search_query = '"Notre Dame" -is:retweet (@Marcus_Freeman1 OR "Freeman" OR "football")'
target_tweet_fields = ['author_id','context_annotations','conversation_id','created_at','entities','public_metrics']
expansions = ['referenced_tweets.id','in_reply_to_user_id']
search_tweets = api.search_recent_tweets(query=search_query, expansions=expansions,tweet_fields=target_tweet_fields,max_results=100)
pd.DataFrame(search_tweets.data)
