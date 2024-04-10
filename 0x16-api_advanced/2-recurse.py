#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """queries the Reddit API and gets a lits of titles of all hot
    articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
               }
    params = {'after': after,
              'count': count,
              'limit': 100}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for i in data.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after, count)
