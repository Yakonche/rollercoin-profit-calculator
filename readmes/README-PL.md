<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Kalkulator zysków Rollercoin</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

### READMES w innych językach

<p align="center">
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-DE.md">
    <img alt="German" src="https://user-images.githubusercontent.com/60564904/111507817-56978680-874b-11eb-8fb2-c66eca9683ec.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-ES.md">
    <img alt="Spanish" src="https://user-images.githubusercontent.com/60564904/111508987-90b55800-874c-11eb-92ec-1d9fcbaf61b6.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-FR.md">
    <img alt="French" src="https://user-images.githubusercontent.com/60564904/111509055-9f9c0a80-874c-11eb-851d-f82deebaa5c7.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/README.md">
    <img alt="English" src="https://user-images.githubusercontent.com/60564904/111509126-b3477100-874c-11eb-9d87-0f484dfa3ff6.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-IL.md">
    <img alt="Israel" src="https://user-images.githubusercontent.com/60564904/111509190-c4907d80-874c-11eb-85fd-9b3fe8e8632a.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-NL.md">
    <img alt="Dutch" src="https://user-images.githubusercontent.com/60564904/111509270-da05a780-874c-11eb-9b81-38ec888946dc.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-PH.md">
    <img alt="Philippines" src="https://user-images.githubusercontent.com/60564904/111509315-e427a600-874c-11eb-8e73-88d67a15c139.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-PT.md">
    <img alt="Portuguese" src="https://user-images.githubusercontent.com/60564904/111509380-f73a7600-874c-11eb-8a88-6663d90e0f7f.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-RU.md">
    <img alt="Russian" src="https://user-images.githubusercontent.com/60564904/111509415-002b4780-874d-11eb-99d3-f877f9744746.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-TR.md">
    <img alt="Turkish" src="https://user-images.githubusercontent.com/60564904/111509458-0ae5dc80-874d-11eb-81ae-3a4775e11df5.png">
  </a>
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
