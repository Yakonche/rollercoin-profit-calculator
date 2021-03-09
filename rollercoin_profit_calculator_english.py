#!/usr/bin/python

import json
import urllib.request

current_hashrate = float(input("Your hashrate (TH/s) : "))

network_powers = [float(input("BTC network power (EH/s) : ")), float(input("DOGE network power (EH/s) : ")), float(input("ETH network power (EH/s) : "))]
rewards = [0.00009, 240, 0.0017]
names = ["BTC", "DOGE", "ETH"]

r = urllib.request.urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cdogecoin%2Cethereum&vs_currencies=usd")
data = json.loads(r.read())
prices = [data["bitcoin"]["usd"], data["dogecoin"]["usd"], data["ethereum"]["usd"]]

current_hashrate /= 1000000

minute = 60
hour = minute*60
day = hour*24
week = day*7
month = (365.25/12)*day
year = month*12

earnings = []
for i, (network_power, reward, price) in enumerate(zip(network_powers, rewards, prices)):
    currency_gain = reward * (current_hashrate / network_power)
    earnings.append(currency_gain * float(price))

max_index = earnings.index(max(earnings))

print("\n---------------------------\n\n{} is the most profitable cryptocurrency to mine.\n{} $ of income per block.\n".format(names[max_index], earnings[max_index]))

earnings_second = earnings[max_index] / (5*minute)
print("Is around :")
print(str(earnings_second*hour) + " $ / hour")
print(str(earnings_second*day) + " $ / day")
print(str(earnings_second*week) + " $ / week")
print(str(earnings_second*month) + " $ / month")
print(str(earnings_second*year) + " $ / year")

input("Press the Enter key to close the window.")