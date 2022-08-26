"""
Author: Yang Xu(yxu6@nd.edu)
Purpose: Workshop for twitter data pulling, session 3.
         The code includes how to apply established model to analyze the data.
"""
import os
import openai
import yaml
import pandas as pd
import nltk


#### Load the data ####
cleaned_data = pd.read_csv("./Data/cleaned_data.csv",dtype="object",sep='\t')
context_data = pd.read_csv("./Data/context_data.csv",dtype="object",sep='\t')
annotations_data = pd.read_csv("./Data/annotations_data.csv",dtype="object",sep='\t')
urls_data = pd.read_csv("./Data/urls_data.csv",dtype="object",sep='\t')
mention_data = pd.read_csv("./Data/mentions_data.csv",dtype="object",sep='\t')
hashtag_data = pd.read_csv("./Data/hashtags_data.csv",dtype="object",sep='\t')

#### Descriptive Analysis

##### entities associated with each tweet
tweet_entities = context_data.groupby('tweet_id')['entity_name'].unique().reset_index()
tweet_entities.head()
temp = context_data.entity_name.value_counts()
temp[0:30]
target_tweet_id = context_data.loc[context_data.entity_name=="Dick Durbin"].tweet_id.unique()
cleaned_data.loc[cleaned_data.id.isin(target_tweet_id),'text']

tweet_annotations = annotations_data.groupby('tweet_id')['normalized_text'].unique().reset_index()
temp = annotations_data.normalized_text.value_counts()
temp[0:30]

##### domains associated with each tweet
tweet_domains = context_data.groupby('tweet_id')['domain_name'].unique().reset_index()
tweet_domains.head(n=10)
##### domains frequency by domain
temp = context_data.domain_name.value_counts()
temp.iloc[0:30]


##### mention associate with each tweet
mention_data.username.value_counts().reset_index().rename(columns={"index":"mentioned_user","username":"counts"})
temp = mention_data.username.value_counts()
temp[0:30]

##### hashtag associate with each tweet
hashtag_data.tag.value_counts().reset_index().rename(columns={"index":"hashtag","username":"counts"})
temp = hashtag_data.tag.value_counts()
data_plot = temp[0:30].reset_index().rename(columns={'index':'hashtag','tag':'counts'})
data_plot.head()

import matplotlib.pyplot as plt
plt.bar(data_plot['hashtag'],data_plot['counts'])


#### Sentiment Analysis

cleaned_data = pd.read_csv("./Data/cleaned_data.csv",dtype="object",sep='\t')
cleaned_data = cleaned_data.assign(text_to_analyze = cleaned_data.text.str.replace(r'http\S+', '',regex=True).replace(r'@\w+','',regex=True).replace(r'\n','',regex=True))
cleaned_data = cleaned_data[['id','text','referenced_text','all_text','text_to_analyze']]
cleaned_data = cleaned_data.applymap(str)
cleaned_data.head()
cleaned_data.dtypes

cleaned_data.loc[0,'text']
cleaned_data.loc[0,'text_to_analyze']

##### nltk sentiment analysis
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import tokenize
## ! nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
# lines_list = tokenize.sent_tokenize()
temp = analyzer.polarity_scores(cleaned_data.text_to_analyze[3])
pd.DataFrame(temp,index=[0])

sentiment_result = pd.concat([pd.DataFrame(analyzer.polarity_scores(element),index=[0]) for element in cleaned_data.text_to_analyze],keys=cleaned_data.id)
sentiment_result = sentiment_result.reset_index(level=1,drop=True).reset_index(level=0)
sentiment_result

#### textblob sentiment analysis
from textblob import TextBlob
temp = TextBlob(cleaned_data.text_to_analyze[3])
temp.sentiment
type(temp.sentiment)
sentiment_result = pd.concat([pd.DataFrame(TextBlob(element).sentiment).T for element in cleaned_data.text_to_analyze],keys=cleaned_data.id)
sentiment_result = sentiment_result.reset_index(level=1,drop=True).rename(columns={0:"polarity",1:"subjectivity"}).reset_index(level=0)
sentiment_result

#### flair sentiment analysis
from flair.models import TextClassifier
from flair.data import Sentence
analyzer2 = TextClassifier.load('en-sentiment')
result = []
for element in cleaned_data.text_to_analyze:
    sentence = Sentence(element)
    analyzer2.predict(sentence)
    result.append(sentence.labels)
sentiment_result = pd.DataFrame(result)[0].astype(str).str.split(" ",expand=True).rename(columns={0:'label',1:'confidence'})
sentiment_result['confidence'] = sentiment_result['confidence'].str.replace(r'\(|\)',"",regex=True).astype(float)
sentiment_result
sentiment_result.describe()


#### BERTweet
import torch
from transformers import AutoModel,AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("vinai/bertweet-base", normalization=True)

line = cleaned_data.text[3]

input_ids = torch.tensor([tokenizer.encode(line)])
bertweet = AutoModel.from_pretrained("vinai/bertweet-base")

with torch.no_grad():
    features = bertweet(input_ids)
features[1]

#### openapi

# with open("./Code/twitter_credential_true.yaml", 'r') as stream:
    # OPENAI_API_KEY = yaml.safe_load(stream)['openapi_api-keys']
OPENAI_API_KEY=""
openai.api_key = os.getenv(OPENAI_API_KEY)

#### Use openapi to analytize the top-5 liked tweets
cleaned_data = pd.read_csv("./Data/cleaned_data.csv",dtype="object",sep='\t')
cleaned_data[['retweet_count','reply_count','like_count','quote_count']] = cleaned_data[['retweet_count','reply_count','like_count','quote_count']].astype(int)
text_subset = cleaned_data.loc[cleaned_data.like_count>30].sort_values('like_count',ascending=False)[['text','like_count']]
text_subset = text_subset['text']
text_to_analyze = text_subset.str.replace(r'http\S+', '',regex=True).replace(r'@\w+','',regex=True).replace(r'\n','',regex=True)
text_to_analyze = text_to_analyze.to_frame().assign(order=range(1,len(text_to_analyze)+1,1)).applymap(str)
text_to_analyze = text_to_analyze.assign(prompt = text_to_analyze.order+". \\"+text_to_analyze.text)

prompt = 'Classify the sentiment in these tweets:\n\n' +text_to_analyze.loc[:,'prompt'].iloc[0:5].str.cat(sep='\n')


openai.api_key = OPENAI_API_KEY
response = openai.Completion.create(
  engine="text-davinci-001",
  prompt=prompt,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
response
text_to_analyze.iloc[4,0]
pd.Series(response['choices'][0]['text'].split('\n'))

pd.Series(response['choices'][0]['text'].split('\n'))
