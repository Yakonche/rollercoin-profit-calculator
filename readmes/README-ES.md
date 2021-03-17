<p align="center"><img src="https://i.imgur.com/UnThSPW.png"/></p>

<h1 align="center">Calculadora de ganancias de Rollercoin</h1>

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

Calculadora que le permite determinar qué criptomoneda es la más rentable para "extraer" en el sitio web rollercoin.com.
Esta calculadora también dará una estimación de los ingresos cada hora / día / semana / mes / año, en función de la duración de un bloque (aproximadamente 5 min).

<p align="center"><img src="https://user-images.githubusercontent.com/60564904/111250612-ec2cfc00-860d-11eb-98f3-bc8beb837055.png"/></p>

Descargas
---------

[Versión 0.1.0](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.1.0)

<details>
<summary>Versión antigua</summary>
* [Versión 0.0.5](https://github.com/Yakonche/rollercoin-profit-calculator/releases/tag/0.0.5)
</details>

Ejecutando desde fuentes de Python
----------------------------------

### Requisitos

* Python 3.9 - (https://www.python.org/downloads)
* Pip - (https://bootstrap.pypa.io/get-pip.py) Guarde como y luego ingrese el siguiente comando : `python get-pip.py`
* Dependencias de Python 3 - `pip install -r requirements.txt`

### Corriendo

`git clone https://github.com/yakonche/rollercoin-profit-calculator.git`

`cd rollercoin-profit-calculator`

`pip install -r requirements.txt`

`python rc_profit_calc.py`

Construcción
------------

Puede crear una versión binaria para su distribución con el comando :

`python setup.py build`

Traducción
----------

### Construir traducción

Los comandos relevantes para administrar las plantillas son:

`python setup.py extract_messages` - Extrae todas las cadenas de destino del código base para producir el archivo `pot`

`python setup.py update_catalogs` - Actualiza los archivos `po` generados, se utilizan cuando cambian las cadenas

`python setup.py compile_catalogs` - Compila solo los archivos de traducción, produce archivos `mo`

También puede escribir el siguiente comando:

`python setup.py extract_messages update_catalogs compile_catalogs` para ejecutar los 3 comandos.

Además, `python setup.py build` ahora compilará las traducciones y las copiará en la compilación.



Fuente original : https://gist.github.com/Bilaboz/56572e81ace7b47d4302d6f5840118aa
