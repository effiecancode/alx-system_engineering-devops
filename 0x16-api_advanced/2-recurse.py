#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests


def add_title(hot_list, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    dict = response.json()
    hot_posts = dict['data']['children']
    add_title(hot_list, hot_posts)
    after = dict['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
