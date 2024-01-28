from src.ipay.services.c2b1 import C2BV2
from .domain_tests import i_pay_data2


def test_initiate_payment_1():
    c2b = C2BV2()
    response = c2b.initiate_payment(i_pay_data2)
    print(response)
    assert response["link"] is not None
