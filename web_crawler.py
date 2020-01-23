
'''**********************************************python web crawler***************************************'''
import requests  # for http requests 
import re   #regular expression can be used instead of beautiful soup 
from  bs4 import BeautifulSoup  #for html parsing 
from string import ascii_lowercase
def web_crawler(url):
   words=[]
   corresponding_links=[]
   p=requests.get(url)
   p1=BeautifulSoup(p.content,'html.parser')
   p1=p1.find_all('a',class_="css-ytumd6 e1j8zk4s1") #using the class_name in dictionary.com li-tag by inspecting 
   for ele in p1:
       if(len(ele.text.strip())>=13):
           words.append(ele.text.strip())
           corresponding_links.append(ele.get('href'))
   print(words)
   print(corresponding_links)
   
url='https://www.dictionary.com/list/'
#for scrapping all the words starting from A to Z , we have to use the alphabets 
for alphabets in ascii_lowercase:
   for i in range(1,10): 
     web_crawler(url+alphabets+'/'+str(i))
