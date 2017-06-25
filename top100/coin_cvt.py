import json
import re

with open('coinInfo.json', 'r') as f:
    coinjs = json.load(f)


newjson = {}

for coin in coinjs:

    number = coin["number"]
    number = number.replace(" ","")
    number = number.replace("\n","")

    marketCap = coin["marketCap"]
    marketCap = marketCap.replace(" ","")
    marketCap = marketCap.replace("\n","")

    circulatingSupply = coin["circulatingSupply"]
    circulatingSupply = circulatingSupply.replace(" ","")
    circulatingSupply = circulatingSupply.replace("\n","")

    newjson.update(
        {
            coin["name"]: {
                'number' : number,
                'marketCap' : marketCap,
                'price' : coin["price"],
                'circulatingSupply' : circulatingSupply,
                'volume' : coin["volume"],
                'percentChange' : coin["percentChange"]
                }
            }
        )

with open('formatedCoinInfo.json', 'w') as f:
    json.dump(newjson,f, indent=2)


