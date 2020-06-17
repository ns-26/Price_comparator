#!/usr/bin/env python
# coding: utf-8

# In[34]:


import requests as rq
from bs4 import BeautifulSoup
import re
from tkinter import *

window=Tk()
e_val=StringVar()
def Flipkart():
    query = e_val.get()
    payload = {'q' : query}
    header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    
    
    r = rq.get("https://www.flipkart.com/search", params=payload, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    results_div = soup.find('div', attrs={'class' : re.compile('_3O0U0u')})


    for rd in results_div:
        price = rd.find('div', attrs = {'class' : re.compile('_1vC4OE')})
        break;

    if price!=None :
        print(price.getText());


    for name in results_div:
        prodName=name.find('div', attrs = {'class' : re.compile('_3wU53n')})
        break;
    if prodName == None:
        for name in results_div:
            prodName=name.find('a', attrs = {'class' : re.compile('_2cLu-l')})
            break;


    if prodName!=None :
        print(prodName.getText());


e1 = Entry(window, textvariable=e_val)
b1 = Button(window, text="Flipkart Search", command=Flipkart)
t1 = Text(window)
e1.grid(row=0, column=0, columnspan=4)
b1.grid(row=0, column=4, columnspan=2)
window.mainloop()


# In[ ]:




