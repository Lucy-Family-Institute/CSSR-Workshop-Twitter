# Session 1 Notes

## Plan for Today
1. [Install Python IDE, packages](Python_IDE_Setup.md)
2. Understanding HTTP, interacting with API
3. Set up API credentials
4. Live code to pull data


## HTTP and 404

>### HTTP
![404](source/google404.webp)

>  #### What is HTTP protocol?
>  Client Request - Server Response

> #### Frequent HTTP Status Code:
> 1. Successful responses: 200(Successful)
> 2. Client error response: 401(Unauthorized), 403(Forbidden), 404(Not Found)
> 3. Server error response: 500(Internal Server Error), 503(Service Unavailable)

## Tweet Cap and Rate Limit
> 1. [Monthly Tweet Cap](https://developer.twitter.com/en/portal/dashboard)
> 2. [Rate Limit](https://developer.twitter.com/en/portal/products)

## Tweet API Basics
1. By default, the API only returns the ```id``` and the ```text``` fields.
2. Request additional fields
    - ```author_id```
    - ```context_annotations```
    - ```conversation_id```
    - ```created_at```
    - ```entities```
    - ```in_reply_to_user_id```
    - ```public_metrics```
    - ```referenced_tweets```
3. Expansions

   ![Expansions](source/Expansions.png)
4. Query
    - ```keyword```
    - ```"exact phrase match"```
    - ```#```
    - ```@```
    - ```from:	```
    - ```to:```
    - ```conversation_id:```
    - ```is:retweet```
    - ```is:quote```

  [Full Query Parameters](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query)
