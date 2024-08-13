import requests
import time

def make_api_request(url, params, headers=None, retries=3):
    """Makes an API request and handles retries."""
    for _ in range(retries):
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            time.sleep(1)
    return None

def parse_tweet_data(tweet_json):
    """Parses tweet JSON data to extract relevant information."""
    return {
        'tweet_id': tweet_json.get('id_str'),
        'user_id': tweet_json.get('user', {}).get('id_str'),
        'text': tweet_json.get('text'),
        'created_at': tweet_json.get('created_at'),
        'retweet_count': tweet_json.get('retweet_count'),
        'favorite_count': tweet_json.get('favorite_count')
    }

def handle_rate_limit(response):
    """Handles Twitter API rate limits by sleeping for the required time."""
    if response.status_code == 429:
        reset_time = int(response.headers.get('x-rate-limit-reset'))
        sleep_time = max(reset_time - int(time.time()), 0)
        time.sleep(sleep_time)