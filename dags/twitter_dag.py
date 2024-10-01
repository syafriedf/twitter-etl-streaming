from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import tweepy
import psycopg2

def fetch_twitter_data():
    # Konfigurasi Twitter API
    consumer_key = 'BtVR8S9zkJVbv5IylqzHvyFSz'
    consumer_secret = 'h3SUWF85avkeXqm4IrvKPKOMygs0edduqjhF6UqWp10ST4EzuA'
    access_token = '708143202-NrOo3FnWyc2eTXPUaI4ApUaCqseDluX2VdfeuhyS'
    access_token_secret = 'wNiiycu642i8RDCjmDzJq3SDVLnNeqHhZ9YBflZswjgg5'

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    # Ambil data dari Twitter
    tweets = api.user_timeline(screen_name='twitter_username', count=10)

    # Simpan data ke PostgreSQL
    conn = psycopg2.connect("dbname='twitter_db' user='user' host='postgres' password='password'")
    cursor = conn.cursor()

    for tweet in tweets:
        cursor.execute("INSERT INTO tweets (id, text) VALUES (%s, %s)", (tweet.id, tweet.text))

    conn.commit()
    cursor.close()
    conn.close()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 1),
}

with DAG('twitter_data_dag', default_args=default_args, schedule_interval='@daily') as dag:
    fetch_data = PythonOperator(
        task_id='fetch_twitter_data',
        python_callable=fetch_twitter_data
    )
