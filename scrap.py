#using this to scrap title,etc
#python3 used here 

from bs4 import BeautifulSoup
import requests 
import re
from htmldate import find_date

def get_lang(data):
 #regular expression used here for lang attribute  
 lang = re.search('''\s+(?:[^>]*?\s+)?lang="([^"]*)"''',data).group(1)
 print(lang)
 
def get_title(data):
  #title extraction function 
  soup = BeautifulSoup(data,'lxml')
  print(soup.title.text)


def get_date(data):
  #this function gets the last modified date of a website
     x = find_date(data)
     print(x)   


#using file handeling to accesss urls
f=open("link.txt","r")
for x in f:

 print(x)
 try:
     #exception handeling here if request is not good

     r = requests.get(x.rstrip())
     data = r.text
     get_title(data)
     get_lang(data) 
     get_date(data)	 
     print("-------------------------------------")


 

 except Exception as e:
  print(e) 
