#!/usr/bin/python3
''' This script fetches a reddit hot list '''
import requests


def top_ten(subreddit):
    ''' fetches a given subreddit's subscribers '''

    headers = {"User-Agent": ("Mozilla/5.0 (X11; Linux x86_64; rv:109.0)\
            Gecko/20100101 Firefox/115.0")}
    req = requests.get('https://api.reddit.com/r/{}/hot.json'
                       .format(subreddit), headers=headers,
                       allow_redirects=False)

    if req.status_code == 200:
        req = req.json()

        hot_list = req["data"]["children"]

        for i in range(10):
            print('{}'.format(hot_list[i]["data"]["title"]))

    else:
        print("None")
