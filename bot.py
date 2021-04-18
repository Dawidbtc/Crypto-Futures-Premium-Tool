import time 
import hmac
import requests
import json
response= requests.get("https://ftx.com/api/futures/BTC-1231")
futuresName=response.json()['result']['description']
futuresPrice=response.json()['result']['last']
spotResponse=requests.get("https://ftx.com/api/futures/BTC-PERP")
spotPrice=spotResponse.json()['result']['last']
currentAPY=(futuresPrice-spotPrice)/spotPrice

print("Welcome to Futures Premium Calculator")
print("This tool can be used to quickly calculate yield on capturing premium profits")
print("Market data extracted from FTX")
print("By Dawid Chudzik")
print("-------------------------------------------")
print("Current Farthest Out Futures Expiry:",futuresName)
print("Current Price of Future: $",futuresPrice)
print("Current Price of Spot: $",spotPrice)
print("Current Yield From Capturing Futures Premium: "+"{:.2%}".format(currentAPY))