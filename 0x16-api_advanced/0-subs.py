#!/usr/bin/python3
"""Gets the number of subreddit subscribers"""
import requests


def number_of_subscribers(subreddit):
    """gets the total number of subs from reddit's API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent':'0x16-api_advanced:project:v1.0.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    data = response.json().get('data')
    return data.get("subscribers")
