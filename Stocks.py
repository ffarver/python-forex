from bs4 import BeautifulSoup as bs
import requests
from requests.exceptions import RequestException
from contextlib import closing
import csv
import os
import time

def menu():
    choice = input("What trade would you like to check?\n[1] Forex\n[2] Stocks\n")

    if choice == '1':
        os.system('cls')
        forex()
    elif choice == '2':
        os.system('cls')
        stocks()
    elif choice == 'eurusd':
        eurusd()

def forex():
    pair = input("What currency pair would you like to see?\n[1] EURUSD\n[2] GBPUSD\n[3] USDJPY\n[4] USDCAD\n[5] EURJPY\n[6] Back\n")
    if pair == '1':
        os.system('cls')
        eurusd()
    elif pair == '2':
        os.system('cls')
        gbpusd()
    elif pair == '3':
        os.system('cls')
        usdjpy()
    elif pair == '4':
        os.system('cls')
        usdcad()
    elif pair == '5':
        os.system('cls')
        eurjpy()
    else:
        os.system('cls')
        menu()

def eurusd():
    os.system('cls')
    url = 'https://www.dailyforex.com/currencies/eur/usd'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'class' : 'Bid' })
    high_box = soup.find('span', attrs={'class' : 'cell2 col-xs-5'})
    high = high_box.get_text()
    name = name_box.get_text()
    print('Current price of EURUSD: ', name)
    print('The high for today is: ', high)
    time.sleep(7)
    os.system('cls')
    forex()
          
def  gbpusd():
    os.system('cls')
    url = 'https://www.dailyforex.com/currencies/gbp/usd'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'class' : 'Bid'})
    high_box = soup.find('span', attrs={'class' : 'cell2 col-xs-5'})
    high = high_box.get_text()
    name = name_box.get_text()
    print('Current price of GBPUSD: ', name)
    print('The high for today is: ', high)
    time.sleep(7)
    os.system('cls')
    forex()
        
def usdjpy():
    os.system('cls')
    url = 'https://www.dailyforex.com/currencies/usd/jpy'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'class' : 'Bid'})
    high_box = soup.find('span', attrs={'class' : 'cell2 col-xs-5'})
    high = high_box.get_text()
    name = name_box.get_text()
    print('Current price of USDJPY: ', name)
    print('The high for today is: ', high)
    time.sleep(7)
    os.system('cls')
    forex()

def usdcad():
    os.system('cls')
    url = 'https://www.dailyforex.com/currencies/usd/cad'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'class' : 'Bid'})
    high_box = soup.find('span', attrs={'class' : 'cell2 col-xs-5'})
    high = high_box.get_text()
    name = name_box.get_text()
    print('Current price of USDCAD: ', name)
    print('The high for today is: ', high)
    time.sleep(7)
    os.system('cls')
    forex()
    
def eurjpy():
    os.system('cls')
    url = 'https://www.dailyforex.com/currencies/eur/jpy'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'class' : 'Bid'})
    high_box = soup.find('span', attrs={'class' : 'cell2 col-xs-5'})
    high = high_box.get_text()
    name = name_box.get_text()
    print('Current price of EURJPY: ', name)
    print('The high for today is: ', high)
    time.sleep(7)
    os.system('cls')
    forex()

def stocks():
    stock = input("What stock would you like to see?\n[1] Tesla\n[2] Amazon\n[3] Exxon Mobile\n[4] IBM\n[5] Google\n[6] Back\n")
    if stock == '1':
        os.system('cls')
        tsla()
    elif stock == '2':
        os.system('cls')
        amzn()
    elif stock == '3':
        os.system('cls')
        exxon()
    elif stock == '4':
        os.system('cls')
        ibm()
    elif stock == '5':
        os.system('cls')
        google()
    else:
        os.system('cls')
        menu()

def tsla():
    os.system('cls')
    url = 'http://www.nasdaq.com/symbol/tsla/real-time'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'id' : 'quotes_content_left__LastSale'})
    market_close = soup.find('span', attrs={'id' : 'quotes_content_left__PreviousClose'})
    close = market_close.get_text()
    name = name_box.get_text()
    high_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysHigh'})
    low_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysLow'})
    high = high_today.get_text()
    low = low_today.get_text()
    print('Current value of TSLA: ', '$', name)
    print('High for today is: ', '$', high)
    print('Low for today is: ', '$', low)
    print('Previous market close value: ', '$', close)
    time.sleep(7)
    os.system('cls')
    stocks()

def amzn():
    os.system('cls')
    url = 'http://www.nasdaq.com/symbol/amzn/real-time'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'id' : 'quotes_content_left__LastSale'})
    market_close = soup.find('span', attrs={'id' : 'quotes_content_left__PreviousClose'})
    close = market_close.get_text()
    name = name_box.get_text()
    high_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysHigh'})
    low_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysLow'})
    high = high_today.get_text()
    low = low_today.get_text()
    print('Current value of AMZN: ', '$', name)
    print('High for today is: ', '$', high)
    print('Low for today is: ', '$', low)
    print('Previous market close value: ', '$', close)
    time.sleep(7)
    os.system('cls')
    stocks()

def exxon():
    os.system('cls')
    url = 'http://www.nasdaq.com/symbol/xom/real-time'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'id' : 'quotes_content_left__LastSale'})
    market_close = soup.find('span', attrs={'id' : 'quotes_content_left__PreviousClose'})
    close = market_close.get_text()
    name = name_box.get_text()
    high_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysHigh'})
    low_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysLow'})
    high = high_today.get_text()
    low = low_today.get_text()
    print('Current value of XOM: ', '$', name)
    print('High for today is: ', '$', high)
    print('Low for today is: ', '$', low)
    print('Previous market close value: ', '$', close)
    time.sleep(7)
    os.system('cls')
    stocks()

def ibm():
    os.system('cls')
    url = 'http://www.nasdaq.com/symbol/ibm/real-time'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'id' : 'quotes_content_left__LastSale'})
    market_close = soup.find('span', attrs={'id' : 'quotes_content_left__PreviousClose'})
    close = market_close.get_text()
    name = name_box.get_text()
    high_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysHigh'})
    low_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysLow'})
    high = high_today.get_text()
    low = low_today.get_text()
    print('Current value of IBM: ', '$', name)
    print('High for today is: ', '$', high)
    print('Low for today is: ', '$', low)
    print('Previous market close value: ', '$', close)
    time.sleep(7)
    os.system('cls')
    stocks()

def google():
    os.system('cls')
    url = 'http://www.nasdaq.com/symbol/googl/real-time'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'id' : 'quotes_content_left__LastSale'})
    market_close = soup.find('span', attrs={'id' : 'quotes_content_left__PreviousClose'})
    close = market_close.get_text()
    name = name_box.get_text()
    high_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysHigh'})
    low_today = soup.find('span', attrs={'id' : 'quotes_content_left__TodaysLow'})
    high = high_today.get_text()
    low = low_today.get_text()
    print('Current value of GOOGL: ', '$', name)
    print('High for today is: ', '$', high)
    print('Low for today is: ', '$', low)
    print('Previous market close value: ', '$', close)
    time.sleep(7)
    os.system('cls')
    stocks()
    

menu()
