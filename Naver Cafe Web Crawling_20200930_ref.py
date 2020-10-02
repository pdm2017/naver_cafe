#!/usr/bin/env python
# coding: utf-8

# In[1]:
# Test

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pyperclip
import pandas as pd

naver_id   = 'xxxx'
naver_pass = 'xxxxx'
naver_url  = 'https://nid.naver.com/nidlogin.login'
base_url   = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=28326943&search.boardtype=L&search.page='


# In[2]:


def naver_login_get_cafe_data(naver_id, naver_pass, base_url, max_page):
    driver = webdriver.Chrome('driver/chromedriver')
    driver.get(naver_url)
    time.sleep(1)

    tag_id = driver.find_element_by_id("id")
    tag_pw = driver.find_element_by_id("pw")
    tag_id.clear()
    time.sleep(1)

    # id 입력
    tag_id.click()
    pyperclip.copy(naver_id)
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # pw 입력
    tag_pw.click()
    pyperclip.copy(naver_pass)
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 로그인 버튼을 클릭합니다
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()
    time.sleep(1)
    
    # get Page
    page_list = []
    for page_num in range(1, max_page):
        base_url2 = base_url + "{0}".format(page_num)
        time.sleep(0.5)
        driver.get(base_url2)
        driver.switch_to.frame('cafe_main')

        html = driver.page_source
        bs = BeautifulSoup(html, 'lxml')

        # 작성 게시
        td_results = bs.find_all('td', class_ = 'td_article')
        page_list.append(td_results)
        
    result_ban = []
    result_url = []

    for page in page_list:
        for td in page:
            tmp = str(td)
            idx = tmp.find('학부모')

            if idx > 1:
                tmp_td = tmp[idx - 4:idx].strip()
                result_ban.append(tmp_td)

                idx2 = tmp.find('href="/ArticleRead.nhn?clubid=28326943')
                idx3 = tmp.find('onclick="clickcr(this, ')
                tmp_url = 'https://cafe.naver.com' + tmp[idx2 + 6 : idx3 - 2].replace("&amp;", "&").strip()
                result_url.append(tmp_url) 
                
    contents_list = []
    for url in result_url:
        driver.get(url)
        time.sleep(5)  # 전체를 Loading 하는데 오래걸린다
        driver.switch_to.frame('cafe_main')

        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')
        text = ""
        for el in bs.find_all('div', class_ = 'se-module se-module-text'):
            text += el.get_text() + " "

        contents_list.append(text.replace("\n", ""))
        
    return result_ban, result_url, contents_list 


# In[3]:


def word_count(pandas_series, TopN):
    word_list = []
    for row in pandas_series:
        words = row.split(' ')
        for word in words:
            word = word.replace("엄마가", "엄마")                
            if len(word.strip()) > 1:
                word_list.append(word)
                
    word_count = dict()
    for i in word_list:
        word_count[i] = word_count.get(i, 0) + 1

    word_count_sort = sorted(word_count.items(), key=lambda x:-x[1])[:TopN] 
    
    return word_count_sort


# In[8]:


result_ban, result_url, contents_list  = naver_login_get_cafe_data(naver_id, naver_pass, base_url, 2)
df = pd.DataFrame({"BAN":result_ban, "URL":result_url, "TEXT":contents_list})
ban_count = df['BAN'].value_counts()
print(ban_count)

word_count_list = word_count(df['TEXT'], 10)
print(word_count_list)


# In[ ]:




