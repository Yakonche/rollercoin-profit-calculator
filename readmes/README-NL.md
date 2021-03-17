<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Rollercoin Winstcalculator</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

Over
----

( Note : This is a translation done via Google Translate, so please excuse me for any errors you might read there. )

Rekenmachine waarmee u kunt bepalen welke cryptocurrency het meest winstgevend is om te "minen" op de website rollercoin.com.
Deze calculator geeft ook een schatting van het inkomen op elk uur / dag / week / maand / jaar, gebaseerd op de duur van een blok (ongeveer 5 min).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

Downloads
---------

[Versie 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>Oude versie</summary>
* [Versie 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Uitgevoerd vanaf Python-bronnen
-------------------------------

### Voorwaarden

* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Opslaan als en voer de volgende opdracht in : `python get-pip.py`
* Python 3-afhankelijkheden - `pip install -r requirements.txt`

### Rennen

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Gebouw
------

U kunt een binaire uitgave bouwen voor distributie met het commando :

`python setup.py build`

Vertaling
---------

### Bouw een vertaling

De relevante commando's voor het beheren van de sjablonen zijn :

`python setup.py extract_messages` - Trekt alle doelstrings uit de codebase om het `pot`-bestand te produceren

`python setup.py update_catalogs` - Werkt de gegenereerde `po` bestanden bij, gebruik deze wanneer strings veranderen

`python setup.py compile_catalogs` - Compileert alleen de vertaalbestanden, levert `mo` bestanden op

U kunt ook de volgende opdracht schrijven :

`python setup.py extract_messages update_catalogs compile_catalogs` om de 3 opdrachten uit te voeren.

Bovendien zal `python setup.py build` nu vertalingen compileren en naar de build kopiëren.



Originele bron : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
