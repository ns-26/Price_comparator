import requests as rq
from bs4 import BeautifulSoup
from tkinter import *




window = Tk()





def findGoogleLink():
    query = e_val.get()
    payload = {"q": query, 'num' : '20'}
    header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    
    
    r = rq.get("https://www.google.co.in/search", params=payload, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    result_div = soup.find_all('div', attrs = {'class': 'r'})
    links = []


    for r in result_div:
        try:
            link = r.find('a')
            if link != '': 
                links.append(link['href'])
        except:
            continue
    t = links[0]
    print(t)


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


def Amazon():
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




e_val = StringVar()
e1 = Entry(window, textvariable = e_val)
b1 = Button(window, text="Search Item", command=findGoogleLink)
e1.grid(row=0, column=0, columnspan=3)
b1.grid(row=0, column=3)
window.mainloop()