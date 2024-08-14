#!/usr/bin/python3

"""
0-subs
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'mannedstats'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        print(f"Er: code {response.status_code},subreddit '{subreddit}'")
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))
