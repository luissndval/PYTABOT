import json
import logging
import os
import random
from datetime import datetime
from urllib.parse import urlencode

import allure
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def handle_request_exception(e, response):
    global status_code, response_body
    response_type = "error"
    json_data = None
    print("----->>> Error in request: ", e)

    if isinstance(e, requests.exceptions.HTTPError):
        status_code = response.status_code  # Capturar el código de estado
        print("----->>> Status code: ", status_code)
        response_body = response.content.decode('utf-8')
        json_data = response_body  # Asignar el contenido de la respuesta como json_data

    return {
        "response_type": response_type,
        "response_data": json_data,
        "status_code": status_code,
        "response_body": response_body  # Incluir el código de estado en el diccionario de retorno
    }


class Apis:
    def __init__(self, initial_id=1):
        self.current_id = initial_id

    @staticmethod
    def read_json(nombre_archivo):
        # Obtener la ruta principal del proyecto
        ruta_principal = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Construir la ruta completa al archivo JSON en la carpeta "data"
        ruta_json = os.path.join(ruta_principal, 'data', nombre_archivo)
        try:
            with open(ruta_json, 'r') as archivo:
                datos = json.load(archivo)
            return datos
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no fue encontrado en la carpeta 'data'.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error al decodificar el archivo JSON: {str(e)}")
            return None

    @staticmethod
    def get_request_form_data(url, headers=None, data=None):
        response = None
        try:
            response = requests.get(url, headers=headers, data=data)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            response_body_request = response.content.decode('utf-8')
            status_code_request = response.status_code  # Capturar el status code de la respuesta
            return {"response_type": response_type,
                    "response_data": json_data,
                    'response_body_request': response_body_request,
                    'status_code_request': status_code_request,
                    "response": response}
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def get_request_url_encode(url, headers=None, params=None):
        response = None
        try:
            query_string = urlencode(params)
            full_url = f"{url}?{query_string}"
            response = requests.get(full_url, headers=headers)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            response_body_request = response.content.decode('utf-8')
            return {"response_type": response_type,
                    "response_body_request": response_body_request,
                    "response": response,
                    "json_data": json_data
                    }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def get_request_raw(url, headers=None, params=None):
        response = None
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            response_type = "success"
            response_body_request = response.content
            return {"response_type": response_type,
                    "response_body_request": response_body_request,
                    "response": response,
                    }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def get_request_binary(url, headers=None, params=None):
        response = None
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            response_type = "success"
            response_body_request = response.content
            return {"response_type": response_type,
                    "response_body_request": response_body_request,
                    "response": response,
                    }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def get_request_graphql(url, headers=None, data=None):
        response = None
        try:
            response = requests.get(url, headers=headers, data=data)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            print("Response JSON: %s", json_data)
            response_body_request = response.content.decode('utf-8')
            return {
                "response_type": response_type,
                "json_data": json_data,
                "response_body_request": response_body_request,
                "status_code": status_code
            }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def post_request(url, headers=None, data=None, json_data=None):
        try:
            response = requests.post(url, headers=headers, data=data, json=json_data)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            status_code_ = response.status_code  # Capturar el status code de la respuesta
            response_body_request = response.content.decode('utf-8')
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

        # Incluir el status code en el diccionario de retorno
        return {
            "response_type": response_type,
            "response_data": json_data,
            "response_body": response_body_request,
            "status_code": status_code_
        }

        # Incluir el status code en el diccionario de retorno
        return {
            "response_type": response_type,
            "response_data": json_data,
            "response_body": response_body,
            "status_code": status_code
        }

    @staticmethod
    def post_request_form_data(url, headers=None, files=None):
        response = None
        try:
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            response_body_request = response.content.decode('utf-8')
            return {"response_type": response_type,
                    "response_data": json_data,
                    'response_body_request': response_body_request,
                    "response": response}
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def post_request_url_encode(url, headers=None, params=None):
        response = None
        try:
            query_string = urlencode(params)
            response = requests.post(url, headers=headers, data=query_string)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            response_body_request = response.content.decode('utf-8')
            return {'response_type': response_type,
                    'response_data': json_data,
                    'response_body': response_body_request,
                    'response': response}
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

        return {"response_type": response_type, "response_data": json_data}

    @staticmethod
    def post_request_raw(url, headers=None, data=None):
        response = None
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            response_type = "success"
            print("Response Headers: %s", response.headers)
            response_body_request = response.content
            print("Response Body: %s", response_body)
            return {"response_type": response_type,
                    "response_body_request": response_body_request,
                    "response": response
                    }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def post_request_binary(url, headers=None, data=None):
        response = None
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            response_type = "success"
            print("Response Headers: %s", response.headers)

            response_body_request = response.content
            print("Response Body: %s", response_body)
            return {"response_type": response_type,
                    "response_body_request": response_body_request,
                    "response": response
                    }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def post_request_graphql(url, headers=None, data=None):
        response = None
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            print("Response JSON: %s", json_data)

            response_body_request = response.content.decode('utf-8')
            print("Response Body: %s", response_body)
            return {"response_type": response_type,
                    "response_body_request": response_body_request,
                    "response": response
                    }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def put_request(url, headers=None, data=None, json_data=None):
        response = None
        try:
            response = requests.put(url, headers=headers, data=data, json=json_data)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            print("Response JSON: %s", json_data)

            response_body_request = response.content.decode('utf-8')
            print("Response Body: %s", response_body)
            return {"response_type": response_type,
                    "response_body_request": response_body_request,
                    "response": response
                    }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def put_request_form_data(url, headers=None, data=None):
        response = None
        try:
            response = requests.put(url, headers=headers, data=data)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            print("Response JSON: %s", json_data)
            response_body_request = response.content.decode('utf-8')
            print("Response Body: %s", response_body)
            return {
                "response_type": response_type,
                "response_body_request": response_body_request,
                "response": response
            }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def put_request_url_encode(url, headers=None, params=None):
        response = None
        try:
            query_string = urlencode(params)
            response = requests.put(url, headers=headers, data=query_string)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            print("Response JSON: %s", json_data)
            response_body_request = response.content.decode('utf-8')
            print("Response Body: %s", response_body)
            return {"response_type": response_type,
                    "response_body_request": response_body_request,
                    "response": response
                    }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def put_request_raw(url, headers=None, data=None):
        response = None
        try:
            response = requests.put(url, headers=headers, data=data)
            response.raise_for_status()
            response_type = "success"
            print("Response Headers: %s", response.headers)
            response_body_request = response.content
            print("Response Body: %s", response_body)
            return {
                "response_type": response_type,
                "response_body_request": response_body_request,
                "response": response
            }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def put_request_binary(url, headers=None, data=None):
        response = None
        try:
            response = requests.put(url, headers=headers, data=data)
            response.raise_for_status()
            response_type = "success"
            print("Response Headers: %s", response.headers)
            response_body_request = response.content
            print("Response Body: %s", response_body)
            return {
                "response_type": response_type,
                "response_body_request": response_body_request,
                "response": response
            }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def Creacion_Reference_ID():
        global last_id
        try:
            # ruta_actual = os.path.abspath(__file__)
            # ruta_padre = os.path.dirname(os.path.dirname(ruta_actual))
            # ruta_txt = os.path.join(ruta_padre, 'src','data')
            ruta_padre = r"C:\ProgramData\Jenkins\.jenkins\workspace\DatesIncrementales"
            ruta_txt = os.path.join(ruta_padre)
            file_path = os.path.join(ruta_txt, 'ID-Operation.txt')

            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    last_id = file.read().strip()
            else:
                last_id = str(random.randint(3600025, 99999999))
                return last_id
        except Exception as e:
            print(f"Error getting last ID: {e}")
            return last_id

    @staticmethod
    def patch_request(url, headers=None, params=None, data=None):
        response = None
        try:
            response = requests.patch(url, headers=headers, params=params, data=data)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            response_body_request = response.content.decode('utf-8')
            return {"response_type": response_type,
                    "response_data": json_data,
                    "response_body_request": response_body_request
                    }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def patch_request_url_encode(url, headers=None, params=None, data=None):
        response = None
        try:
            query_string = urlencode(params)
            response = requests.patch(url, headers=headers, params=params, data=data)
            response.raise_for_status()
            json_data = response.json()
            response_type = "success"
            response_body_request = response.content.decode('utf-8')
            return {"response_type": response_type,
                    "response_data": json_data,
                    "response_body_request": response_body_request,
                    "query_string": query_string}
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def patch_request_raw(url, json_data, headers):
        response = None

        try:
            response = requests.patch(url, json=json_data, headers=headers)
            response.raise_for_status()
            response_type = "success"
            response_body_request = response.content.decode('utf-8')
            status_code_response = response.status_code
            return {
                "response_type": response_type,
                "response_data": response_body,
                "status_code_response": status_code_response,
                "response_body_request": response_body_request
            }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def delete_request_raw(url, headers=None, data=None):
        response = None

        try:
            response = requests.delete(url, headers=headers, data=data)
            response.raise_for_status()
            response_type = "success"
            print("Response Headers: %s", response.headers)
            response_body_request = response.content
            return {
                "response_type": response_type,
                "response_data": response_body,
                "status_code": status_code,
                "response_body_request": response_body_request
            }
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)

    @staticmethod
    def head_request(url, headers=None, params=None):
        response = None

        try:
            response = requests.head(url, headers=headers, params=params)
            response.raise_for_status()
            response_type = "success"
            print("Response Headers: %s", response.headers)
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)
        return {"response_type": response_type, "response": response}

    @staticmethod
    def head_request_url_encode(url, headers=None, params=None):
        response = None
        try:
            query_string = urlencode(params)
            full_url = f"{url}?{query_string}"
            response = requests.head(full_url, headers=headers)
            response.raise_for_status()
            response_type = "success"
            print("Response Headers: %s", response.headers)
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)
        return {"response_type": response_type}

    @staticmethod
    def head_request_raw(url, headers=None, data=None):
        response = None
        try:
            response = requests.head(url, headers=headers, data=data)
            response.raise_for_status()
            response_type = "success"
            print("Response Headers: %s", response.headers)
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)
        return {"response_type": response_type}

    @staticmethod
    def options_request(url, headers=None):
        response = None
        try:
            response = requests.options(url, headers=headers)
            response.raise_for_status()
            response_type = "success"
            print("Response JSON: %s", response.json())
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)
        return {"response_type": response_type}

    @staticmethod
    def options_request_url_encode(url, headers=None, params=None):
        response = None
        try:
            query_string = urlencode(params)
            full_url = f"{url}?{query_string}"
            response = requests.options(full_url, headers=headers)
            response.raise_for_status()
            response_type = "success"
            print("Response JSON: %s", response.json())
        except requests.exceptions.RequestException as e:
            return handle_request_exception(e, response)
        return {"response_type": response_type}

    @staticmethod
    def increment_id(current_id):
        try:
            new_id = int(current_id) + 1
            return str(new_id).zfill(len(current_id))
        except ValueError:
            print("Invalid ID format")
            return None

    @staticmethod
    def get_last_id():
        try:
            # Obtén la ruta del proyecto
            project_dir = r"C:\ProgramData\Jenkins\.jenkins\workspace\DatesIncrementales"
            file_path = rf"{project_dir}\ID-Operation.txt"
            with open(file_path, "r") as file:
                last_id_ = file.read().strip()
            return last_id_
        except FileNotFoundError:
            return "Documento no funciona"

    @staticmethod
    def save_last_id(new_last_id):
        try:
            # Obtén la ruta del proyecto
            project_dir = r"C:\ProgramData\Jenkins\.jenkins\workspace\DatesIncrementales"
            file_path = rf"{project_dir}\ID-Operation.txt"

            with open(file_path, "w") as file:
                file.write(new_last_id)
        except Exception as e:
            print(f"Error saving last ID: {e}")

    @staticmethod
    def validate_json(json_data):
        def validate_fields(expected_datas, data, parent_key=""):
            for key, expected_type in expected_datas.items():
                if isinstance(expected_type, dict):
                    if key in data:
                        validate_fields(expected_type, data[key], parent_key=f"{parent_key}.{key}")
                    else:
                        print(f"Campo '{parent_key}.{key}' no encontrado en response_data")
                else:
                    if key in data:
                        value = data[key]
                        if expected_type is type(None):
                            if value is None or value.lower() >= "null":
                                print(f"Campo '{parent_key}.{key}' validado")
                            else:
                                print(
                                    f"Campo '{parent_key}.{key}' no tiene el tipo de dato esperado: {expected_type.__name__}")
                        elif isinstance(value, expected_type):
                            print(f"Campo '{parent_key}.{key}' validado")
                        else:
                            print(
                                f"Campo '{parent_key}.{key}' no tiene el tipo de dato esperado: {expected_type.__name__}")
                    else:
                        print(f"Campo '{parent_key}.{key}' no encontrado en response_data")

            if isinstance(json_data, dict):
                validate_fields(expected_datas, json_data)
            else:
                print("El JSON no es un diccionario válido.")

    @staticmethod
    def AddReport(response_bodys):
        allure.attach(response_bodys, "Response Body", allure.attachment_type.TEXT)

    @staticmethod
    def FechaFormat():
        fecha_Actual = datetime.now()
        fecha_formato = fecha_Actual.strftime("%Y-%m-%d %H:%M:%S")
        return fecha_formato


def delete_request(url, headers=None, params=None):
    response = None
    try:
        response = requests.delete(url, headers=headers, params=params)
        response.raise_for_status()
        json_data = response.json()
        response_type_request = "success"
        status_code_response = response.status_code
        response_body_request = response.content.decode('utf-8')
        print("Response Body:", response_body)
        return {
            "response_type": response_type_request,
            "response_data": json_data,
            "response_body_request": response_body_request,
            "status_code": status_code_response,
            "response": response
        }
    except requests.exceptions.RequestException as e:
        return handle_request_exception, (e, response)


def delete_request_url_encode(url, headers=None, params=None):
    response = None
    try:
        query_string = urlencode(params)
        full_url = f"{url}?{query_string}"
        response = requests.delete(full_url, headers=headers)
        response.raise_for_status()
        json_data = response.json()
        response_type = "success"
        response_body_request = response.content.decode('utf-8')
        return {"response_type": response_type,
                "response_body_request": response_body_request,
                "response": response,
                "json_data": json_data
                }
    except requests.exceptions.RequestException as e:
        return handle_request_exception(e, response)
