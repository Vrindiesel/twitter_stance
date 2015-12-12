# Nicolas Hahn
# NLDS Lab
# get stance tweets from database
# write each to a CSV, two for each topic (for, against)
# each tweet line:
# tweet_id, topic, stance, hashtag, text

import sys
import re
import os
import csv
import math
import difflib
import configparser
import random
import datetime
import enchant
from collections import defaultdict
import oursql
import sqlalchemy as s
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.dialects import mysql
from sqlalchemy import func
# file where hashtags and topics are stored
import stance_hashtags

###########
# Globals #
###########

# twitter dataset = 7
dataset_id = 7
# timestamp in format that is filename friendly
currtime = str(datetime.datetime.now())
currtime = currtime.replace(' ','-').replace(':','-').split('.')[0]
csv_dir = './stance_hashtag_csvs/'
# file with random tweet text, 1 per line
# random_tweet_file = "/home/nick/TwitterSearchToDatabase/random_tweets/random-20k.tweet"
# which filters we want to apply
config = None
# list of all topic objects with for/against hashtags + mysql db topic_id
all_topics = stance_hashtags.all_topics    

Tweet = None
Text = None
Hashtag_Relation = None
Hashtag = None

###############
# Match Class #
###############

class Match:
    def __init__(self, 
        tweet_id=None,
        topic=None,
        fullname=None,
        stance=None,
        hashtag=None, 
        text=None):
        self.tweet_id = tweet_id
        self.topic = topic
        self.fullname = fullname
        self.stance = stance
        self.hashtag = hashtag
        self.text = text
    
    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

#############################
# Database connection/setup #
#############################

# open connection to database
# then return engine object
def connect(username, password, database):
    db_uri = 'mysql+oursql://{}:{}@{}'.format(username, password, database)
    # db_uri = 'mysql://{}:{}@{}'.format(username, password, database)
    engine = s.create_engine(db_uri, encoding='utf-8')
    engine.connect()
    return engine

# create a session from the engine
def createSession(eng):
    Session = s.orm.sessionmaker()
    Session.configure(bind=eng)
    session = Session()
    return session

# creates a table class for each table used
def generateTableClasses(eng):
    ABase = automap_base()
    ABase.prepare(eng, reflect=True)
    global Tweet, Text, Hashtag_Relation, Hashtag
    Tweet = ABase.classes.tweets
    Text = ABase.classes.texts
    Hashtag_Relation = ABase.classes.hashtag_relations
    Hashtag = ABase.classes.hashtags
    

#####################
# General functions #
#####################

def cleanText(text):
    """lowercase, rm newlines and double quotes"""
    if text != None:
        newtext = text.lower().replace('\n',' ')
        newtext = newtext.replace('"',"'")
        return newtext

def getTweetIdsFromHashtag(hashtag, session):
    """return list of tweet ids which contain a given hashtag"""
    # database stores upper, lowercase hashtags separately (#Atheism vs #atheism)
    hashtag_text = hashtag.replace('#','').lower()
    tweet_ids = []
    hquery = session.query(Tweet, Hashtag_Relation, Hashtag).\
                filter((Tweet.dataset_id==dataset_id) &
                    (Hashtag_Relation.tweet_id==Tweet.tweet_id) &
                    (Hashtag_Relation.hashtag_id==Hashtag.hashtag_id) &
                    (func.lower(Hashtag.hashtag_text)==func.lower(hashtag_text)))
    for t,_,_ in hquery.all():
        tweet_ids.append(t.tweet_id)
    return tweet_ids

def getHashtagMatches(hashtag, topic, fullname, stance, session):
    """query the db for all tweets that match a hashtag"""
    tweet_ids = getTweetIdsFromHashtag(hashtag,session)
    print("Got",len(tweet_ids),"from hashtag",hashtag)
    # because query with >50000 or so items breaks mysql
    chunk_size = 10000
    tweet_chunks = [tweet_ids[x:x+chunk_size] for x in range(0, len(tweet_ids), chunk_size)]
    batch_matches = []
    for chunk in tweet_chunks:
        tquery = session.query(Tweet, Text).\
                    filter((Tweet.dataset_id==dataset_id) &
                        (Text.dataset_id==dataset_id) & 
                        (Tweet.text_id==Text.text_id) &
                        (Tweet.tweet_id.in_(chunk)))
        for tweet_obj,text_obj in tquery.all():
            batch_matches.append(Match(
                tweet_id=tweet_obj.tweet_id,
                topic=topic,
                fullname=fullname,
                stance=stance,
                hashtag=hashtag,
                text=cleanText(text_obj.text)))
    filtered_matches = filterHashtagMatches(batch_matches)
    return filtered_matches

def hasXDictionaryWords(matches, num_words):
    """after normalization, ensure at least X dictionary words"""
    spell_dict = enchant.Dict('en_us')
    filtered_matches = []
    for match in matches:
        match_ct = 0
        for token in match.text.split():
            if spell_dict.check(token):
                match_ct += 1
            if match_ct >= num_words:
                filtered_matches.append(match)
    return filtered_matches

def removeDuplicateTweets(matches, cutoff):
    """removes tweets that are highly similar to another"""
    print('len of matches before remove dupes',len(matches))
    no_dupe_matches = matches
    raw_match_tuples = []
    for match in no_dupe_matches:
        match_tokens = set([m.lower() for m in match.text.split() if m[0][0] != '#'])
        raw_match_tuples.append((match,match_tokens))
    match_tuples = sorted(raw_match_tuples, key=lambda x: x[0].text)
    filtered_matches = []
    token_sets = []
    for mtuple in match_tuples:
        dupe = False
        for tset in token_sets:
            largest_set_size = len(mtuple[1]) if len(mtuple[1]) > len(tset) else len(tset)
            if len(tset & mtuple[1]) / largest_set_size >= cutoff:
                dupe = True
                break
        if not dupe: 
            filtered_matches.append(mtuple[0])
            token_sets.append(mtuple[1])
    return filtered_matches
    

def removeOffTopicHashtags(matches):
    """for hashtags like '#hoax' make sure 'climate' is also in the tweet somewhere"""
    filtered_matches = []
    hashtag_topics = {}
    for topic in all_topics:
        for hashtag in topic['extra_query']:
            hashtag_topics[hashtag.lower()] = topic['topic']
    for match in matches:
        if match.hashtag.lower() in hashtag_topics:
            if hashtag_topics[match.hashtag.lower()].lower() in match.text.lower().split():
                filtered_matches.append(match)
        else:
            filtered_matches.append(match)
    return filtered_matches

def removeAmbiguousHashtags(matches):
    """remove tweets that have both for and against hashtags"""
    filtered_matches = []
    for match in matches:
        opposite = 'FAVOR' if match.stance == 'AGAINST' else 'AGAINST'
        opp_hashtags = [t for t in all_topics if t['topic'] == match.topic][0][opposite]
        for token in [t for t in match.text.split() if t[0] == '#']:
            if token not in opp_hashtags:
                filtered_matches.append(match)
    return filtered_matches

def filterHashtagMatches(matches):
    """ 
    Ensure that each tweet conforms to the following:
    - remove tweets with urls / pictures (string match 'http'?)
    - need at least X dictionary words
    - at least X total words
    - remove tweets with both for and against hashtags
    - remove duplicate tweets (X% tokens identical) 
    """
    remove_urls = config.get('filters','remove_urls')
    min_dict_words = config.get('filters','min_dict_words')
    min_total_words = config.get('filters','min_total_words')
    if remove_urls != 'disabled':
        matches = [m for m in matches if 'http' not in m.text]
    if min_dict_words != 'disabled':
        matches = hasXDictionaryWords(matches,int(min_dict_words))    
    if min_total_words != 'disabled':
        matches = [m for m in matches if len(m.text.split()) >= int(min_total_words)] 
    
    matches = removeOffTopicHashtags(matches)
    matches = removeAmbiguousHashtags(matches)
    return matches

# def createRandomTweetObjects(random_tweet_file):
#     """create match objects from file with tweets on each line"""
#     print('getting random tweets')
#     random_tweet_texts = []
#     with open(random_tweet_file,'r') as rfile:
#         random_tweet_texts = [line.strip() for line in rfile.readlines()]
#     random_matches = []
#     for rtweet in random_tweet_texts:
#         random_matches.append(Match(
#             tweet_id=0,
#             topic='random',
#             fullname='Random Tweets',
#             stance='n/a',
#             hashtag='n/a',
#             text=rtweet))
#     return random_matches
# 
# 
# def generateRandomCSV(random_tweet_file):
#     """standalone function for generating random tweet csv"""
#     random_file = csv_dir+'random_tweets.csv'
#     random_tweets = createRandomTweetObjects(random_tweet_file)
#     print(len(random_tweets))
#     writeToCSV(random_tweets, random_file, -1)
#     print('finished writing random tweet csv')


def writeToCSV(matches, write_file, max_tweets):
    """
    write each tweet object to a line in the csv
    if unnecessary to have a limit on number of tweets, set max_tweets = -1
    """
    if max_tweets == -1:
        max_tweets = len(matches)
    print("Writing",max_tweets,"tweets to csv file for topic",matches[0].topic,"with stance:",matches[0].stance)
    with open(write_file,'w') as csv_file:
        csv_file.write('"ID","Target","Stance","Hashtag","Tweet"\n')
        for m in matches[:max_tweets]:
            line = ''
            for field in [m.tweet_id,m.fullname,m.stance,m.hashtag,m.text]:
                line += '"'+str(field)+'",'
            csv_file.write(line[:-1]+'\n')
        

##################
# Main Execution #
##################

def main(user=sys.argv[1],pword=sys.argv[2],db=sys.argv[3]):
    
    # usual stuff to sync with MySQL db, setup
    print('Connecting to database',db,'as user',user)
    sys.stdout.flush()
    matches = []
    global config
    config = configparser.ConfigParser()
    config.read('write_stance_tweets_csv_config.ini')
    remove_duplicate_ratio = float(config.get('filters','remove_duplicate_ratio'))    
    csv_subdirectory = csv_dir+"stance_nostance"+currtime+"/"
    os.mkdir(csv_subdirectory)
    random_tweets = createRandomTweetObjects(random_tweet_file)
     
    # dict of all the final tweets so we can build a nostance csv too
    every_final_tweet = {}
    topics_to_process = [
                        'abortion',
                        'atheism',
                        'climate',
                        'hillary',
                        'feminism'
                        ]
    
    # create stance csvs first for each topic
    # for topic in all_topics:
    for topic in [t for t in all_topics if t['topic'] in topics_to_process]:
        
        eng = connect(user, pword, db)
        metadata = s.MetaData(bind=eng)
        session = createSession(eng)
        generateTableClasses(eng)
        
        # get stance data
        topic_name = topic['topic']
        fullname = topic['fullname']
        print('creating stance data csv for topic',topic_name)
        for_tweets = []
        against_tweets = []
        
        # every_final_tweet[topic_name] = {}
        for hashtag in topic['FAVOR']:
            for_tweets += getHashtagMatches(hashtag,topic_name,fullname,'FAVOR',session)
        for hashtag in topic['AGAINST']:
            against_tweets += getHashtagMatches(hashtag,topic_name,fullname,'AGAINST',session)
        for_tweets = removeDuplicateTweets(for_tweets, remove_duplicate_ratio) 
        for_write_file = csv_subdirectory+"favor_"+topic_name+"_"+currtime+".csv"
        writeToCSV(for_tweets, for_write_file, -1)
        against_tweets = removeDuplicateTweets(against_tweets, remove_duplicate_ratio) 
        against_write_file = csv_subdirectory+"against_"+topic_name+"_"+currtime+".csv"
        writeToCSV(against_tweets, against_write_file, -1)
        session.close()
    
if __name__ == "__main__":
    main()

