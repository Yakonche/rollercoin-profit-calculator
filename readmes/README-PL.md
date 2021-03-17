<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Kalkulator zysków Rollercoin</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

O
-

( Note : This is a translation done via Google Translate, so please excuse me for any errors you might read there. )

Kalkulator pozwalający określić, która kryptowaluta jest najbardziej opłacalna do „wydobycia” na stronie rollercoin.com.
Kalkulator ten poda również szacunkowy dochód o każdej godzinie / dniu / tygodniu / miesiącu / roku na podstawie czasu trwania bloku (około 5 minut).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

Pliki do pobrania
-----------------

[Wersja 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>Stare wersje</summary>
* [Wersja 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Uruchamianie ze źródeł Pythona
------------------------------

### Wymagania

* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Zapisz jako, a następnie wprowadź następujące polecenie : `python get-pip.py`
* Zależności Python 3 - `pip install -r requirements.txt`

### Bieganie

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Budynek
-------

Możesz zbudować wersję binarną do dystrybucji za pomocą polecenia :

`python setup.py build`

Tłumaczenie
-----------

### Twórz tłumaczenia

Odpowiednie polecenia do zarządzania szablonami to :

`python setup.py extract_messages` - Wyciąga wszystkie ciągi znaków docelowych z bazy kodu, aby utworzyć plik `pot`

`python setup.py update_catalogs` - Aktualizuje wygenerowane pliki `po`, używane, gdy zmieniają się ciągi znaków

`python setup.py compile_catalogs` - Kompiluje tylko pliki tłumaczeń, daje pliki `mo`

Możesz również napisać następujące polecenie:

`python setup.py extract_messages update_catalogs compile_catalogs` w celu wykonania 3 poleceń.

Dodatkowo, `python setup.py build` będzie teraz kompilować tłumaczenia i kopiować je do kompilacji.



Pierwotnym źródłem : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
