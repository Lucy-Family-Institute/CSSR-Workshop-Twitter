# Session 2 Notes

## Preparation
> By now you should be able to pull data through Twitter API
> The API send the data that includes 4 sections:
>    - **data**
>    - **includes**: has two sub-sections: referenced_tweets, referenced_users
>    - **error**
>    - **meta**
>
> The data should be consisted of 4 or 5 files:
>    - **raw_data**: pulled tweets based on the request
>    - **raw_reference_tweets**: contains tweets that have been referenced by the tweets in the **raw_data**
>    - **raw_reference_users**(optional): user information associated with the **raw_reference_tweets**
>    - **raw_errors**: error messages when pulling tweets
>    - **raw_meta**: meta data generated when pulling tweets

## Plan for Today
> 1. Load and explore data
> 2. Parse **context annotations**, **entities**
> 3. Parse **referenced_tweet**, **public metrics**
> 4. Convert **created_at**
> 5. Merge **raw_data** & **raw_reference_data**
> 6. Filter data by condition

## Context Annotations and Entities
> - Tweet context annotations offer a way to understand contextual information about the Tweet itself. Though 100% of Tweets are reviewed, due to the contents of Tweet text, only a portion are annotated.
>
> - The context annotations is derived from the analysis of a Tweet’s text and will include a domain and entity pairing which can be used to **discover Tweets on topics** that may have been previously difficult to surface. At present, there is a list of 50+ domains to categorize Tweets.
>
>
> - Entity annotations: Entities are comprised of below types. Entities are delivered as part of the entity payload section. They are programmatically assigned based on what is explicitly mentioned in the Tweet text.
>     - Person - Barack Obama, Daniel, or George W. Bush
>     - Place - Detroit, Cali, or "San Francisco, California"
>     - Product - Mountain Dew, Mozilla Firefox
>     - Organization - Chicago White Sox, IBM
>     - Other - Diabetes, Super Bowl 50
> - [More detail](https://developer.twitter.com/en/docs/twitter-api/annotations/overview)

## Explore
> Read csv file with ```pd.read_csv```
>    - ```dtype=object```, so the long id number is kept in full
>    - the default ```sep``` is comma
>
> Summarize data with:
>    - ```raw_data.describe()```
>
> Pay attention to the datatypes:
>    - ```raw_data.dtypes```
>    - Ideally, all columns should be object
>
> Glimpse the data with the first five rows
>    - ```raw_data.head()```
>    - It is often useful to check a few rows so we have an idea what the data look like
>
> Further checking by indexing
>    - ```raw_data.loc[0,"context_annotations"]```
>    - loc-indexing can be used with conditions, column name, row numbers
>    - ```raw_data.iloc[0,1]```
>    - iloc-indexing is only used for both row-number and column-number indexing
>    - Notice that one tweet can have multiple annotations. It is a better practice to parse the column ```context_annotations``` to a separate dataframe

## Parse
> **When parsing data, or any data wrangling, keep in mind what the data type is, and which type to convert to.**
>
> **In the cleaning task for tweet data, pay attention to whether it's ```str``` or ```dict``` or ```list```or ```int```.**
> #### Understanding **JSON** Data ####
>    - A common use of JSON is to exchange data to/from a web server.
>    - When receiving data from a web server, the data is always a string.
>    - use ```ast.literal_eval()``` to convert the string first
>    - ideally the converted data type should be **dict** or **list**, which can be easily flattened
>    - use ```pd.json_normalize()``` to flatten the
>
> #### Define Function ####
>    - Define function that can parse each of the entries and return the parsed data
>    - The function will process data explained above
>
> #### Vectorize Function ####
> Why we need to vectorize a function?
>    - Vectorization could simplify the code
>    - Vectorization will take array as the input instead of single entry
>    - use ```np.vectorize()```
>
> #### Apply Function to raw data ####
>    - The function returns a dataframe or multiple dataframes
>    - The associated tweet id can be used to merge with the original text
>
> #### Parse referenced_tweets, public_metrics ####
>    - The referenced_tweets can be parsed within the original data
>    - Use **regex**
>         - ```\d```:digits [0-9]
>         - ```\w```:alphanumeric [A-Za-z0-9_]
>         - ```\s```: space
>         - ```+```: one or more
>         - ```*```: zero or more
>         - ```.```: any character
>
> #### Parse created_at ####
>    - By default, twitter returns timezone-aware datetime format
>    - The timezone is set at the zone of UTC
>    - Use ```pd.to_datetime()``` to convert the string to datetime format first
>    - Then the ```datetime.dt.tz_convert('US/Eastern')``` can convert the time to US ET, the conversion is DST sensitive

### End

  ####  [Submit questions and issues here](https://github.com/Lucy-Family-Institute/CSSR-Workshop-Twitter/issues) ####
