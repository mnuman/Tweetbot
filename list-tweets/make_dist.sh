#!/bin/bash
cd lib/python3.6/site-packages
zip -r9 ~/list-tweets.zip *
cd -
zip -g ~/list-tweets.zip list.py
