import bs4
import requests
from bs4 import BeautifulSoup

# to display real time price of hdfc bank
i=1
def parsePrice():

    r=requests.get('https://in.finance.yahoo.com/quote/HDFCBANK.NS?p=HDFCBANK.NS&.tsrc=fin-srch')   # stock market website
    soup = bs4.BeautifulSoup(r.text,'html.parser')
    price: object = soup.find_all('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
    return price

while(i<5):

    print("The current value of the stock hdfc is" +str(parsePrice()))
    i+=1