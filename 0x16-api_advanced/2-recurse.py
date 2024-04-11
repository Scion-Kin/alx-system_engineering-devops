#!/usr/bin/python3
''' This script fetches a reddit hot list '''
import requests


def recurse(subreddit, hot_list=[], count=0):
    ''' fetches a given subreddit's hot list '''

    headers = {"User-Agent": ("Mozilla/5.0 (X11; Linux x86_64; rv:109.0)\
            Gecko/20100101 Firefox/115.0")}
    req = requests.get('https://api.reddit.com/r/{}/hot.json'
                       .format(subreddit), headers=headers,
                       allow_redirects=False)

    if req.status_code != 200:
        return None

    req = req.json()

    hot = req["data"]["children"]

    if count == len(hot):
        return hot_list

    hot_list.append(hot[count]["data"]["title"])
    return recurse(subreddit, hot_list, count + 1)
