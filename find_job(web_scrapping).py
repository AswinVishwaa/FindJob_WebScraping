# -*- coding: utf-8 -*-
"""find_job(web_scrapping).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hPru3v-_t94hfknG6ZmokKkqDfAO7GGA
"""

from bs4 import BeautifulSoup
import requests
import time

print("Enter unfamiliar skills")
unfamiliar_skill=input('<O>')

def find_jobs():
  html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
  soup = BeautifulSoup(html_text,'lxml')
  jobs = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
  for index,job in enumerate(jobs):
    period = job.find("span",class_="sim-posted").span.text
    if "few" in period:
      company_name=job.find("h3",class_="joblist-comp-name").text.replace(' ','')
      skills = job.find("span",class_="srp-skills").text.replace(' ','')
      link = job.header.h2.a["href"]
      if unfamiliar_skill not in skills:
        print(f"Company_Name    : {company_name.strip()}")
        print(f"Required Skills : {skills.strip()}")
        print(f"More Info       : {link}")
        print("")

if __name__ == '__main__':
  while True:
    find_jobs()
    waiting_time=10
    print(f"please wait for {waiting_time} minutes")
    #time.sleep(waiting_time*60)

