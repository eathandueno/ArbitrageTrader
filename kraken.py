import requests
import random
import time 
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

    # def findMatch(self,balances):
    #     prices = self.cryptoPrices
        
    #     currencys = self.cryptoList
    #     tradeList = []
    #     for crypto in currencys:
    #         base = crypto[:3:]
    #         quote = crypto[3::]
    #         if balances[1] == base:
                
    #             first = (balances[0] * prices[currencys.index(crypto)], quote)
    #             # currencys.pop(currencys.index(crypto))
    #             tradeList.append(first)
                
    #         elif balances[1] == quote:
    #             # base = crypto[:3:]
    #             # print(crypto)
    #             conversion  = prices[currencys.index(crypto)]
    #             # print(conversion)
    #             first = (balances[0] / conversion, base)
    #             # print(first)
    #             tradeList.append(first)
    #     return tradeList

    def show_all_Cryptos(self):
        for crypto in self.cryptoList:
            print(crypto)
            # print(self.cryptoPrices)
        return self.cryptoPrices
    
    


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
eath.add_currency((30,'SOL'))
# print(eath.get_list())
# pey.add_currency((1000,'USD'))
# pey.add_currency((1,'BTC'))
# cryptosDict = eath.cryptoDict
# # print(cryptosDict)
# currencys = eath.cryptoList
# cryptos = eath.cryptoPrices
# print(eath.get_balances())
# print(eath.findMatch())
# print('=======================')
# print(pey.findMatch().findMatch())
currencys = CryptoPair.cryptoDict
priceIndex = CryptoPair.cryptoPrices
def findMatch(dict, currencys):
    tradesList = {}
    for key in dict:
        
        key = key
        keyvalue = dict[key]
        for crypto in currencys:
            
            base = crypto[:3:]
            quote = crypto[3::]
            if keyvalue == base:
                
                first = (key * currencys[crypto], quote)
                tradesList.update({first[0]:first[1]})
                print("First trade: {} {} into {} ".format(key, keyvalue, first))
                currencys = CryptoPair.cryptoDict
                for crypto in currencys:
                    base = crypto[:3:]
                    quote = crypto[3::]
                    
                    currencys = CryptoPair.cryptoDict
                    if first[1] == base and keyvalue != base:
                        second = (first[0] * currencys[crypto], quote)
                        tradesList.update({second[0]:second[1]})
                        print("Second trade: {} {} into {} ".format(first[0], first[1], second))
                    elif first[1] == quote and keyvalue != quote:
                        second = (first[0] / currencys[crypto], base)
                        tradesList.update({second[0]:second[1]})
                        print("Second trade: {} {} into {} ".format(first[0], first[1], second))
            elif keyvalue == quote:
                base = crypto[:3:]
                conversion  = (key / currencys[crypto])
                # print(conversion)
                first = (conversion , base)
                print("First Trade: {} {} into {}".format(key, keyvalue, first))
                tradesList.update({first[0]:first[1]})
    
    return tradesList
findMatch(eath.get_balances(), CryptoPair.cryptoDict)
# findMatch(findMatch(findMatch(eath.get_balances())))

