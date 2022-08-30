import random
import time 
import requests
class CryptoPair():
    
    
    cryptoDict = {}
    cryptoList = []
    cryptoPrices = []
    def __init__(self, base, quote, searchBase, searchQuote, price):
        self.base = base
        self.quote = quote
        self.price = price
        self.searchBase = searchBase
        searchQuote = searchQuote
        self.cryptoPrices.append(self.price)
        self.cryptoList.append(self.base+self.quote)
        self.cryptoDict.update({self.base + self.quote:self.price})

    def show_all_Cryptos(self):
        for crypto in self.cryptoList:
            print(crypto)
            
        return self.cryptoList
    
    


class userAccount(CryptoPair):
    
    def __init__(self,username):
        
        self.username = username
        self.balances = {}
        self.tradesList = {}
    def add_currency(self,currency):
        
        value = currency[1]
        return self.balances.update({currency[0]: value})
    def get_list(self):
        return self.cryptoPrices
    def get_balances(self):
        return self.balances
def fetch_pair(base, quote, searchB, searchQ,tempB, tempQ):
    try:
        return CryptoPair(base, quote,searchB,searchQ, float((requests.get("https://api.kraken.com/0/public/Depth?pair=" + searchB + searchQ)).json()['result'][searchB + searchQ]['asks'][0][0]))
    except:
        return CryptoPair(base, quote,searchB,searchQ, float((requests.get("https://api.kraken.com/0/public/Depth?pair=" + searchB + searchQ)).json()['result'][tempB + tempQ]['asks'][0][0]))


ETHUSD = fetch_pair('ETH','USD','XETH', 'ZUSD','XETH', 'ZUSD')
CRVUSD = fetch_pair('CRV','USD','CRV','USD','CRV', 'USD')
BTCUSD = fetch_pair('BTC','USD','XXBTZ','USD','USD','XXBTZ')
SOLUSD =fetch_pair("SOL","USD","SOL","USD",'SOL','USD')
CRVETH = fetch_pair('CRV', 'ETH','CRV', 'ETH','CRV','ETH')
ETHBTC = fetch_pair('ETH','BTC','XETH','XXBT','XETH','XXBT')
CRVBTC = fetch_pair('CRV','BTC','CRV', 'BTC','CRV','XBT')
# userAccount({})
# CRVBTC.show_all_Cryptos()

eath = userAccount('Papadueno')
# pey = userAccount('Plazmabacon')
eath.add_currency((5,'ETH'))
# eath.add_currency((30,'SOL'))
currencys = CryptoPair.cryptoDict
priceIndex = CryptoPair.cryptoPrices
def findMatch(dict, currencys):
    tradesList = {}
    for key in dict: 
        # Loop through balances given in method call
        key = key
        keyvalue = dict[key]
        for crypto in currencys:
            # Loop through crypto currency list
            base = crypto[:3:]
            quote = crypto[3::]
            if keyvalue == base:
                # If a currency in the given wallet 
                first = (key * currencys[crypto], quote)
                i = 0
                uniqueTrade = []
                # tradesList.update({first[0]:first[1]})
                uniqueTrade.append({1:first})
                print("First trade: {} {} into {} ".format(key, keyvalue, first))
                
                for crypto in currencys:
                    base = crypto[:3:]
                    quote = crypto[3::]
                    # print(keyvalue)
                    
                    if first[1] == base and keyvalue != quote:
                        second = (first[0] * currencys[crypto], quote)
                        # tradesList.update({second[0]:second[1]})
                        uniqueTrade.append({2:second})
                        print("Second trade: {} {} into {} ".format(first[0], first[1], second))

                        for crypto in currencys:
                            base = crypto[:3:]
                            quote = crypto[3::]
                            if second[1] == base:
                                third = (second[0] * currencys[crypto], quote)
                                # tradesList.update({third[0]:third[1]})
                                uniqueTrade.append({3:third})
                                tradesList.update({i:uniqueTrade})
                                i += 1
                                print("Third trade: {} {} into {} ".format(second[0], second[1], third))
                            elif second[1] == quote:
                                third = (second[0] / currencys[crypto], base)
                                # tradesList.update({third[0]:third[1]})
                                uniqueTrade.append({3:third})
                                tradesList.update({i:uniqueTrade})
                                i += 1
                                print("Third trade: {} {} into {}".format(second[0], second[1], third))

                    elif first[1] == quote and keyvalue != base:
                        second = (first[0] / currencys[crypto], base)
                        # tradesList.update({second[0]:second[1]})
                        uniqueTrade.append({2:second})
                        print("Second trade: {} {} into {} ".format(first[0], first[1], second))
                        for crypto in currencys:
                            base = crypto[:3:]
                            quote = crypto[3::]
                            if second[1] == base:
                                third = (second[0] * currencys[crypto], quote)
                                # tradesList.update({third[0]:third[1]})
                                uniqueTrade.append({3:third})
                                tradesList.update({i:uniqueTrade})
                                i += 1
                                print("Third trade: {} {} into {} ".format(second[0], second[1], third))
                            elif second[1] == quote:
                                third = (second[0] / currencys[crypto], base)
                                # tradesList.update({third[0]:third[1]})
                                uniqueTrade.append({3:third})
                                tradesList.update({i:uniqueTrade})
                                i += 1
                                print("Third trade: {} {} into {}".format(second[0], second[1], third))
                        
            elif keyvalue == quote:
                first = ((key / currencys[crypto]) , base)
                # first = (key * currencys[crypto], quote)
                i = 0
                uniqueTrade = []
                print("First Trade: {} {} into {}".format(key, keyvalue, first))
                # tradesList.update({first[0]:first[1]})
                uniqueTrade.append({1:first})
                for crypto in currencys:
                    base = crypto[:3:]
                    quote = crypto[3::]
                    if first[1] == base and keyvalue != quote:
                        second = (first[0] * currencys[crypto], quote)
                        # tradesList.update({second[0]:second[1]})
                        uniqueTrade.append({2:second})
                        print("Second trade: {} {} into {} {}".format(first[0], first[1], second[0], second[1]))
                        for crypto in currencys:
                            base = crypto[:3:]
                            quote = crypto[3::]
                            if second[1] == base:
                                third = (second[0] * currencys[crypto], quote)
                                # tradesList.update({third[0]:third[1]})
                                uniqueTrade.append({3:third})
                                tradesList.update({i:uniqueTrade})
                                i += 1
                                print("Third trade: {} {} into {} ".format(second[0], second[1], third))
                            elif second[1] == quote:
                                third = (second[0] / currencys[crypto], base)
                                tradesList.update({third[0]:third[1]})
                                
                                print("Third trade: {} {} into {}".format(second[0], second[1], third))
                    elif first[1] == quote and keyvalue != quote:
                        second = (first[0] / currencys[crypto], base)
                        tradesList.update({second[0]:second[1]})
                        
                        
                        print("Second trade: {} {} into {} {}".format(first[0], first[1], second[0], second[1]))
                        for crypto in currencys:
                            base = crypto[:3:]
                            quote = crypto[3::]
                            if second[1] == base:
                                third = (second[0] * currencys[crypto], quote)
                                tradesList.update({third[0]:third[1]})
                                print("Third trade: {} {} into {} ".format(second[0], second[1], third))
                            elif second[1] == quote:
                                third = (second[0] / currencys[crypto], base)
                                tradesList.update({third[0]:third[1]})
                                
                                print("Third trade: {} {} into {}".format(second[0], second[1], third))
    
    return tradesList
first_test = findMatch(eath.get_balances(), currencys)
# print(len(first_test))
# for result in first_test:
#     print(first_test[result])
# findMatch(findMatch(eath.get_balances(),CryptoPair.cryptoDict),CryptoPair.cryptoDict)

