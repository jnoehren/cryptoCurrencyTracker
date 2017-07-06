import urllib.parse
import requests

file = open("symbolnames.txt","r")
counter = 0
for line in file:
	line = line.replace("\n","")
	api = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms='
	coin = line
	toSyms = '&tsyms=USD'

	URL = api + coin + toSyms
	print(counter)
	print(coin)
	counter+=1

	try:
		json_data = requests.get(URL).json()
		print(json_data['RAW'][coin]['USD']['PRICE'])
		print("")

	except :
		print('error')
		print("")