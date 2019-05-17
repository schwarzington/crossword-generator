#!/usr/bin/python

import string
import re
import requests 
import os
import sys
import random
import numpy
import mechanize
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
  
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.get('https://www.wordplays.com/crossword-clues')
answer_input = browser.find_element_by_id("answer")
answer_input.send_keys("BASEBALL")
browser.find_element_by_id("search").click()
soup_level1=BeautifulSoup(browser.page_source, 'lxml')
test = [re.sub("\(\d.*\)", "", td.find('a').text.encode('utf-8')).strip() for td in soup_level1.find_all("td", class_="clue")]
print(test)

				



		
				
				
