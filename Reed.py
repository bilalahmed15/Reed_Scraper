#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd 
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
import re
from selenium.webdriver.common.action_chains import ActionChains
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)


# In[19]:


driver = webdriver.Chrome()
driver.get("https://www.reed.co.uk")
time.sleep(10)


# In[20]:


Accept_button=driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/div/div/button')
Accept_button.click()
time.sleep(10)


# In[21]:


driver.find_element(By.XPATH,'/html/body/div[2]/div/header/div[2]/div[1]/ul/li[2]/a').click()
time.sleep(10)


# In[22]:


driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/form/div[1]/input').send_keys('hmafsar9@gmail.com')
driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/form/div[2]/input').send_keys('jyxkyp-nidqur-Gurpy2')
signin_button=driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/form/button')
signin_button.click()
time.sleep(20)


# In[23]:


driver.find_element(By.XPATH,'/html/body/div[1]/div/form/div[1]/div[1]/span/input').send_keys('AI Engineer')
driver.find_element(By.XPATH,'/html/body/div[1]/div/form/div[1]/div[2]/span/input').send_keys('London')
driver.find_element(By.XPATH,'/html/body/div[1]/div/form/div[1]/div[3]/button').click()
time.sleep(10)


# # Applying to multiple job

# In[24]:


import time
j=1
i=2
while(j<40):
    if (i==26):
        driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[3]/main/div[6]/div/nav/ul/li[9]/a').click()
        i=1
    else:
        while(i<25):
            time.sleep(10)
            try:
                driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[3]/main/article['+str(i)+']/div/div/div[1]/header/h2/a').click()
                try:
                    try:
                        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div[1]/div[2]/article/div/div[2]/aside/div[1]/button[1]').click()
                        time.sleep(10)
                        driver.back()
                        driver.back()
                        time.sleep(10)
                    except:
                        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div[1]/div[2]/article/div/div[2]/aside/div[1]/button[1]').click()
                        time.sleep(10)
                        driver.back()
                        driver.back()
                        time.sleep(10)
                except:
                    driver.back()
            except:
                driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[3]/main/article['+str(i)+']/div/div/div[1]/header/h2/a').click()
                try:
                    try:
                        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div[1]/div[2]/article/div/div[2]/aside/div[1]/button[1]').click()
                        time.sleep(10)
                        driver.back()
                        driver.back()
                        time.sleep(10)
                    except:
                        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div[1]/div[2]/article/div/div[2]/aside/div[1]/button[1]').click()
                        time.sleep(10)
                        driver.back()
                        driver.back()
                        time.sleep(10)
                except:
                    driver.back()
            i+=1
    j+=1
 
    


