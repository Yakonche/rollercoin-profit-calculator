<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Rollercoin Profit Calculator</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

### READMES sa ibang mga wika

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

Tungkol sa
----------

( Note : This is a translation done via Google Translate, so please excuse me for any errors you might read there. )

Ang Calculator na nagbibigay-daan sa iyo upang matukoy kung aling cryptocurrency ang pinaka kumikitang "mine" sa website ng rollercoin.com.
Ang calculator na ito ay magbibigay din ng isang pagtatantya ng kita sa bawat oras / araw / linggo / buwan / taon, batay sa tagal ng isang bloke (humigit-kumulang na 5 minuto).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

Mga Pag-download
----------------

[Bersyon 0.1.2](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.2)

<details>
<summary>Mga Lumang Bersyon</summary>
* [Bersyon 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)
* [Bersyon 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Tumatakbo mula sa mga mapagkukunan ng Python
--------------------------------------------

### Mga Kinakailangan

* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) I-save habang ipasok ang sumusunod na utos : `python get-pip.py`
* Mga dependency sa Python 3 - `pip install -r requirements.txt`

### Tumatakbo

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Gusali
------

Maaari kang bumuo ng isang binary release para sa pamamahagi ng utos :

`python setup.py build`

Pagsasalin
----------

### Bumuo ng pagsasalin

Ang mga nauugnay na utos para sa pamamahala ng mga template ay:

`python setup.py extract_messages` - Kinukuha ang lahat ng mga target na string mula sa codebase upang makabuo ng `pot` file

`python setup.py update_catalogs` - Ina-update ang nabuong `po` na mga file, ginagamit kapag nagbago ang mga string

`python setup.py compile_catalogs` - Pinagsasama ang mga file ng pagsasalin, nagbubunga ng `mo` na mga file

Maaari mo ring isulat ang sumusunod na utos :

`python setup.py extract_messages update_catalogs compile_catalogs` upang maisagawa ang 3 utos.

Bilang karagdagan, ang `python setup.py build` ay mag-iipon ng mga pagsasalin at kopyahin ang mga ito sa build.



Orihinal na mapagkukunan : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
