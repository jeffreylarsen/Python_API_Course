# import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import selenium
from splinter import Browser
from selenium import webdriver
import json
import numpy as np
import requests as r
import re

def create_json():
    # create a path to chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    # create a variable for the url
    url = 'https://en.wikipedia.org/wiki/Special:Random'

    story_dict = {}
    # find new webpage
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    editor_list = ['','JL', 'jl', 'TL', 'tl' ,'IT']
    segment_list =  ['VO', 'PKG', 'SOTVO', 'TZ']

    #gather webpage info
    slug = soup.find_all('h1', class_='firstHeading')[0].text
    segment = np.random.choice(segment_list)
    editor = np.random.choice(editor_list)
    source = 'Wikipedia'
    script = soup.find_all(['div'], class_='mw-body-content mw-content-ltr')[0].text

    story_dict["page_number"] = ''
    story_dict["slug"] = slug
    story_dict["segment"] = segment
    story_dict["writer"] = 'Ghost'
    story_dict["editor"] = editor
    story_dict["source"] = source
    story_dict["script"] = r"{}".format(script).replace('\\','')
    story_dict["mos_objects"] = ''
    story_dict["show_id"] = 6

    return json.dumps(story_dict)

def post_stories():
    token = r.post(
        "https://www.jeffreylarsen.pro/login",
        data= {
            "username": "dustyish@gmail.com",
            "password": "dustie1"
        }) \
        .json()['access_token']
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }
    story_list = [create_json() for i in range(50)]
    
    for story in story_list:
        print(story)
        r.post(
            "https://www.jeffreylarsen.pro/stories/",
            headers = headers,
            data = story
        )

post_stories()