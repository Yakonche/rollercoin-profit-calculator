<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Rollercoin Gewinnrechner</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

Über
----

( Note : This is a translation done via Google Translate, so please excuse me for any errors you might read there. )

Rechner, mit dem Sie bestimmen können, welche Kryptowährung auf der Website rollercoin.com am rentabelsten ist, um sie abzubauen.
Dieser Rechner gibt auch eine Schätzung des Einkommens zu jeder Stunde / Tag / Woche / Monat / Jahr basierend auf der Dauer eines Blocks (ca. 5 Minuten).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

Downloads
---------

[Veröffentlichung 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>Alte Veröffentlichungen</summary>
* [Veröffentlichung 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Laufen aus Python-Quellen
-------------------------

### Bedarf

* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Speichern unter und geben Sie den folgenden Befehl ein : `python get-pip.py`
* Python 3 Abhängigkeiten - `pip install -r requirements.txt`

### Laufen

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Gebäude
-------

Sie können eine binäre Version für die Verteilung mit dem folgenden Befehl erstellen :

`python setup.py build`

Übersetzung
-----------

### Übersetzung erstellen

Die relevanten Befehle zum Verwalten der Vorlagen sind :

`python setup.py extract_messages` - Zieht alle Zielzeichenfolgen aus der Codebasis heraus, um eine Pot-Datei zu erstellen

`python setup.py update_catalogs` - Aktualisiert die generierten `po`-Dateien und wird verwendet, wenn sich Zeichenfolgen ändern

`python setup.py compile_catalogs` - Kompiliert nur die Übersetzungsdateien und ergibt `mo`-Dateien

Sie können auch den folgenden Befehl schreiben :

`python setup.py extract_messages update_catalogs compile_catalogs` um die 3 Befehle auszuführen .

Zusätzlich kompiliert `python setup.py build` jetzt Übersetzungen und kopiert sie in den Build.



Originalquelle : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
