#!/usr/bin/python3
"""Gets the number of subreddit subscribers"""
import requests


def number_of_subscribers(subreddit):
    """gets the total number of subs from reddit's API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url)
    if response.status_code == 404:
        return 0
    data = response.json().get('data')
    return data.get("subscribers")
