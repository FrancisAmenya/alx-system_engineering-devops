#!/usr/bin/python3
"""
1-top_ten
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'jvstblvck'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    (top_ten(argv[1]))
