<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Калькулятор прибыли Rollercoin</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

### ЧИТАЙТЕ на других языках

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
  <a href="https://github.com/Yakonche/rollercoin-profit-calculator/blob/master/readmes/README-TR.md">
    <img alt="Turkish" src="https://user-images.githubusercontent.com/60564904/111509458-0ae5dc80-874d-11eb-81ae-3a4775e11df5.png">
  </a>
</p>

О
-

( Note : This is a translation done via Google Translate, so please excuse me for any errors you might read there. )

Калькулятор, позволяющий определить, какую криптовалюту выгоднее всего «майнить» на сайте Rollercoin.com.
Этот калькулятор также дает оценку дохода каждый час / день / неделю / месяц / год в зависимости от продолжительности блока (примерно 5 минут).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

Загрузки
--------

[Версия 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>Старые версии</summary>
* [Версия 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Запуск из источников Python
---------------------------

### Требования

* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Сохранить как, затем введите следующую команду : `python get-pip.py`
* Зависимости Python 3 - `pip install -r requirements.txt`

### Бег

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Строительство
-------------

Вы можете собрать двоичный выпуск для распространения с помощью команды :

`python setup.py build`

Перевод
-------

### Создать перевод

Соответствующие команды для управления шаблонами:

`python setup.py extract_messages` - извлекает все целевые строки из кодовой базы для создания файла `pot`

`python setup.py update_catalogs` - обновляет сгенерированные файлы `po`, используется при изменении строк

`python setup.py compile_catalogs` - Компилирует только файлы перевода, выдает файлы `mo`

Вы также можете написать следующую команду:

`python setup.py extract_messages update_catalogs compile_catalogs`, чтобы выполнить 3 команды.

Кроме того, `python setup.py build` теперь будет компилировать переводы и копировать их в сборку.



Первоисточник : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
