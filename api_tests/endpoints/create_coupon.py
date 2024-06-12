from _pom.api.type_request import Apis
from api_tests.data.enviroment.url import url
from api_tests.data.headers.create_coupon_header import Access_Token


class create_coupon(Apis):

    @staticmethod
    def create_coupon(Enviroment, json_data=None):
        try:
            Enviroments = {"QA": url['qa']}
            if Enviroment not in Enviroments:
                raise Exception("Ambiente no reconocido")

            url_init = Enviroments[Enviroment]
            url_path = f"{url_init}/api/couponCreate"
            print(f"Enpoint post {url_path}")
            headers = {
                "Authorization": Access_Token["Access"],
                "Content-Type": "application/json"}
            response = Apis.post_request(url_path, headers=headers, json_data=json_data)
            response_type = response["response_type"]
            response_body = response["response_body"]
            status_code = response["status_code"]

            if status_code >= 200:
                print(
                    "----------------------------------------------------------------------------------------------------""\n",
                    status_code)
                print(
                    "----------------------------------------------------------------------------------------------------""\n",
                    response_body)

            return {"response_type": response_type,
                    "response_body": response_body,
                    "status_code": status_code}
        except Exception as e:
            print("Error: ", e)
            raise
