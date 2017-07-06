import json

with open('rawCoinInfo.json', 'r') as f:
    coinjs = json.load(f)


symbolList = []

for coin in coinjs:
    symbolList.append(coin['symbol'])

symbolFile = open('symbolnames.txt','w')
for symbol in symbolList:
    symbolFile.write("%s\n" % symbol)