# tweet-scrape-to-db
<h3>Overview</h3>
A Python program that uses the twitter API to scrape all tweets from the past week for a given query and stores them in a local SQLite3 database.

<h3>Dependencies</h3>
 * <a href="https://github.com/tweepy/tweepy">Tweepy</a> - python library for the twitter API
 * SQLite3 - for local db storage
 * Time - to avoid crashes if twitter's api locks you out
 
<h3>Usage</h3>
Open tweet-scraper.py and fill in the consumer_key, consumer_secret, access_token and access_token_secret vars with your personal twitter dev keys. Fill in the search_term var with the query you want to search for (see <a href="https://twitter.com/search-home">Twitter Search</a> for tips on formatting a query). Finally, fill in the db_name var with the name of your local db (ex. "foobar.db"), then run.
