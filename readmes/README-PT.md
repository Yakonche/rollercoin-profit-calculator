<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Calculadora de lucro Rollercoin</h1>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/yakonche/rollercoin-profit-calculator?style=flat-square&color=00b16a">
  <img alt="Downloads" src="https://img.shields.io/github/downloads/yakonche/rollercoin-profit-calculator/total?style=flat-square&color=0055A4">
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yakonche/rollercoin-profit-calculator?style=flat-square&color=FFFFFF">
  <img alt="License" src="https://img.shields.io/github/license/yakonche/rollercoin-profit-calculator?style=flat-square&color=EF4135">
  <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/yakonche/rollercoin-profit-calculator/badge?style=flat-square"/>
</p>

Sobre
-----

( Note : This is a translation done via Google Translate, so please excuse me for any errors you might read there. )

Calculadora que permite determinar qual criptomoeda é a mais lucrativa para "minerar" no site rollercoin.com.
Esta calculadora também fornecerá uma estimativa da renda a cada hora / dia / semana / mês / ano, com base na duração de um bloco (aproximadamente 5 min).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

Transferências
--------------

[Versão 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>Versões antigas</summary>
* [Versão 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Executando a partir de fontes Python
------------------------------------

### Requisitos

* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Salve como e digite o seguinte comando : `python get-pip.py`
* Dependências do Python 3 - `pip install -r requirements.txt`

### Correndo

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Prédio
------

Você pode construir uma versão binária para distribuição com o comando :

`python setup.py build`

Tradução
--------

### Construir tradução

Os comandos relevantes para gerenciar os modelos são:

`python setup.py extract_messages` - Retira todas as strings de destino da base de código para produzir o arquivo `pot`

`python setup.py update_catalogs` - Atualiza os arquivos `po` gerados, use quando as strings mudam

`python setup.py compile_catalogs` - Compila apenas os arquivos de tradução, produz arquivos `mo`

Você também pode escrever o seguinte comando:

`python setup.py extract_messages update_catalogs compile_catalogs` para executar os 3 comandos.

Além disso, `python setup.py build` irá agora compilar as traduções e copiá-las para o build.



Fonte original : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
