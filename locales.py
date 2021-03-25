import gettext
import os

from utils import len_display

gettext.bindtextdomain('rc_profit_calc', 'locale')
gettext.textdomain('rc_profit_calc')
gettext.install('rc_profit_calc', 'locale')
_ = gettext.gettext

console_width = 120

langs = [
    {"name": "English", "code": "en_US"},
    {"name": "Français", "code": "fr_FR"},
    {"name": "Deutsche", "code": "de_DE"},
    {"name": "Español", "code": "es_ES"},
    {"name": "Polski", "code": "pl_PL"},
    {"name": "Português", "code": "pt_PT"},
    {"name": "Türk", "code": "tr_TR"},
    {"name": "Pусский", "code": "ru_RU"},
    {"name": "Pilipino", "code": "fil_PH"}
]


def install_language(code):
    lang = gettext.translation(
        'rc_profit_calc', 'locale', [code]
    )
    lang.install()
    os.environ['LANGUAGE'] = code


def get_language():
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

    return langs[selected_lang]['code']


def get_currency():
    from data import currencies_fiat, currencies_crypto
    options = [curr['code'] for curr in currencies_crypto + currencies_fiat]

    while True:
        print(_("\nFiat currencies :"))
        for idx, curr in enumerate(currencies_fiat):
            cell_str = _("{}: {} ({})").format(curr['code'], curr['name'], curr['sym'])
            cell_padding = int(console_width / 2 - len_display(cell_str.strip()))

            print(
                cell_str.strip() + (" " * cell_padding),
                end="" if idx != len(currencies_fiat) - 1 else "\n"
            )
            if idx % 2:
                print()  # \n

        print(_("\nCrypto currencies :"))
        for idx, curr in enumerate(currencies_crypto):
            cell_str = _("{}: {} ({})").format(
                curr['code'].ljust(4, " "), curr['name'], curr['sym']
            )
            cell_padding = int(console_width / 2 - len_display(cell_str.strip()))

            print(
                cell_str.strip() + (" " * cell_padding),
                end="" if idx != len(currencies_crypto) - 1 else "\n"
            )
            if idx % 2:
                print()  # \n

        selected_currency = input(_("\nSelect a currency [default - USD] : ")) or "USD"
        if selected_currency not in options:
            print(_("\nInvalid currency!\n"))
            continue
        break

    return [curr for curr in currencies_crypto + currencies_fiat if curr['code'] == selected_currency][0]
