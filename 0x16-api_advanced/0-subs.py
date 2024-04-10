#!/usr/bin/python3
"""Gets the number of subreddit subscribers"""
import requests


def number_of_subscribers(subreddit):
    """gets the total number of subs from reddit's API"""
    if not subreddit or type(subreddit) is not str:
        return 0
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_res = response.json
    else:
        return 0
    return json_res.get('data', {}).get("subscribers")
