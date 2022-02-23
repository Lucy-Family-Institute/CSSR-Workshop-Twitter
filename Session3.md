# Session 3

## Preparation
> After session 2, you should have the data as below:
>    - cleaned_data.csv
>    - context_data.csv
>    - annotations_data.csv
>    - hashtags_data.csv
>    - mentions_data.csv

## Plan for Today
> 1. Named Entity Recognition and Descriptive analysis
> 2. Sentiment analysis

## Named Entity Recognition(NER)
> **What is NER?**
>    - Named entity recognition is a natural language processing technique that can automatically scan entire articles and pull out some fundamental entities in a text and classify them into predefined categories.
>
> **Other NER tools:**
>    - [nltk](https://www.nltk.org/)
>    - [spaCy](https://spacy.io/usage)
>

## Context Annotations and Entities
> **What are context annotations and entities?**
> - Tweet context annotations offer a way to understand contextual information about the Tweet itself. Though 100% of Tweets are reviewed, due to the contents of Tweet text, only a portion are annotated.
>
> - The context annotations is derived from the analysis of a Tweet’s text and will include a domain and entity pairing which can be used to **discover Tweets on topics** that may have been previously difficult to surface. At present, there is a list of 50+ domains to categorize Tweets.
>
> - Entity annotations: Entities are comprised of below types. Entities are delivered as part of the entity payload section. They are programmatically assigned based on what is explicitly mentioned in the Tweet text.
>     - Person - Barack Obama, Daniel, or George W. Bush
>     - Place - Detroit, Cali, or "San Francisco, California"
>     - Product - Mountain Dew, Mozilla Firefox
>     - Organization - Chicago White Sox, IBM
>     - Other - Diabetes, Super Bowl 50
> - [More detail](https://developer.twitter.com/en/docs/twitter-api/annotations/overview)
>

## Descriptive Analysis
> **What we can extract from the context annotations and entities data?**
> - ```context_data``` can tell which domain(s) the associated tweet is in. Such as _Politics_ or _Sports_.
> - ```entities``` can tell what entities appear in the tweet(s)
> - Use ```value_counts``` to get those frequently mentioned entities
> - Join multiple entities by ```tweet_id```, to piece together what entities each tweet has
> - Join the hashtags or mentions for each tweet
> - Counts the frequency of hashtags and mentions
>
## Sentiment Analysis
> **What is sentiment analysis?**
>    - Identify, extract, quantify, and study affective states and subjective information.
>
> **Rule-based Model**
>    - A set of rules based on which the text is labeled as positive/negative/neutral
>    - Packages:
>         - nltk-SentimentIntensityAnalyzer
>         - TextBlob
>    - [VADER Compound Score](https://github.com/cjhutto/vaderSentiment#about-the-scoring) range: [-1~1]
>    -[TextBlob Score](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis) range: polarity[-1.0,1.0], subjectivity[0.0,1.0]
>
> **Pretrained Neural Network**
>    - The model is trained with real data.
>         - flair
>
> **Commercialized Model**
>    - [Openapi](https://beta.openai.com/examples/default-adv-tweet-classifier)
>
> **Train the Model in Specific Domain**
>    - [BERT](https://github.com/baotramduong/Twitter-Sentiment-Analysis-with-Deep-Learning-using-BERT/blob/main/Notebook.ipynb)
>    - [BERTweet](https://github.com/VinAIResearch/BERTweet)
>    - [Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/4)
>    - [Coding Example](https://www.kaggle.com/aquib5559/1-6million-tweet-sentiment-analysis-using-bert/notebook)
>
## Wrap Up
> Project Breakdown
>    - Data Collection
>    - Data Clean and Preparation
>    - Data Analysis and Modeling
>

```mermaid
flowchart TD
    A[Data Collection] --> B(Data Clean and Preparation);
    B --> Data Analysis and Modeling;
```
