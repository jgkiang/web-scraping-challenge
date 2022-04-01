#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


    url = 'http://redplanetscience.com/'
    browser.visit(url)


# In[4]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find_all('div', class_='content_title')
    news_p = soup.find_all('div', class_='article_teaser_body')
    print("Title: ",news_title)
    print("Paragraph: ",news_p)


# In[5]:


    url = 'http://spaceimages-mars.com/'
    browser.visit(url)


# In[6]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = url + featured_image
    print("Featured Image Url: ",featured_image_url)


# In[7]:


    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)


# In[8]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[9]:


    tables = pd.read_html(url)
    print(tables)


# In[10]:


    marsdf = tables[0]
    marsdf


# In[11]:


    html_table = marsdf.to_html()
    html_table


# In[12]:


    url = 'https://marshemispheres.com/'
    browser.visit(url)


# In[13]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[14]:


    items = soup.find_all('img', class_ ='thumb')
    items


# In[15]:


    titles = soup.find_all('a', class_ ='itemLink product-item')['href']
    titles

## I want to use find_all here, but the list indices must be integers or slices, not str. 
## How do I use a range() statement to iterate each title in the list?


# In[ ]:


    hemisphere_image_urls = [
        {'title':titles[0],'img_url':items[0]}, 
        {'title':titles[1],'img_url':items[1]},
        {'title':titles[2],'img_url':items[2]},
        {'title':titles[3],'img_url':items[3]}]
    hemisphere_image_urls


    mars_info = {
        "mars_news": {
            "news_title": news_title,
            "news_p": news_p,
            },
        "mars_img": featured_image_url,
        "mars_facts": html_table,
        "mars_hemisphere": hemisphere_image_urls
    }

    return mars_info


