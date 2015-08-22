#!/usr/bin/env python2

# import dependencies
import tweepy, time
import urllib2
from bs4 import BeautifulSoup as bs

# Get Tweeter key and secret from Config File
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# CONSTANTS
website = "http://www.boootube.com"
yt_url = "https://www.youtube.com/watch?v="

# Tweeter Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Handling URL
o = urllib2.build_opener()
o.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")]
html = o.open(website)

i = 1

while 1:
    soup = bs(html)
    
    # Find all youtube links
    for link in soup.find_all('a'):
        temp_link = link.get('href')
        if temp_link[0] is '#':
            Y_link = yt_url + temp_link[1:]
            api.update_status(status = Y_link)
            # sleep for 24 hours
            time.sleep(86400)
    # Go to next page
    html = o.open(website + '/?p=' + str(i))
    i += 1
    if i == 65:
        break
