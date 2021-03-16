<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Rollercoin Profit Calculator</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=00b16a">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

About
-----

Calculator that allows you to determine which cryptocurrency is the most profitable to "mine" on the rollercoin.com website.
This calculator will also give an estimate of income at every hour / day / week / month / year, based on the duration of a block (approximately 5 min).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111032926-f7fe9f80-840e-11eb-8090-e61cdb20f08b.png"/></p>

Downloads
---------

[Release 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>Old releases</summary>
* [Release 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Running from Python sources
---------------------------

### Requirements

* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Save as then enter the following command : `python get-pip.py`
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

### Build translation

The relevant commands for managing the templates are :

`python setup.py extract_messages` - Pulls all the target strings out of the codebase to produce `pot` file

`python setup.py update_catalogs` - Updates the generated `po` files, use when strings change

`python setup.py compile_catalogs` - Compiles just the translation files, yields `mo` files

You can also write the following command :

`python setup.py extract_messages update_catalogs compile_catalogs` in order to perform the 3 commands.

Additionally, `python setup.py build` will now compile translations and copy them into the build.



Original source : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
