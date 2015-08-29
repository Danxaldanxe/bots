#!/usr/bin/env python3

import tweepy
from creds import consumer_key, consumer_secret, access_token, access_token_secret
from random import sample
from time import sleep

# --- get terms --- #
selector_terms = set(map(lambda x: x.strip('\n'), open('terms.txt','r').readlines()))

# --- set up API --- #
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# --- search for tweets containing a random selector term --- #
def retweet_selector(selector):
    # grab a tweet containing this term
    tweet = api.search(q=selector, lang='en').pop()
    while not selector in tweet.text:
        # basically enforces same case
        tweet = api.search(q=selector, lang='en').pop()
    print('Retweeting', '\"' + tweet.text + '\" from user', tweet.user.screen_name,
          'because it contains selector term:', selector)
    # retweet it
    api.retweet(tweet.id)

# --- main etc ? --- #
while True:
    selector = sample(selector_terms, 1)[0]
    retweet_selector(selector)
    sleep(15*60)

