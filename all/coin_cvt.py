import json
import re

with open('rawCoinInfo.json', 'r') as f:
    coinjs = json.load(f)


newjson = {}

for coin in coinjs:
    null = None;

    number = coin["number"]
    number = number.replace(" ","")
    number = number.replace("\n","")

    marketCap = coin["marketCap"]
    marketCap = marketCap.replace(" ","")
    marketCap = marketCap.replace("\n","")

    circulatingSupply = coin["circulatingSupply"]
    if(circulatingSupply is not null):
        circulatingSupply = circulatingSupply.replace(" ","")
        circulatingSupply = circulatingSupply.replace("\n","")
    else : circulatingSupply = "null"
    
    newjson.update(
        {
            coin["name"]: {
                'number' : number,
                'symbol' : coin["symbol"],
                'marketCap' : marketCap,
                'price' : coin["price"],
                'circulatingSupply' : circulatingSupply,
                'volume' : coin["volume24"],
                '1HPercent' : coin["%1h"],
                '24HPercent' : coin['%24h'],
                '7DPercent' : coin['%7d']
                }
            }
        )

with open('formatedCoinInfo.json', 'w') as f:
    json.dump(newjson,f, indent=2)


