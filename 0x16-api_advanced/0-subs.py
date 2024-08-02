#!/usr/bin/python3
"""
Module to query the Reddit API and get the number of subscribers for a subreddit.
"""

import requests
import sys


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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Send GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            print(f"Error: Status code {response.status_code}")
            print(f"Response: {response.text}")
            return 0
    except requests.RequestException as e:
        # Handle any request exceptions
        print(f"Error: {e}")
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
