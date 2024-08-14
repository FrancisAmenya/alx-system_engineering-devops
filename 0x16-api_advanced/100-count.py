#!/usr/bin/python3
"""
Working on a word counter
"""
import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries the Reddit API and counts
    occurrences of specified keywords
    in the titles of hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        counts (dict): Accumulator for word counts (default None).
        after (str): Pagination cursor (default None).
    """
    if counts is None:
        counts = defaultdict(int)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {'User-Agent': 'MyRedditApp/0.1 by YourUsername'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']

        # Count keywords in titles
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                # Create a regex pattern to match the word
                pattern = r'\b' + re.escape(word.lower()) + r'\b'
                counts[word.lower()] += len(re.findall(pattern, title))

        # Check for more posts
        if data['after']:
            return count_words(subreddit, word_list, counts, data['after'])
        else:
            # Print results
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word} {count}")
    else:
        return
