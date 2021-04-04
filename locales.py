import gettext
import os

from utils import len_display

gettext.bindtextdomain('calculator', 'locale')
gettext.textdomain('calculator')
gettext.install('calculator', 'locale')
_ = gettext.gettext

console_width = 120

print("")

langs = [
    {"name": "English  ", "code": "en_US"},
    {"name": "Français ", "code": "fr_FR"},
    {"name": "Deutsche ", "code": "de_DE"},
    {"name": "Español  ", "code": "es_ES"},
    {"name": "Polski   ", "code": "pl_PL"},
    {"name": "Português", "code": "pt_PT"},
    {"name": "Türk     ", "code": "tr_TR"},
    {"name": "Pусский  ", "code": "ru_RU"},
    {"name": "Pilipino ", "code": "fil_PH"}
]


def install_language(code):
    lang = gettext.translation(
        'calculator', 'locale', [code]
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
    # Import is done late because the translation has to be installed first
    from data import currencies_fiat, currencies_crypto

    # Valid options, a list of every country code, pulled from the dicts
    options = [curr['code'] for curr in currencies_crypto + currencies_fiat]
#British Pound Sterling (£)
    # Spin until user picks a valid option
    while True:
        print(_(" Fiat currencies :"))
        print(" ┌────────┬───────────────────────────┬───────┬────────┬───────────────────────────┬───────┐")
        print(_(" │  code  │ name                      │symbol │  code  │ name                      │symbol │"))
        print(" ├────────┴───────────────────────────┴───────┼────────┴───────────────────────────┴───────┤")
        for idx, curr in enumerate(currencies_fiat):
            cell_str = _(" | - {} : {}  {}").format(
                curr['code'].ljust(4, " "),
                curr['name'].ljust(26, " "),
                curr['sym'].ljust(5 if len_display(curr['sym']) == len(curr['sym']) else 4, " ")
            )

            # Output the cell contents, end="" removes the newline from print
            print(cell_str, end="")
            # Add a newline only every second iteration because we have two
            # cells per row
            if idx % 2:
                print(" |")  # \n
        if not idx % 2:
            print(" |                                            |")
        print(" └────────────────────────────────────────────┴────────────────────────────────────────────┘")

        print(_(" Crypto currencies :"))
        print(" ┌────────┬───────────────────────────┬───────┬────────┬───────────────────────────┬───────┐")
        print(_(" │  code  │ name                      │symbol │  code  │ name                      │symbol │"))
        print(" ├────────┴───────────────────────────┴───────┼────────┴───────────────────────────┴───────┤")
        for idx, curr in enumerate(currencies_crypto):
            cell_str = _(" | - {} : {}  {}").format(
                curr['code'].ljust(4, " "),
                curr['name'].ljust(26, " "),
                curr['sym'].ljust(5, " ")
            )

            print(
                cell_str, end=""
            )
            if idx % 2:
                print(" |")  # \n
        if not idx % 2:
            print(" |                                            |")
        print(" └────────────────────────────────────────────┴────────────────────────────────────────────┘")

        # As the user to select from the displayed lists
        selected_currency = input(
            _("\n Select a currency [default - USD] : ")
        ) or "USD"

        # If the user's input wasn't in the list of options, go back to start
        # of `while True` loop
        if selected_currency not in options:
            print(_("\n Invalid currency!\n"))
            continue
        # We only reach the end if the user has picked a valid option
        # so we can break the `while True` at this point
        break

    # Lookup the selected code in `data.py`'s arrays, return the first matching
    # dict (always one match)
    return [
        curr for curr in currencies_crypto + currencies_fiat
        if curr['code'] == selected_currency
    ][0]
