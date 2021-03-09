#!/usr/bin/python

import json
import urllib.request

current_hashrate = float(input("Votre hashrate (TH/s) : "))

network_powers = [float(input("Puissance du réseau BTC (EH/s) : ")), float(input("Puissance du réseau DOGE (EH/s) : ")), float(input("Puissance du réseau ETH (EH/s) : "))]
rewards = [0.00009, 240, 0.0017]
names = ["BTC", "DOGE", "ETH"]

r = urllib.request.urlopen("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cdogecoin%2Cethereum&vs_currencies=eur")
data = json.loads(r.read())
prices = [data["bitcoin"]["eur"], data["dogecoin"]["eur"], data["ethereum"]["eur"]]

current_hashrate /= 1000000

minute = 60
heure = minute*60
jour = heure*24
semaine = jour*7
mois = (365.25/12)*jour
an = mois*12

earnings = []
for i, (network_power, reward, price) in enumerate(zip(network_powers, rewards, prices)):
    currency_gain = reward * (current_hashrate / network_power)
    earnings.append(currency_gain * float(price))

max_index = earnings.index(max(earnings))

print("\n---------------------------\n\n{} est la crypto-monnaie la plus rentable à exploiter.\n{} € de revenu par bloc.\n".format(names[max_index], earnings[max_index]))

earnings_second = earnings[max_index] / (5*minute)
print("Soit environ :")
print(str(earnings_second*heure) + " € / heure")
print(str(earnings_second*jour) + " € / jour")
print(str(earnings_second*semaine) + " € / semaine")
print(str(earnings_second*mois) + " € / mois")
print(str(earnings_second*an) + " € / an")

input("Appuyez sur la touche Entrée pour fermer la fenêtre.")