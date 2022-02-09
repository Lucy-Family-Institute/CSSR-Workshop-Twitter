# CSSR-Workshop-Twitter
Author: Yang Xu(yxu6@nd.edu)

## IMPORTANT INFORMATION

The twitter developer account is a must-have for this workshop. To apply for a developer account, you need to have a regular twitter account. It is assumed you already have one. You will need to receive approval of a developer account before any proceedings to work on codes and twitter data analysis.

Please refer to [Developer_Account](https://github.com/Lucy-Family-Institute/CSSR-Workshop-Twitter/blob/master/Developer_Account.md) for the info of application. It is **strongly recommended** to apply as soon as you sign up the workshop. The application can take days or weeks to be approved, and twitter might require further explanation after reviewing the initial application.

## Overview

This is the introduction of the Workshop offered by Lucy Family Institute-CSSR.

Twitter is a social media where people share news, attitudes and immediate reactions to social events. Twitter offers an API to researchers to collect data. The API allows users to define their own conditions for data retrieval, such as keywords, date range, is retweet or not, reply or mention a certain user etc.

The workshop introduces a series of hands-on projects on how to collect data from twitter, parse tweets and apply basic NLP(Natural Language Processing) analysis.

Participants will learn:
1. How to set up code and pull data through twitter API, save data locally. (Feb.9)
2. Wrangle and clean the raw data. (Feb.16)
3. Apply NLP(Natural Language Processing) model, such as sentiment analysis. (Feb.23)

## Prior Knowledge

The workshop assumes the working knowledge of Python. There are links to some useful Python basics below.

## Software Details

Make sure the Python3(recommended version 3.7 or later) and IDE(recommended Jupyter) are installed.

You can refer to the [Python_IDE_Setup](https://github.com/Lucy-Family-Institute/CSSR-Workshop-Twitter/blob/master/Python_IDE_Setup.md) to install the required apps.

The packages this workshop will use are:
1. tweepy
2. pandas

You can install them through pip3 or conda. We can include this in the first session of the workshop.

Once you have the twitter developer account and Python IDE set up on your computer. You are ready to pull data from twitter.

## Workshop Plan and Dates

The workshop is planned to spread out over three weeks with 1.5 hours sessions each week. Each workshop will cover a brief introduction, go through a few live demos. The instructor will answer questions and help with the bugs.

### Course Dates:

1. Session 1: Wednesday, 3:30-5pm Feb.9 CDS Classroom 246
2. Session 2: Wednesday, 3:30-5pm Feb.16 CDS Classroom 125
3. Session 3: Wednesday, 3:30-5pm Feb.23 CDS Classroom 246

### Session 1: Set up and twitter data pull

Examples of pulling data from twitter:

1. Timeline from certain accounts
2. The tweets a certain user liked
3. Tweets contain a certain hashtag or multiple hashtags
4. Search tweets by a set of conditions(time-permitting)

For those who are interested in the advanced techniques, there is code to show how to pull data and save it locally at the same time, this is especially useful when the size of the pulled data is huge.

### Session 2: Parse twitter data

The raw data that the twitter API returned shall be converted to json format first, then it will be preferably converted to a dataframe for the subsequent analysis. The session 2 will show how-to. This requires some basic knowledge about data format, such as: json, dict, list.

Here is an [example](https://www.w3schools.com/python/python_datatypes.asp) to illustrate different data types in python. The data types we will need to deal with in this workshop are: str, int, float, list, tuple, dict, set and bool.

JSON data is a data type widely used for data exchange. Please read the [Intro](https://www.w3schools.com/js/js_json_intro.asp) and [JSON Parse](https://www.w3schools.com/js/js_json_intro.asp). This will help us perceive the twitter data parsing.

Besides, we will also use two basic control flows in programming. It is helpful if you know the control flows in programming, but if not, [here](https://docs.python.org/3/tutorial/controlflow.html) is a good intro on that. We will mostly use condition(*if...else...*) and loop(*for loop*) control.

### Session 3: NLP Analysis

Tweets often come with the real-time reactions to social events. Thus, the tweets we obtained carries many information. One of most common cases is sentiment analysis, which will rate each tweet whether it's positive/native to a certain topic.

The workshop will introduce a few NLP models for such task. Besides that, it is often useful to wrangle the data before analysis. E.g. single out links from the text body. The package **pandas** will be very powerful for data cleaning.

## Course Attendance and Delivery

To make sure the workshop meets its expectation, registration is required with a maxium capacity of 15.

The workshop is voluntary, but each session builds off of the previous session and so if missing any session you might need to catch-up on your own.

The workshop will be completely in person. All materials will be shared via Github.
