"""
Author: Yang Xu(yxu6@nd.edu)
Purpose: Workshop for twitter data and social science, session 2.
         The code includes how to read saved tweets data, parsing, merging.
         The final export would be a clean dataframe, with each column
"""

# Loading Packages
import pandas as pd
import os,json
import numpy as np
import time
import ast
from datetime import timezone

os.getcwd()
# ROOT_DIR = '/Users/yxu6/Alego/CSSR-Workshop-Twitter/'
ROOT_DIR = os.path.split(os.getcwd())[0]
# os.chdir()

##### read the saved data
####### method 1
raw_data = pd.read_csv('./Data/Breyer_data_2022_02.csv',sep='\t',dtype=object).dropna(subset=['id'])
raw_includes_tweets = pd.read_csv('./Data/Breyer_reference_tweets_2022_02.csv',sep='\t',dtype=object).dropna(subset=['id'])
raw_includes_users = pd.read_csv('./Data/Breyer_reference_users_2022_02.csv',sep='\t',dtype=object).dropna(subset=['id'])
raw_error = pd.read_csv('./Data/Breyer_errors_2022_02.csv',sep='\t',dtype=object)
raw_meta = pd.read_csv('./Data/Breyer_meta_2022_02.csv',sep='\t',dtype=object)

####### method 2
raw_data = pd.read_json('./Data/Breyer_data.json',orient='records',lines=True)
raw_includes_tweets = pd.read_json('./Data/Breyer_includes_tweets.json',orient='records',lines=True)
raw_includes_users = pd.read_json('./Data/Breyer_includes_users.json',orient='records',lines=True)
raw_meta = pd.read_json('./Data/Breyer_meta.json',orient='records',lines=True)

# method1
raw_errors = []
with open('./Data/Breyer_errors.json', 'r') as r:
    for line in r:
        temp = json.loads(line)
        if temp:
            raw_errors.append(pd.DataFrame(temp))
            # raw_Breyer_errors.append(json.loads(line))
raw_errors = pd.concat(raw_errors)

# method2
raw_errors = pd.read_json('./Data/Breyer_errors.json',orient='value',lines=True)
pd.melt(raw_errors).dropna(subset=['value']).value.apply(pd.Series)

##### summarize the data
raw_data.describe().T
raw_data.dtypes
raw_includes_tweets.describe().T
raw_includes_users.describe().T
raw_error.describe().T
raw_meta.describe().T

##### glimpse the data
raw_data.head()
raw_includes_tweets.head()
raw_includes_users.head()
raw_error.head()
raw_meta.head()

#### indexing the data
temp = raw_data.loc[0,'context_annotations']
type(temp)
#### convert str to json
# temp_json = ast.literal_eval(temp)
# type(temp_json)
pd.json_normalize(temp,sep="_")

temp = raw_data.loc[0,'entities']
type(temp)
# temp_json = ast.literal_eval(temp)
# type(temp_json)
pd.json_normalize(temp['annotations'],sep="_")
pd.json_normalize(temp['urls'],sep="_")

raw_data.head()

#### define functions to parse the json data
def context_flatten(id,context_annotations):
    # temp = ast.literal_eval(context_annotations)
    temp = pd.json_normalize(context_annotations,sep="_")
    temp = temp.assign(tweet_id = id)
    return(temp)

def entities_flatten(id,entities):
    # temp = ast.literal_eval(entities)
    if 'annotations' in  entities.keys():
        temp_annotations = entities['annotations']
        temp1 = pd.json_normalize(temp_annotations,sep="_").assign(tweet_id = id)
    else: temp1 = None
    if 'urls' in  entities.keys():
        temp = entities['urls']
        temp2 = pd.json_normalize(temp,sep="_").assign(tweet_id = id)
    else: temp2 = None
    if 'mentions' in  entities.keys():
        temp = entities['mentions']
        temp3 = pd.json_normalize(temp,sep="_").assign(tweet_id = id)
    else: temp3 = None
    if 'hashtags' in  entities.keys():
        temp = entities['hashtags']
        temp4 = pd.json_normalize(temp,sep="_").assign(tweet_id = id)
    else: temp4 = None
    if 'cashtags' in  entities.keys():
        temp = entities['cashtags']
        temp5 = pd.json_normalize(temp,sep="_").assign(tweet_id = id)
    else: temp5 = None
    return(temp1,temp2,temp3,temp4,temp5)

# raw_data.loc[raw_data.context_annotations.isna()]
#### vectorize functions
context_flatten_vct = np.vectorize(context_flatten)
entities_flatten_vct = np.vectorize(entities_flatten)

#### drop rows that the context_annotations are missing
raw_data.loc[raw_data.context_annotations.isna()]
raw_data_subset = raw_data.dropna(subset=['context_annotations'])

#### parse column context_annotations to another dataframe named context_data
#### the vectoried function takes array and work on each element of the array
context_list = context_flatten_vct(raw_data_subset.id, raw_data_subset.context_annotations)
context_data = pd.concat(context_list,ignore_index=True)

#### parse column entities into two additional dataframe: annotaions_data and url_data
raw_data_subset = raw_data.dropna(subset=['entities'])
annotations_list,urls_list,mention_list,hashtag_list,cashtag_list = entities_flatten_vct(raw_data_subset.id, raw_data_subset.entities)
annotations_data = pd.concat(annotations_list,ignore_index=True)
urls_data = pd.concat(urls_list,ignore_index=True)
mention_data = pd.concat(mention_list,ignore_index=True)
hashtag_data = pd.concat(hashtag_list,ignore_index=True)
cashtag_data = pd.concat(cashtag_list,ignore_index=True)

context_data.to_csv("./Data/context_data.csv",index=False,sep='\t')
annotations_data.to_csv("./Data/annotations_data.csv",index=False,sep='\t')
urls_data.to_csv("./Data/urls_data.csv",index=False,sep='\t')
mention_data.to_csv("./Data/mentions_data.csv",index=False,sep='\t')
hashtag_data.to_csv("./Data/hashtags_data.csv",index=False,sep='\t')
cashtag_data.to_csv("./Data/cashtags_data.csv",index=False,sep='\t')

urls_data.describe(include='all').T

#### parse the raw_includes_tweets

raw_includes_tweets.loc[raw_includes_tweets.context_annotations.isna()]
raw_includes_tweets_subset = raw_includes_tweets.dropna(subset=['context_annotations'])

includes_context_list = context_flatten_vct(raw_includes_tweets_subset.id, raw_includes_tweets_subset.context_annotations)
includes_context_data = pd.concat(context_list,ignore_index=True)

raw_includes_tweets_subset = raw_includes_tweets.dropna(subset=['entities'])
includes_annotations_list,includes_urls_list,includes_mention_list,includes_hashtag_list,includes_cashtag_list = entities_flatten_vct(raw_includes_tweets_subset.id, raw_includes_tweets_subset.entities)
includes_annotations_data = pd.concat(includes_annotations_list,ignore_index=True)
includes_urls_data = pd.concat(includes_urls_list,ignore_index=True)
includes_mention_data = pd.concat(includes_mention_list,ignore_index=True)
includes_hashtag_data = pd.concat(includes_hashtag_list,ignore_index=True)
includes_cashtag_data = pd.concat(includes_cashtag_list,ignore_index=True)

#### For those prefer a python-style programmers, bleow is an alternative to parse in a 'pythonic' way

#### drop rows that the context_annotations are missing
raw_data_subset = raw_data.dropna(subset=['context_annotations'])
context_data = pd.concat([pd.json_normalize(x,sep="_") for x in raw_data_subset['context_annotations']],keys=raw_data_subset.id)
context_data.reset_index(level=1,drop=True).reset_index(level=0)

#### drop rows that the entities are missing
raw_data_subset = raw_data.dropna(subset=['entities'])
context_data = pd.concat([pd.json_normalize(element,sep="_") for element in raw_data_subset['entities']],keys=raw_data_subset.id)
temp = context_data.reset_index(level=1,drop=True).reset_index(level=0)
annotations_data = pd.concat([pd.json_normalize(element,sep="_",errors='ignore') for element in temp['annotations'].dropna()],keys=temp.dropna(subset=['annotations']).id)
annotations_data.reset_index(level=1,drop=True).reset_index(level=0)
urls_data = pd.concat([pd.json_normalize(element,sep="_",errors='ignore') for element in temp['urls'].dropna()],keys=temp.dropna(subset=['urls']).id)
urls_data.reset_index(level=1,drop=True).reset_index(level=0)
mentions_data = pd.concat([pd.json_normalize(element,sep="_",errors='ignore') for element in temp['mentions'].dropna()],keys=temp.dropna(subset=['mentions']).id)
mentions_data.reset_index(level=1,drop=True).rename(columns={'id':'user_id'}).reset_index(level=0)
hashtags_data = pd.concat([pd.json_normalize(element,sep="_",errors='ignore') for element in temp['hashtags'].dropna()],keys=temp.dropna(subset=['hashtags']).id)
hashtags_data.reset_index(level=1,drop=True).reset_index(level=0)
cashtags_data = pd.concat([pd.json_normalize(element,sep="_",errors='ignore') for element in temp['cashtags'].dropna()],keys=temp.dropna(subset=['cashtags']).id)
cashtags_data.reset_index(level=1,drop=True).reset_index(level=0)

raw_data = raw_data.drop(['context_annotations','entities'],axis=1)

raw_includes_tweets.head()

#### Practice: Parse raw_include on your own
#### Item1: parse column context_annotations into another dataframe called: includes_context_data
#### Item2: parse column entities into another two dataframes called: includes_annotations_data and includes_url_data
#### Item3: parse column includesd_tweets into another two columns: includesd_id and includesd_tweets, then delete column: includesd_tweets
#### Item4: parse column public_metrics into another four columns: retweet_count, reply_count, like_count, quote_count, then delete column: public_metrics

#### parse column includesd_tweets into two columns: includesd_id, includesd_type
temp = raw_data.loc[~raw_data.referenced_tweets.isna(),['id','referenced_tweets']]
temp = raw_data.loc[1,'referenced_tweets']
type(temp[0])
#pd.DataFrame(raw_data.referenced_tweets).explode('referenced_tweets')
raw_data[['referenced_type','referenced_id']] = raw_data.referenced_tweets.explode().apply(pd.Series).drop(0,axis=1)
#raw_data.referenced_tweets.str.extract(r"type\'\:\s+\'(\w+)\'\,\s+\'id\'\:\s+\'(\d+)", expand=True).rename(columns={0:"referenced_id",1:"referenced_type"})
raw_data.loc[~raw_data.referenced_tweets.isna(),['referenced_tweets','referenced_id','referenced_type']]
#### then delete the original column referenced_tweets
raw_data = raw_data.drop('referenced_tweets', axis=1)

#### parse public metrics into 4 columns: retweet_count, reply_count, like_count, quote_count
raw_data.loc[0,'public_metrics']
raw_data[['retweet_count','reply_count','like_count','quote_count']] = pd.DataFrame.from_records(raw_data.public_metrics)
#raw_data.public_metrics.str.extract(r"\s(\d+),.*\s(\d+),.*\s(\d+),.*\s(\d+)",expand=True).astype(int)

raw_data[['public_metrics','retweet_count','reply_count','like_count','quote_count']]
#### then delete the original column public_metrics
raw_data = raw_data.drop('public_metrics', axis=1)
#### summarize the four new columns
raw_data[['retweet_count','reply_count','like_count','quote_count']].describe()

#### convert column created_at to US Eastern Time
raw_data['created_at']
raw_data['created_at'] = pd.to_datetime(raw_data['created_at']).dt.tz_convert('US/Eastern')
raw_data['created_at']

#### the convertsion is DST sensitive
dst_test = pd.Series(['2022-03-13T06:00:01Z','2022-03-13T07:00:01Z','2022-03-13T08:00:01Z'])
pd.to_datetime(dst_test).dt.tz_convert('US/Eastern')

raw_includes_tweets.describe().T
raw_includes_tweets.head()

#### Practice: Parse raw_includes_tweets on your own
#### Item3: parse column includes_tweets into another two columns: includes_id and includes_type, then delete column: includes_tweets
#### Item4: parse column public_metrics into another four columns: retweet_count, reply_count, like_count, quote_count, then delete column: public_metrics
#### Item5: convert column created_at to US Eastern Time
raw_data
raw_includes_tweets

#### merge raw_data with referenced_tweets
raw_includes_tweets_subset = raw_includes_tweets[['id','text']].rename(columns={'id':'referenced_id','text':'referenced_text'}).drop_duplicates(subset=['referenced_id'])
raw_includes_tweets_subset.referenced_id = raw_includes_tweets_subset.referenced_id.astype(float)
raw_data.referenced_id = raw_data.referenced_id.astype(str)
raw_includes_tweets_subset.dtypes
raw_data.dtypes
raw_data.loc[~raw_data.referenced_id.isna(),'referenced_id']
data_with_referenced_text = raw_data.merge(raw_includes_tweets_subset, how='left', on='referenced_id')
data_with_referenced_text[['id','text','referenced_text']]
data_with_referenced_text['all_text'] = data_with_referenced_text.text +" "+ data_with_referenced_text.referenced_text.fillna('')
data_with_referenced_text[['id','text','referenced_text','all_text']]
data_with_referenced_text.loc[0,'all_text']
data_with_referenced_text.loc[0,'text']
data_with_referenced_text.loc[0,'referenced_text']

data_with_referenced_text.to_csv("./Data/cleaned_data.csv",index=False,sep='\t')

#### Filter data by conditions
data_with_referenced_text
data_with_referenced_text.loc[data_with_referenced_text.like_count>50]
data_with_referenced_text.sort_values(by='like_count',ascending=False)[['id','all_text','retweet_count','reply_count','like_count','quote_count']]
