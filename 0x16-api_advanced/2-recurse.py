#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """queries the Reddit API and gets a lits of titles of all hot
    articles for a given subreddit"""
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}
    params = {'limit': 100}
    if after is not None:
        params['after'] = after

    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        posts = res.json().get('data', {}).get('children', [])
        if not posts:
            return hot_list
        [hot_list.append(post['data']['title']) for post in posts]
        new_after = res.json().get('data', {}).get('after')
        return recurse(subreddit, hot_list, new_after)
    else:
        return None
