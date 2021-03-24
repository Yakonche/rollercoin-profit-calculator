import unicodedata


def len_display(s):
    return sum(1 + (unicodedata.east_asian_width(c) in "WF") for c in s)
