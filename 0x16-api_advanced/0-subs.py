#!/usr/bin/python3
"""
Module to query the Reddit API and get the number of subscribers for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid.
    """
    # Set up the API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "linux:my_reddit_client:v1.0 (by /u/your_username)"
    }

    try:
        # Send GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If not successful (including redirects), return 0
            return 0
    except requests.RequestException:
        # Handle any request exceptions
        return 0
