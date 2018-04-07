# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 10:16:23 2018 by Apoorva Karn """
import tweepy #https://github.com/tweepy/tweepy
import csv
import json
#Twitter API credentials
consumer_key = "q0oABjJFqZYoygv6Wsd5cPPj5"
consumer_secret = "xyITW0kVELunEUk2ujnnDHJoHDLPoZ4DdvaD92hszw8mSfBMM5"
access_key = "781866509236776960-cYpIkUA5PA8QJCGu7rTGP3nlOs9avyB"
access_secret = "gU4ktkFdSCjoQk3PV563ixYH1lWqgtLXawTz6U6JqHPax"


def get_all_tweets(screen_name):
    f = open('paytmtweet.csv', 'w',newline='')    
    writer = csv.writer(f)
    writer.writerow(["id","created_at","text"])
    
    
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []  

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.search(q= screen_name,count=100)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    count = 0
    #keep grabbing tweets until there are no tweets left to grab
    while( len(new_tweets) >0 and count <4):
        print( "getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.search(q = screen_name,count=100,max_id=oldest)
       
        count = count + 1
        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print ("...%s tweets downloaded so far" % (len(alltweets)))
   
    #form the tweepy tweets into a 2D array that will populate the csv
    
   # outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    for tweet in alltweets :
        outtweets = [tweet.id, tweet.created_at, tweet.text.encode("utf-8")]
        #print (outtweets)           
        writer.writerows([outtweets])
       # print(outtweets)
        
    file = open('tweet.json', 'w') 
    print ("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print ( "Done")
    file.close()
    
    '''
    with open('tweet1.json', 'w', encoding='utf8') as file:
        for status in alltweets:
         json.dump(status._json,file,sort_keys = True,indent = 4)
    pass
    '''
    
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@Paytm -filter:retweets")
    


