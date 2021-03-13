#!/usr/bin/python

import json
import urllib.request
import os
import sys

from sty import fg

if sys.platform == "win32":
    os.system('color')

current_hashrate = float(input("\n Enter your hashrate (TH/s) : "))

network_powers = [
    float(input("\n Enter the " + fg(255, 128, 10) + "BTC" + fg.rs +
                " network power (EH/s) : ")),
    float(input(" Enter the " + fg(255, 255, 0) + "DOGE" + fg.rs +
                " network power (EH/s) : ")),
    float(input(" Enter the " + fg(127, 0, 255) + "ETH" + fg.rs +
                " network power (EH/s) : "))
]

rewards = [
    float(input(
        "\n Enter the " + fg(255, 128, 10) + "BTC" + fg.rs + " reward\n"
        " Default value is 0.00009, just press Enter to validate this value : "
    ) or 0.00009),
    float(input(
        "\n Enter the " + fg(255, 255, 0) + "DOGE" + fg.rs + " reward\n"
        " Default value is 240, just press Enter to validate this value : "
    ) or 240.0),
    float(input(
        "\n Enter the " + fg(127, 0, 255) + "ETH" + fg.rs + " reward\n"
        " Default value is 0.0017, just press Enter to validate this value : "
    ) or 0.0017)
]

names = [fg(255, 128, 10) + "BTC" + fg.rs, fg(255, 255, 0) + "DOGE" + fg.rs,
         fg(127, 0, 255) + "ETH" + fg.rs]

r = urllib.request.urlopen(
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin%2Cdogecoin%2Cethereum&vs_currencies=usd"
    )
data = json.loads(r.read())
prices = [data["bitcoin"]["usd"], data["dogecoin"]["usd"],
          data["ethereum"]["usd"]]

current_hashrate /= 1000000

minute = 60
hour = minute*60
day = hour*24
week = day*7
month = (365.25/12)*day
year = month*12

earnings = []
earnings_crypto = []
for i, (network_power, reward, price) in enumerate(
        zip(network_powers, rewards, prices)):
    currency_gain = reward * (current_hashrate / network_power)
    earnings.append(currency_gain * float(price))
    earnings_crypto.append(currency_gain)

max_index = earnings.index(max(earnings))

print("\n ---------------------------\n")
print((
    " \"{}\" is the most profitable cryptocurrency to mine.\n"
    " \"{}\" " + fg(0, 255, 0) + "$" + fg.rs + " of income per block.\n"
    " Or \"{}\" \"{}\" / block.\n"
    ).format(
        names[max_index], earnings[max_index], earnings_crypto[max_index],
        names[max_index]
    )
)

earnings_second = earnings[max_index] / (5*minute)
earnings_cryptot = earnings_crypto[max_index] / (5*minute)

print(" Is around :")
print(" " + str(earnings_second*hour) + fg(0, 255, 0) + " $" + fg.rs +
      " / hour, or " + str(earnings_cryptot*hour) + " " + names[max_index])
print(" " + str(earnings_second*day) + fg(0, 255, 0) + " $" + fg.rs +
      " / day, or " + str(earnings_cryptot*day) + " " + names[max_index])
print(" " + str(earnings_second*week) + fg(0, 255, 0) + " $" + fg.rs +
      " / week, or " + str(earnings_cryptot*week) + " " + names[max_index])
print(" " + str(earnings_second*month) + fg(0, 255, 0) + " $" + fg.rs +
      " / month, or " + str(earnings_cryptot*month) + " " + names[max_index])
print(" " + str(earnings_second*year) + fg(0, 255, 0) + " $" + fg.rs +
      " / year, or " + str(earnings_cryptot*year) + " " + names[max_index])

input("\n Press the Enter key to close the window.\n")
