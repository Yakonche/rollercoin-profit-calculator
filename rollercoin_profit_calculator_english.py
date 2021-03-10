#!/usr/bin/python

import json
import urllib.request

current_hashrate = float(input("\nEnter your hashrate (TH/s) : "))

network_powers = [
    float(input(
        "\nEnter the BTC network power (EH/s)\n"
        "Default value is 0.00009, just press Enter to validate this value : "
    ) or 0.00009),
    float(input(
        "\nEnter the DOGE network power (EH/s)\n"
        "(Default value is 240, just press Enter to validate this value : "
    ) or 240.0),
    float(input(
        "\nEnter the ETH network power (EH/s)\n"
        "Default value is 0.0017, just press Enter to validate this value : "
    ) or 0.0017)
]
rewards = [0.00009, 240, 0.0017]
names = ["BTC", "DOGE", "ETH"]

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

print(
    "\n ---------------------------\n\n{} is the most profitable "
    "cryptocurrency to mine.\n{} $ of income per block.\nOr {} {} / block.\n"
    .format(
        names[max_index], earnings[max_index], earnings_crypto[max_index],
        names[max_index]
    )
)

earnings_second = earnings[max_index] / (5*minute)
earnings_cryptot = earnings_crypto[max_index] / (5*minute)
print("Is around :")
print(str(earnings_second*hour) + " $ / hour" + " ,or " +
      str(earnings_cryptot*hour) + " "+names[max_index])
print(str(earnings_second*day) + " $ / day" + " ,or " +
      str(earnings_cryptot*day) + " " + names[max_index])
print(str(earnings_second*week) + " $ / week" + " ,or " +
      str(earnings_cryptot*week) + " " + names[max_index])
print(str(earnings_second*month) + " $ / month" + " ,or " +
      str(earnings_cryptot*month) + " " + names[max_index])
print(str(earnings_second*year) + " $ / year" + " ,or " +
      str(earnings_cryptot*year) + " " + names[max_index])

input("\nPress the Enter key to close the window.")
