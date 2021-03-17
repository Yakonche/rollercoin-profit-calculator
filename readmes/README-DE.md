<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Rollercoin Gewinnrechner</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

### READMES in anderen Sprachen

<p align="center">
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
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-PL.md">
    <img alt="Polish" src="https://user-images.githubusercontent.com/60564904/111509351-ee49a480-874c-11eb-9205-04cc7ed5eaaf.png">
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
