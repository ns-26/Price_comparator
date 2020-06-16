#!/usr/bin/env python
# coding: utf-8

# In[34]:


import requests as rq
from bs4 import BeautifulSoup
import re
from tkinter import *

window=Tk()
e_val=StringVar()
def get_info():
    query = e_val.get()
    payload = {'q' : query}
    header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    r = rq.get("https://www.amazon.in/s?k="+query, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    results_div = soup.find_all('div', attrs={'class' :re.compile('sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32')})
    results_div_deep=[];
    for rd in results_div:
        results_div_deep.append(rd.find('span', attrs = {'class' : re.compile('a-price-whole')}))
    for result in results_div_deep:
        if result != None:
            print(result.getText())
            break;
            
e1 = Entry(window, textvariable=e_val)
b1 = Button(window, text="Amazon Search", command=get_info)
t1 = Text(window)
e1.grid(row=0, column=0, columnspan=4)
b1.grid(row=0, column=4, columnspan=2)
window.mainloop()


# In[ ]:




