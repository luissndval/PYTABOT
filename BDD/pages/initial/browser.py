import time

from BDD.data.country_brand import country
from _pom.front.front import functions


class browser(functions):
    global pais

    def start_browser(self, country_code, brand):
        try:
            self.pais = country_code
            functions.driver_Firefox(self)
            time.sleep(3)
            # Obtener la información de países y marcas desde el módulo country
            countries_data = country

            # Bucle para recorrer la información de países y marcas
            for country_key, brands_urls in countries_data.items():
                if country_code.lower() == country_key.lower():
                    # Verificar si la marca está presente en el país
                    if brand in brands_urls:
                        url = brands_urls[brand]
                        functions.browser(self, url)
                        break  # Salir del bucle si la marca es encontrada

            functions.max(self)
            time.sleep(3)
        except Exception as e:
            print("Error:", e)
            raise
    def get_country(self):
        return self.pais