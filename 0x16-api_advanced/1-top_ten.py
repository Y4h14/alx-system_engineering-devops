#!/usr/bin/python3
"""defines a function accessing reddit API"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    params = {'limit': 10}

    response = requests.get(url, params=params)
    if response.status_code == 404:
        print('None')
        return
    data = response.json().get('data')
    for i in data.get("children"):
        print(i.get("data").get("title"))
