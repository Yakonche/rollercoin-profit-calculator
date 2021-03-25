import gettext

_ = gettext.gettext



currencies_fiat = [
    {"code": "AUD", "name": _("Australian Dollar")         , "sym": "$"   },
    {"code": "CAD", "name": _("Canadian Dollar")           , "sym": "$"   },
    {"code": "GBP", "name": _("British Pound Sterling")    , "sym": "£"   },
    {"code": "NZD", "name": _("New Zealand Dollar")        , "sym": "$"   },
    {"code": "USD", "name": _("United States Dollar")      , "sym": "$"   },
    {"code": "ARS", "name": _("Argentine Peso")            , "sym": "$"   },
    {"code": "MXN", "name": _("Mexican Peso")              , "sym": "$"   },
    {"code": "VEF", "name": _("Venezuelan Bolivar Fuerte") , "sym": "B$"  },
    {"code": "BRL", "name": _("Brazil Real")               , "sym": "R$"  },
    {"code": "PHP", "name": _("Philippine Peso")           , "sym": "₱"   },
    {"code": "RUB", "name": _("Russian Ruble")             , "sym": "₽"   },
    {"code": "CHF", "name": _("Swiss Franc")               , "sym": "CHF" },
    {"code": "PLN", "name": _("Polish Zloty")              , "sym": "zł"  },
    {"code": "TRY", "name": _("Turkish Lira")              , "sym": "₺"   },
    {"code": "EUR", "name": _("Euro")                      , "sym": "€"   },
    {"code": "NGN", "name": _("Nigerian Naira")            , "sym": "₦"   },
    {"code": "SGD", "name": _("Singapore Dollar")          , "sym": "S$"  },
    {"code": "DKK", "name": _("Danish Krone")              , "sym": "kr." },
    {"code": "MMK", "name": _("Burmese Kyat")              , "sym": "K"   },
    {"code": "THB", "name": _("Thai Baht")                 , "sym": "฿"   },
    {"code": "KRW", "name": _("South Korean Won")          , "sym": "₩"   },
    {"code": "JPY", "name": _("Japanese Yen")              , "sym": "¥"   },
    {"code": "CNY", "name": _("Chinese Yuan")              , "sym": "¥"   },
    {"code": "INR", "name": _("Indian Rupee")              , "sym": "₹"   },
    {"code": "ZAR", "name": _("South African Rand")        , "sym": "R"   },
    {"code": "SAR", "name": _("Saudi Riyal")               , "sym": "﷼"   },
    {"code": "BMD", "name": _("Bermudian Dollar")          , "sym": "$"   },
    {"code": "CLP", "name": _("Chilean Peso")              , "sym": "$"   },
    {"code": "HKD", "name": _("Hong Kong Dollar")          , "sym": "元"  },
    {"code": "MYR", "name": _("Malaysian Ringgit")         , "sym": "RM"  },
    {"code": "SEK", "name": _("Swedish Krona")             , "sym": "kr"  },
    {"code": "UAH", "name": _("Ukrainian Hryvnia")         , "sym": "₴"   },
    {"code": "XDR", "name": _("IMF Special Drawing Rights"), "sym": "SDR" },
    {"code": "CZK", "name": _("Czech Koruna")              , "sym": "Kč"  },
    {"code": "HUF", "name": _("Hungarian Forint")          , "sym": "Ft"  },
    {"code": "LKR", "name": _("Sri Lankan Rupee")          , "sym": "ூ" },
    {"code": "PKR", "name": _("Pakistani Rupee")           , "sym": "₨"   },
    {"code": "BDT", "name": _("Bangladeshi Taka")          , "sym": "৳"   },
    {"code": "ILS", "name": _("Israeli New Shekel")        , "sym": "₪"   },
    {"code": "NOK", "name": _("Norwegian Krone")           , "sym": "kr"  },
    {"code": "VND", "name": _("Vietnamese đồng")           , "sym": "₫/đ" },
    {"code": "IDR", "name": _("Indonesian Rupiah")         , "sym": "Rp"  },
    {"code": "TWD", "name": _("New Taiwan Dollar")         , "sym": "圓"  },
    {"code": "KWD", "name": _("Kuwaiti Dinar")             , "sym": "د.ك" },
    {"code": "BHD", "name": _("Bahraini Dinar")            , "sym": ".د.ب"}
]

currencies_crypto = [
    {"code": "BTC" , "name": "Bitcoin"                 , "sym": "₿"   },
    {"code": "BNB" , "name": "Binance Coin"            , "sym": "BNB" },
    {"code": "LINK", "name": "Chainlink"               , "sym": "LINK"},
    {"code": "ETH" , "name": "Ether"                   , "sym": "Ξ"   },
    {"code": "EOS" , "name": "EOS"                     , "sym": "ε"   },
    {"code": "DOT" , "name": "Polkadot"                , "sym": "DOT" },
    {"code": "BITS", "name": "Bits (100 satoshis)"     , "sym": "bits"},
    {"code": "XLM" , "name": "Lumens"                  , "sym": "XLM" },
    {"code": "BCH" , "name": "Bitcoin Cash"            , "sym": "Ƀ"   },
    {"code": "YFI" , "name": "Yearn.finance"           , "sym": "YFI" },
    {"code": "LTC" , "name": "Litecoin"                , "sym": "Ł"   },
    {"code": "SATS", "name": "Satoshi (0,00000001 BTC)", "sym": "sat" },
    {"code": "XRP" , "name": "XRP"                     , "sym": "✕"   }
]
