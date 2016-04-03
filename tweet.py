#!/usr/bin/python
#tweet.py script can be used as command in linux
from twitter import*
import tweepy
import sys
#add individual tokens
access_token=''
access_token_secret=''
consumer_key=''
consumer_secret=''
status=raw_input('What do you want to tweet?\n')
#status will get the string.
if (len(status) < (140)):
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    api.update_status(status)
    print "Sucessfuly Tweeted: "+status
else:
    print "try again tweet is to long"
