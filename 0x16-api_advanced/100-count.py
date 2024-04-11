#!/usr/bin/python3
''' This module defines a function '''
import requests


def count_words(subreddit, word_list, count=0, hot_list=[], keyword_dict={}):
    ''' fetches a given subreddit's hot list and counts for given keywords '''

    headers = {"User-Agent": ("Mozilla/5.0 (X11; Linux x86_64; rv:109.0)\
            Gecko/20100101 Firefox/115.0")}
    req = requests.get('https://api.reddit.com/r/{}/hot.json'
                       .format(subreddit), headers=headers,
                       allow_redirects=False)

    if req.status_code != 200:
        return None

    req = req.json()

    hot = req["data"]["children"]

    keywords = keyword_dict
    if len(keyword_dict) == 0:
        for i in word_list:
            keywords[i] = 0

    if count == len(hot):
        for key, value in keywords.items():
            if value > 0:
                print('{}: {}'.format(key, value))
        return 0

    title = hot[count]["data"]["title"] + ' '

    for j in word_list:
        j_len = len(j) - 1
        for i in range(len(title)):
            if i + len(j) <= len(title) and\
                (title[i] == j[0] or ord(title[i]) == ord(j[0]) - 32 or
                 ord(title[i]) == ord(j[0]) + 32) and\
                    title[i + j_len] == j[-1] and\
                    title[i + j_len + 1] == ' ':

                keywords[j] = keywords[j] + 1

    hot_list.append(title)
    return count_words(subreddit, word_list, count + 1, hot_list, keywords)
