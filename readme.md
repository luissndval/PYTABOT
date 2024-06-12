# PYTABOT Framework de Automatización

## Descripción
PYTABOT es un framework de automatización diseñado para facilitar la realización de pruebas automatizadas en múltiples plataformas:
- incluyendo APIs.
- aplicaciones móviles. 
- pruebas basadas en BDD.
Su estructura modular y extensible permite adaptarse a diferentes entornos y necesidades de pruebas.


## Características
- **Pruebas API**: Capacidad para crear y validar respuestas de API.
- **Pruebas Appium**: Automatización de pruebas en dispositivos móviles.
- **BDD**: Soporte para desarrollo dirigido por comportamiento.

## Requisitos
- Python 3.11
- Appium
- Pytest
- Otros módulos Python que se pueden instalar mediante `requirements.txt`.

## **Commands to run the tests**

**To run the test with allure report**
`behave -f allure_behave.formatter:AllureFormatter -o reports/ features/`

**To run the test without allure report** `behave features/`

**To generate the html allure report from the json files inside reports folder**
`allure serve reports/`# name report

Generar reporte:   allure generate reports --clean -o allure-report 

**Create VENV**

python -m venv nombre_del_venv
nombre_del_venv\Scripts\activate.bat
source nombre_del_venv/bin/activate
deactivate


## Instalación
Clona este repositorio y configura el entorno de pruebas:
```bash
git clone https://url_del_repositorio_del_framework.git
cd PYTABOT
pip install -r requirements.txt



