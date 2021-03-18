<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Rollercoin Kar Hesaplayıcı</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

### OKUMALAR diğer dillerde

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
</p>

Hakkında
--------

Eğer rollercoin.com web sitesinde "mayın" için en karlı olan cryptocurrency belirlemenize olanak sağlar Hesaplama.
Bu hesap da bir blok (yaklaşık 5 dakika) süresine göre, her saat / gün / hafta / ay / yıl gelir tahminini verecektir.

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

İndirilenler
------------
[Sürüm 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>Eski sürümler</summary>
* [Sürüm 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Python kaynaklarından çalıştırma
--------------------------------

### Gereksinimler


* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Farklı kaydedin ve ardından aşağıdaki komutu girin : `python get-pip.py`
* Python 3 bağımlılıkları - `pip install -r requirements.txt`


### Çalıştırma

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Oluşturma
---------

Şu komutla dağıtım için bir ikili yayın oluşturabilirsiniz:

`python setup.py build`

Tercüme
-------
### Çeviri oluştur

Şablonları yönetmek için ilgili komutlar şunlardır:

`python setup.py extract_messages` - `Pot` dosyası oluşturmak için tüm hedef dizeleri kod tabanından çeker

`python setup.py update_catalogs` -  Oluşturulan `pot` dosyalarını günceller, dizeler değiştiğinde kullanın

`python setup.py compile_catalogs` - Yalnızca çeviri dosyalarını derler, `mo` dosyaları verir

Ayrıca aşağıdaki komutu da yazabilirsiniz :

`python setup.py extract_messages update_catalogs compile_catalogs` - 3 komutu gerçekleştirmek için.

Bunlara ek olarak, `python setup.py build` şimdi çevirileri derleyecek ve bunları yapıya kopyalayacaktır.



Orjinal kaynak : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
