import unicodedata
import decimal

ctx = decimal.Context()
ctx.prec = 10


def len_display(s):
    return sum(1 + (unicodedata.east_asian_width(c) in "WF") for c in s)


def float2str(f):
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')
