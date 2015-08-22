#!/bin/bash

clear;

echo "We will install the dependencies require to run the BOT"
if hash pip2 2>/dev/null; then
    echo ""
else
    echo "Please install pip for Python 2.7 from \'https://pypi.python.org/pypi/pip\'"
    echo "exiting"
    exit 1
fi

echo -e "Installing BeautifulSoup"
echo -e "sudo pip2 install beautifulsoup"
sudo pip2 install beautifulsoup

echo -e "Installing tweepy"
echo -e "sudo pip2 install tweepy"
sudo pip2 install tweepy

echo -e "Installation complete"
exit 0
