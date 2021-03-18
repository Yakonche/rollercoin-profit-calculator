<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Calculateur de Profit pour Rollercoin</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

### READMES dans d'autres langues

<p align="center">
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-DE.md">
    <img alt="German" src="https://user-images.githubusercontent.com/60564904/111507817-56978680-874b-11eb-8fb2-c66eca9683ec.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-ES.md">
    <img alt="Spanish" src="https://user-images.githubusercontent.com/60564904/111508987-90b55800-874c-11eb-92ec-1d9fcbaf61b6.png">
  </a>
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/README.md">
    <img alt="English" src="https://user-images.githubusercontent.com/60564904/111509126-b3477100-874c-11eb-9d87-0f484dfa3ff6.png">
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

À propos
--------

Calculatrice qui vous permet de déterminer quelle crypto-monnaie est la plus rentable à «miner» sur le site rollercoin.com.
Ce calculateur donnera également une estimation du revenu à chaque heure / jour / semaine / mois / année, en fonction de la durée d'un bloc (environ 5 min).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

Téléchargements
---------------

[Release 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>Old releases</summary>
* [Release 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Exécution à partir des sources Python
-------------------------------------

### Exigences

* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Enregistrer sous, puis entrez la commande suivante : `python get-pip.py`
* Dépendances de Python 3 - `pip install -r requirements.txt`

### Fonctionnement

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Building
--------

Vous pouvez créer une version binaire pour la distribution avec la commande :

`python setup.py build`

Traduction
----------

### Traduction du build

Les commandes pertinentes pour la gestion des modèles sont :

`python setup.py extract_messages` - Extrait toutes les chaînes cibles de la base de code pour produire le fichier `.pot`

`python setup.py update_catalogs` - Met à jour les fichiers `.po` générés, à utiliser lorsque les chaînes changent

`python setup.py compile_catalogs` - Compile uniquement les fichiers de traduction, donne les fichiers `.mo`

Vous pouvez également taper la commande suivante :

`python setup.py extract_messages update_catalogs compile_catalogs` afin d'exécuter les 3 commandes dans l'ordre.

De plus, `python setup.py build` compilera désormais les traductions et les copiera dans le build.



Source originale : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
