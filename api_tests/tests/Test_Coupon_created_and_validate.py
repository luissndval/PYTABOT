import allure
import pytest

from api_tests.data.data_body.create_coupon_body import coupon_create
from api_tests.endpoints.create_coupon import create_coupon


@pytest.mark.parametrize("json_data, comentario", [(coupon_create, "\n --->> Test 200 ok")])
@allure.title("Clerk Response: 200 ok")
@allure.feature("Create Get and validate coupon Clerk")
@allure.story("Create Get and validate coupon")
@allure.description("-------")
def test_Clerk(json_data,comentario):
    print("\n")
    print(f"Clerk: Create Get and validate coupon --->> {comentario}")
    Enviroment = "QA"
    response = create_coupon.create_coupon(Enviroment, json_data=json_data)
    response_body = response["response_body"]
    response_code = response["status_code"]
    assert response_code >= 200
    assert response_body is not None

