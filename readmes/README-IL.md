<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">מחשבון רווח של Rollercoin</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

### READMES בשפות אחרות

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

על אודות
--------

( Note : This is a translation done via Google Translate, so please excuse me for any errors you might read there. )

מחשבון המאפשר לכם לקבוע איזו מטבע קריפטוגרפי הכי משתלם "לכרות" באתר rollercoin.com.
מחשבון זה ייתן גם אומדן הכנסה בכל שעה / יום / שבוע / חודש / שנה, בהתבסס על משך החסימה (כ -5 דקות).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

הורדות
-------

[גִרְסָה 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>גרסאות ישנות</summary>
* [גִרְסָה 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

פועל ממקורות פייתון
---------------------

### דרישות

* פייתון 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) "שמור בשם" ואז הזן את הפקודה הבאה : `python get-pip.py`
* תלות בפייתון 3 - `pip install -r requirements.txt`

### רץ

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

בִּניָן
-----

אתה יכול לבנות מהדורה בינארית להפצה באמצעות הפקודה :

`python setup.py build`

תִרגוּם
------

### בנה תרגום

הפקודות הרלוונטיות לניהול התבניות הן :

`python setup.py extract_messages` - שולף את כל מיתרי היעד מבסיס הקוד כדי לייצר קובץ `.pot`

`python setup.py update_catalogs` - מעדכן את קבצי ה- `.po` שנוצרו, השתמשו בהם כאשר המחרוזות משתנות

`python setup.py compile_catalogs` - אוסף רק את קבצי התרגום, מניב קבצי `.mo`

אתה יכול גם לכתוב את הפקודה הבאה :

`python setup.py extract_messages update_catalogs compile_catalogs` על מנת לבצע את 3 הפקודות.

בנוסף, `python setup.py build` ירכיב כעת תרגומים ועתיק אותם לבנות.



מקור מקורי : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
