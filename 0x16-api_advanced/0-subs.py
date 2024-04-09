#!/usr/bin/python3
''' This script fetches a given subreddit's subscribers '''
import requests


def number_of_subscribers(subreddit):
    ''' fetches a given subreddit's subscribers '''

    headers = {"User-Agent": ("Mozilla/5.0 (X11; Linux x86_64; rv:109.0)\
            Gecko/20100101 Firefox/115.0")}
    req = requests.get('https://api.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=headers,
                       allow_redirects=False)

    if req.status_code == 200:
        req = req.json()

        return req["data"]["subscribers"]

    return 0
