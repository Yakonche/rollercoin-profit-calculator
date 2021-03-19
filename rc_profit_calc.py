#!/usr/bin/python

import json
import urllib.request
import os
import sys
import decimal

from sty import fg
if sys.platform == "win32":
    os.system('color')

import gettext
gettext.bindtextdomain('rc_profit_calc', 'locale')
gettext.textdomain('rc_profit_calc')
gettext.install('rc_profit_calc', 'locale')
_ = gettext.gettext

print("")

langs = [
    {
        "name": " English    (United States) ",
        "code": "en_US"
    },
    {
        "name": " English    (Britain)       ",
        "code": "en_GB"
    },
    {
        "name": " English    (Canada)        ",
        "code": "en_CA"
    },
    {
        "name": " English    (Australia)     ",
        "code": "en_AU"
    },
    {
        "name": " English    (New Zealand)   ",
        "code": "en_NZ"
    },
    {
        "name": " Français   (France)        ",
        "code": "fr_FR"
    },
    {
        "name": " Français   (Suisse)        ",
        "code": "fr_CH"
    },
    {
        "name": " Français   (Canada)        ",
        "code": "fr_CA"
    },
    {
        "name": " Deutsche   (Deutsche)      ",
        "code": "de_DE"
    },
    {
        "name": "Español    (España)        ",
        "code": "es_ES"
    },
    {
        "name": "Español    (México)        ",
        "code": "es_MX"
    },
    {
        "name": "Español    (Venezuela)     ",
        "code": "es_VE"
    },
    {
        "name": "Español    (Argentina)     ",
        "code": "es_AR"
    },
    {
        "name": "Polski     (Polska)        ",
        "code": "pl_PL"
    },
    {
        "name": "Português  (Portugal)      ",
        "code": "pt_PT"
    },
    {
        "name": "Português  (Brasil)        ",
        "code": "pt_BR"
    },
    {
        "name": "Türk       (Türkiye)       ",
        "code": "tr_TR"
    },
    {
        "name": "Pусский    (Россия)        ",
        "code": "ru_RU"
    },
    {
        "name": "Pilipino   (Pilipinas)     ",
        "code": "fil_PH"
    }
]

ctx = decimal.Context()
ctx.prec = 10

minute = 60
hour = minute * 60
day = hour * 24
week = day * 7
month = (365.25 / 12) * day
year = month * 12

def float2str(f):
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')

def configure_language():
    selected_lang = 0

    while True:
        for idx, lang in enumerate(langs):
            print(
                "\t{}: {} ({})".format(idx + 1, lang['name'], lang['code'])
            )
        lang = input("\n Select a language [default - 1] : ") or "1"

        try:
            lang_idx = int(lang) - 1
            if len(langs) > lang_idx >= 0:
                selected_lang = lang_idx
                break
            else:
                print(" Invalid selection, try again\n")

        except ValueError:
            print(" Please input a number, try again\n")

    lang = gettext.translation(
        'rc_profit_calc', 'locale', [langs[selected_lang]['code']]
    )
    lang.install()
    os.environ['LANGUAGE'] = langs[selected_lang]['code']

def main():
    current_hashrate = float(input(_("\n Enter your hashrate (TH/s) : ")))
    current_hashrate /= 1000000
    currency_code = _("usd")
    currency_sym = _("$")

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
        .format(currency_code)
    )
    data = json.loads(r.read())
    prices = [
        data["bitcoin" ][currency_code],
        data["dogecoin"][currency_code],
        data["ethereum"][currency_code]
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
        ).format(
        names[max_index], earnings[max_index], fg(0, 255, 0) + currency_sym
        + fg.rs, earnings_crypto[max_index], names[max_index]
        )
        )

    periods = [hour, day, week, month, year]
    period_names = [_("hour"), _("day"), _("week"), _("month"), _("year")]
    earnings_second = earnings[max_index] / (5 * minute)
    earnings_second_crypto = earnings_crypto[max_index] / (5 * minute)

    print(_(" This is around :"))

    for period, period_name in zip(periods, period_names):
        print(
            _(" {:.2f} {} per {}, or {} {}")
            .format(
                earnings_second * period, fg(0, 255, 0) + currency_sym + fg.rs,
                period_name, earnings_second_crypto * period, names[max_index]
            )
        )

if __name__ == "__main__":
    configure_language()
    main()
    input(_("\n Press the Enter key to close the window. "))
