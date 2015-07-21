import tweepy
import time
import sqlite3


def main():
    # Twitter API Information
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    search_term = ''

    # Database Setup
    db_name = ""
    conn = sqlite3.connect(db_name)
    db = conn.cursor()
    # If tweets table does not exist, create it
    db.execute('''create table if not exists tweets (content text,
                created_at datetime, tweet_id bigint, user_id bigint)''')

    api = tweepy.API(auth)

    count = 0
    c = tweepy.Cursor(api.search, q=search_term, count=100, result_type="recent",
                      include_entities=True, lang="en").items()
    while True:
        try:
            tweet = c.next()
            t = tweet.id
            print(t)
            add_tweet = 0
            for row in db.execute('SELECT * FROM tweets WHERE tweet_id=?', (t,)):
                add_tweet += 1
            if add_tweet == 0:
                # | TEXT | CREATED_AT | TWEET_ID | USER_ID |
                tweet_data = [tweet.text, tweet.created_at, tweet.id, tweet.user.id_str]
                db.execute('INSERT INTO tweets VALUES (?,?,?,?)', tweet_data)
                count += 1

        except tweepy.TweepError:
            # Twitter API boots user scraping, wait 15 minutes to begin again
            print("Waiting")
            time.sleep(60 * 15)
            continue
        except StopIteration:
            break

    conn.commit()
    print(str(count) + " Tweets recorded.")

main()