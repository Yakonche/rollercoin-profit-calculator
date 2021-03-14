<p align="center"><img width=85 height=105 src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Rollercoin Profit Calculator</h1>

<p align="center"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square"> <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square"> <img alt="GitHub" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square"></p>

About
-----

Calculator that allows you to determine which cryptocurrency is the most profitable to "mine" on the rollercoin.com site
This calculator will also give an estimate of income at every hour / day / week / month / year, based on the duration of a block (approximately 5 min)

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111032926-f7fe9f80-840e-11eb-8090-e61cdb20f08b.png"/></p>

Downloads
---------

[Release 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/download/0.0.5/rollercoin-profit-calculator.zip)

Running from Python sources
---------------------------

### Requirements

* Python 3.7 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Save as then enter the following command : python get-pip.py
* Python 3 dependencies - `pip install -r requirements.txt`

### Running

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Building
--------

You can build a binary release for distribution with the command :

`python setup.py build`

Translation
-----------

The relevant commands for managing the templates are :

`python setup.py extract_messages` - Pulls all the target strings out of the codebase to produce `pot` file

`python setup.py update_catalogs` - Updates the generated `po` files, use when strings change

`python setup.py compile_catalogs` - Compiles just the translation files, yields `mo` files

Additionally `python setup.py build` will now compile translations and copy them into the build.



Original source : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
