# -*- coding: utf-8 -*-

# NLDS Lab
# Nicolas Hahn
# Search Twitter using their search API
# Take one or multiple queries
# Get recent tweets that match the query
# Put each into its own separate file in the queries folder

# go through steps to register Twitter app
# create a file called 'settings.py' and put the following 4 lines in (with your info):
# access_token          = '...'
# access_token_secret   = '...'
# consumer_key          = '...'
# consumer_secret       = '...'

from TwitterSearch import *
from settings import consumer_key, consumer_secret, access_token, access_token_secret
from getpass import getpass
import sys
import pickle
from json import dumps as jDumps
import datetime
import time
import stance_hashtags

alphaChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@'

currtime = str(datetime.datetime.now())
currtime = currtime.replace(' ','-').replace(':','-').split('.')[0]

queriesFolder = '/home/nick/TwitterSearchToDatabase/queries_for_amita'

def searchQuery(ts, query):
    query = query.lower()
    print('Searching for: '+query)
    tso = TwitterSearchOrder()
    keywords = query.split(' ')
    tso.set_keywords(keywords)
    tso.set_language('en')
    tso.set_include_entities(True)

    out_file_name = 'query-'+''.join([q for q in query if q in alphaChars])
    out_file_name += '-'+currtime
    output = open(queriesFolder+"/"+out_file_name, 'w', encoding='utf-8')

    i = 0
    for tweet in ts.search_tweets_iterable(tso):
        i += 1
        # changes single to double quotes, so json.load() works later
        jsonTweet = jDumps(tweet)
        output.write(jsonTweet+'\n')
    output.close()
    print('query "'+query+'" got '+str(i)+' tweets')

def main():

    ts = TwitterSearch(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret
        )
    
    queries = []
    all_topics = stance_hashtags.all_topics
    for topic in all_topics:
        for stance in ['FAVOR','AGAINST']:
            for hashtag in topic[stance]:
                if hashtag not in topic['extra_query']:
                    queries.append(hashtag)
                # add the topic name to the query to ensure good hits
                # if it's a generic hashtag - like #scam
                else:
                    queries.append(hashtag+' '+topic['topic'])
    
    for query in queries:
        try:
            searchQuery(ts, query)
        except TwitterSearchException as e:
            print("TwitterSearchException, rate limited, waiting ~15 mins")
            time.sleep(905)
            searchQuery(ts, query)

if __name__ == "__main__":
    main()
