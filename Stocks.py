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
    pair = input("What currency pair would you like to see?\n[1] EURUSD\n[2] GBPUSD\n[3] USDJPY\n[4] USDCAD\n[5] EURJPY\n[6] Gold\n[7] Oil\n[8] XRP\n[9] Export all data to spreadsheet\n[0] Back\n")
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
    elif pair == '6':
        os.system('cls')
        gold()
    elif pair == '7':
        os.system('cls')
        oil()
    elif pair == '8':
        os.system('cls')
        xrp()
    elif pair == '9':
        os.system('cls')
        spreadsheet()
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
    print('Current price of EURUSD: ','$', name)
    print('The high for today is: ','$', high)
    if name >= '1.165':
        print('It is recommended to open a sell order')
    elif name <= '1.155':
        print('It is recommended to open a buy order')
    else:
        print('It is recommended to not open any order at this time')
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
    print('Current price of GBPUSD: ','$', name)
    print('The high for today is: ','$', high)
    if name >= '1.3085':
        print('It is recommended to open a sell order')
    elif name <= '1.2898':
        print('It is recommended to open a buy order')
    else:
        print('It is recommended to not open any order at this time')
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
    print('Current price of USDJPY: ','$', name)
    print('The high for today is: ','$', high)
    if name >= '113.489':
        print('It is recommended to open a sell order')
    elif name <= '112.000':
        print('It is recommended to open a buy order')
    else:
        print('It is recommended to not open any order at this time')
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
    print('Current price of USDCAD: ','$', name)
    print('The high for today is: ','$', high)
    if name >= '1.314':
        print('It is recommended to open a sell order')
    elif name <= '1.289':
        print('It is recommended to open a buy order')
    else:
        print('It is recommended to not open any order at this time')
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
    print('Current price of EURJPY: ','$', name)
    print('The high for today is: ','$', high)
    if name >= '131':
        print('It is recommended to open a sell order')
    elif name <= '128.5':
        print('It is recommended to open a buy order')
    else:
        print('It is recommended to not open any order at this time')
    time.sleep(7)
    os.system('cls')
    forex()

def gold():
    os.system('cls')
    url = 'https://www.dailyforex.com/commodities/gold'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'class' : 'Bid'})
    high_box = soup.find('span', attrs={'class' : 'cell2 col-xs-5'})
    high = high_box.get_text()
    name = name_box.get_text()
    print('Current price of GOLD: ','$', name)
    print('The high for today is: ', '$', high)
    if name >= '1239.94':
        print('It is recommended to open a sell order')
    elif name <= '1203.44':
        print('it is recommended to open a buy order')
    else:
        print('it is recommended to not open any order at this time')
    time.sleep(7)
    os.system('cls')
    forex()

def oil():
    os.system('cls')
    url = 'https://www.dailyforex.com/commodities/crude-oil'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'class' : 'Bid'})
    high_box = soup.find('span', attrs={'class' : 'cell2 col-xs-5'})
    high = high_box.get_text()
    name = name_box.get_text()
    print('Current price of CrudeOIL: ','$', name)
    print('The high for today is: ', '$', high)
    if name >= '46.00':
        print('it is recommended to open a sell order')
    elif name >= '38.00':
        print('it is recommended to open a buy order')
    else:
        print('it is recommended to not open any order at this time')
    time.sleep(7)
    os.system('cls')
    forex()

def xrp():
    os.system('cls')
    url = 'https://coinmarketcap.com/currencies/ripple/'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name_box = soup.find('span', attrs={'class' : 'h2 text-semi-bold details-panel-item--price__value'})
    name = name_box.get_text()
    print('Current price of XRPUSD: ','$', name)
    if name >= '0.545':
        print('It is recommended to open a sell order')
    elif name <= '0.52':
        print('It is recommended to open a buy order')
    else:
        print('It is recommended to not open any order at this time')
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

def spreadsheet():
    os.system('cls')
    eurusd = 'https://www.dailyforex.com/currencies/eur/usd'
    gbpusd = 'https://www.dailyforex.com/currencies/gbp/usd'
    usdcad = 'https://www.dailyforex.com/currencies/usd/cad'
    eurjpy = 'https://www.dailyforex.com/currencies/eur/jpy'
    usdjpy = 'https://www.dailyforex.com/currencies/usd/jpy'
    gold = 'https://www.dailyforex.com/commodities/gold'
    oil = 'https://www.dailyforex.com/commodities/crude-oil'
    xrpusd = 'https://coinmarketcap.com/currencies/ripple/'
    eu = requests.get(eurusd)
    gu = requests.get(gbpusd)
    uc = requests.get(usdcad)
    ej = requests.get(eurjpy)
    uj = requests.get(usdjpy)
    g = requests.get(gold)
    o = requests.get(oil)
    xu = requests.get(xrpusd)
    soupeu = bs(eu.content, 'html.parser')
    soupgu = bs(gu.content, 'html.parser')
    soupuc = bs(uc.content, 'html.parser')
    soupej = bs(ej.content, 'html.parser')
    soupuj = bs(uj.content, 'html.parser')
    soupg = bs(g.content, 'html.parser')
    soupo = bs(o.content, 'html.parser')
    soupxu = bs(xu.content, 'html.parser')
    eurusd_box = soupeu.find('span', attrs={'class' :  'Bid'})
    gbpusd_box = soupgu.find('span', attrs={'class' : 'Bid'})
    usdcad_box = soupuc.find('span', attrs={'class' : 'Bid'})
    eurjpy_box = soupej.find('span', attrs={'class' : 'Bid'})
    usdjpy_box = soupuj.find('span', attrs={'class' : 'Bid'})
    gold_box = soupg.find('span', attrs={'class' : 'Bid'})
    oil_box = soupo.find('span', attrs={'class' : 'Bid'})
    eurusd_high_box = soupeu.find('span', attrs={'class' : 'cell2 col-xs-5'})
    gbpusd_high_box = soupgu.find('span', attrs={'class' : 'cell2 col-xs-5'})
    usdcad_high_box = soupuc.find('span', attrs={'class' : 'cell2 col-xs-5'})
    eurjpy_high_box = soupej.find('span', attrs={'class' : 'cell2 col-xs-5'})
    usdjpy_high_box = soupuj.find('span', attrs={'class' : 'cell2 col-xs-5'})
    gold_high_box = soupg.find('span', attrs={'class' : 'cell2 col-xs-5'})
    oil_high_box = soupo.find('span', attrs={'class' : 'cell2 col-xs-5'})
    xrpusd_box = soupxu.find('span', attrs={'class' : 'h2 text-semi-bold details-panel-item--price__value'})
    eu_box = eurusd_box.get_text()
    gu_box = gbpusd_box.get_text()
    uc_box = usdcad_box.get_text()
    ej_box = eurjpy_box.get_text()
    uj_box = usdjpy_box.get_text()
    g_box = gold_box.get_text()
    crudeoil = oil_box.get_text()
    xu_box = xrpusd_box.get_text()
    eu_high = eurusd_high_box.get_text()
    gu_high = gbpusd_high_box.get_text()
    uc_high = usdcad_high_box.get_text()
    ej_high = eurjpy_high_box.get_text()
    uj_high = usdjpy_high_box.get_text()
    g_high = gold_high_box.get_text()
    o_high = oil_high_box.get_text()
    if eu_box >= '1.165':
        eu_what = 'sell'
    elif eu_box <= '1.155':
        eu_what = 'buy'
    if gu_box >= '1.3085':
        gu_what = 'sell'
    elif gu_box <= '1.2898':
        gu_what = 'buy'
    else:
        gu_what = 'Neutral'
    if uj_box >= '113.489':
        uj_what = 'sell'
    elif uj_box <= '112.000':
        uj_what = 'buy'
    else:
        uj_what = 'Neutral'
    if uc_box >= '1.314':
        uc_what = 'sell'
    elif uc_box <= '1.289':
        uc_what = 'buy'
    else:
        uc_what = 'Neutral'
    if ej_box >= '131':
        ej_what = 'sell'
    elif ej_box <= '128.5':
        ej_what = 'buy'
    else:
        ej_what = 'Neutral'
    if g_box >= '1239.94':
        g_what = 'sell'
    elif g_box <= '1203.44':
        g_what = 'buy'
    else:
        g_what = 'Neutral'
    if crudeoil >= '46.00':
        oil_what = 'sell'
    elif crudeoil >= '38.00':
        oil_what = 'buy'
    else:
        oil_what = 'Neutral'


    current_value = [[' ', 'eurusd', 'gbpusd', 'usdcad', 'eurjpy', 'usdjpy', 'gold', 'crudeOIL', 'xrpusd'], ['Current Value', eu_box, gu_box, uc_box, ej_box, uj_box, g_box, crudeoil, xu_box]]
    high_value = [['high', eu_high, gu_high, uc_high, ej_high, uj_high, g_high, o_high, 'N/A']]
    buyorsell = [['Buy/Sell', eu_what, gu_what, uc_what, ej_what, uj_what, g_what, oil_what, 'N/A']]
    file = open('compiled_currencies.csv', 'w')
    with file:
        writer = csv.writer(file, dialect='excel')
        writer.writerows(current_value)
        writer.writerows(high_value)
        writer.writerows(buyorsell)
        print('done')

    os.startfile('compiled_currencies.csv')
menu()
