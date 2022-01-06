# CSSR-Workshop-Twitter

This is the introduction for the Workshop offered by Lucy Family Institute-CSSR.

The workshop introduces a series of handy projects on how to collect data from twitter, parse tweets and apply basic NLP(Natural Language Processing) analysis.

Before any proceedings to work on codes and twitter data analysis, please refer to [Developer_Account](https://github.com/Lucy-Family-Institute/CSSR-Workshop-Twitter/blob/master/Developer_Account.md) for the info of application. It is strongly recommended you to apply as soon as you sign up the workshop. The application can take days or weeks to be approved, and twitter might require further explanation after reviewing the initial application.

At the same time, you can refer to the [Python_IDE_Setup](https://github.com/Lucy-Family-Institute/CSSR-Workshop-Twitter/blob/master/Python_IDE_Setup.md) to install the required apps.

Once you have the twitter developer account and Python IDE set up on your computer. You will be able to pull data from twitter.

The workshop is planned with three sessions.

### Session 1: Set up and twitter data pull

Examples of pulling data from twitter:

1. Timeline from certain accounts
2. The tweets a certain user liked
3. Tweets contain a certain hashtag and/or multiple hashtags
4. Search tweets by a set of conditions(optional)

For those who are interested in the advanced techinics, there is code to show how to pull data and save it locally at the same time, this is espercially useful when the size of the pulled data is huge.


### Session 2: Parse twitter data

The raw data that the twitter API returned shall be converted to json format first, then it will be preferably converted to a dataframe for the subsequent analysis. The session 2 will show how-to. This requires some basic knowledge about data format about json, dict, list.

Here is an [example](https://www.w3schools.com/python/python_datatypes.asp) to illustrate different data types in python. The data types we will need to deal with in this workshop are: str, int, float, list, tuple, dict, set and bool.

JSON data is a data type widely used for data exchange. Please read the [Intro](https://www.w3schools.com/js/js_json_intro.asp) and [JSON Parse](https://www.w3schools.com/js/js_json_intro.asp). This will help us perceive the twitter data parsing.

Besides, we will also use two basic control flows in programming. It is helpful if you know the control flows in programming, but if not, [here](https://docs.python.org/3/tutorial/controlflow.html) is a good intro on that. We will mostly use condition(*if...else...*) and loop(*for loop*) control.


### Session 3: NLP Analysis
