#!/usr/bin/python

import json
import urllib.request
import os
import sys
import gettext

from locales import get_currency, get_language, install_language
from utils import float2str

from sty import fg
if sys.platform == "win32":
    os.system('color')

_ = gettext.gettext

minute = 60
hour = minute * 60
day = hour * 24
week = day * 7
month = (365.25 / 12) * day
year = month * 12


def main():
    print()  # \n
    currency = get_currency()

    current_hashrate = float(input(_("\n Enter your hashrate (TH/s) : ")))
    current_hashrate /= 1000000

    names = [
        fg(255, 128,  10) + "BTC"  + fg.rs,
        fg(255, 255,   0) + "DOGE" + fg.rs,
        fg(127,   0, 255) + "ETH"  + fg.rs
    ]

    default_rewards = [
        0.00009,
        240.0,
        0.0017
    ]

    print()  # \n
    network_powers = [
        float(input(
            _(" Enter the {} network power (EH/s) : ").format(name)
        )) for name in names
    ]

    print()  # \n
    rewards = [
        float(input(
        _(" Enter the {} reward [default - {}] : ")
        .format(name, float2str(default))) or default)
        for name, default in zip(names, default_rewards)
    ]

    r = urllib.request.urlopen(
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin%2Cdogecoin%2Cethereum&vs_currencies={}"
        .format(currency['code'])
    )
    data = json.loads(r.read())
    prices = [
        data["bitcoin" ][currency['code'].lower()],
        data["dogecoin"][currency['code'].lower()],
        data["ethereum"][currency['code'].lower()]
    ]

    earnings = []
    earnings_crypto = []
    input_zip = zip(network_powers, rewards, prices)
    for i, (network_power, reward, price) in enumerate(input_zip):
        currency_gain = reward * (current_hashrate / network_power)
        earnings.append(currency_gain * float(price))
        earnings_crypto.append(currency_gain)

    max_index = earnings.index(max(earnings))

    print("\n  --------------------------------------------\n")
    print(_(
        " {} is the most profitable cryptocurrency to mine.\n"
        " {:.2f} {} of income per block.\n Or {} {} per block.\n"
        ).format(names[max_index], earnings[max_index], fg(0, 255, 0) +
        currency['sym'] + fg.rs, earnings_crypto[max_index], names[max_index]))

    periods = [hour, day, week, month, year]
    period_names = [_("hour"), _("day"), _("week"), _("month"), _("year")]
    earnings_second = earnings[max_index] / (5 * minute)
    earnings_second_crypto = earnings_crypto[max_index] / (5 * minute)

    print(_(" This is around :"))

    for period, period_name in zip(periods, period_names):
        print(
            _(" {:.2f} {} per {}, or {} {}")
            .format(
                earnings_second * period,
                fg(0, 255, 0) + currency['sym'] + fg.rs, period_name,
                earnings_second_crypto * period, names[max_index]
            )
        )


if __name__ == "__main__":
    install_language(get_language())
    main()
    input(_("\n Press the Enter key to close the window. "))
