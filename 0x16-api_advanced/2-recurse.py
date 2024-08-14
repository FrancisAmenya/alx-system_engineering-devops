#!/usr/bin/python3
"""
Working on  a hot list
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list
    of titles of all hot articles
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to accumulate the titles
   (default empty list).

    Returns:
        list or None: A list of titles if found, otherwise None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'jvstblvck'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there is a next set of posts
        if data['after']:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
