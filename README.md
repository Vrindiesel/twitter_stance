# twitter_stance
Twitter Crawler for NLDS lab stance tasks



If the IAC database is not set up for twitter, run `sql_scripts/twitterStructure.sql` to add the necessary tables. Also make sure that the topics you are adding are in the topics table.

Don't run `nukeTwitter.sql` unless you want all the Twitter data gone forever.

# To set up your machine to get new raw data for existing topics, hashtags and upload them to IAC database:
  1. Add the IAC password to `getAndUploadStanceTweets.sh` where it says 'IAC PASSWORD GOES HERE'
  2. Change path names if necessary, same for `searchTwitterCL_stance.py` (line 32) and `listJSONtoMySQL_stance.py` (line 28)
  3. Run `getAndUploadStanceTweets.sh`

# To add new hashtags for the same topics:
  1. Find the topic in `stance_hashtags.py` and add it to the `'FAVOR'` or `'AGAINST'` lists
    - This will cause `searchTwitterCL_stance.py` to generate a file with the hashtag in the filename
  2. Add another pattern in `getAndUploadStanceTweets.sh` if one of the current ones will not match with this filename to move this file to the appropriate topic folder in `queries_for_amita`
  3. Run `getAndUploadStanceTweets.sh`

# To add a new topic:
  1. Add another object to `stance_hashtags.py` using the old topics as a template, also add the new topic name to the list at the bottom, `all_topics`
  2. Add the proper `mv` lines to getAndUploadStanceTweets.sh
  3. Add another folder to `queries_for_amita` with the topic name
  4. Add the topic folder and database `topic_id` to `listJSONtoMySQL_stance.py` 
    - TODO: have this script use stance_hashtags so this part is automatically updated
  5. Run `getAndUploadStanceTweets.sh`
  
# To generate CSV files from Twitter data in the server:
  1. Add IAC password to `write_stance_tweets_csv.sh`
  2. Ensure settings in `write_stance_tweets_csv_config.ini` are correct
  3. Make sure path at line 37 is where you want the csvs to go
  4. Make sure all topics you want generated are in `topics_to_process` on line 303
  5. Run `write_stance_tweets_csv.sh`
