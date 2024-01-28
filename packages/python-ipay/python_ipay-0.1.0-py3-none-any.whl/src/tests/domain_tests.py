import json

from src.ipay.domain import IPayDataV2, IPayDataV1, MobileMoneyTransactionData, CardTriggerPayload

i_pay_data1 = IPayDataV2(
    live=0,
    oid="123456789",
    inv="123456789",
    ttl=100,
    tel="254712345678",
    eml="johndoe@email.com",
    vid="demo",
    curr="KES",
    p1="",
    p2="",
    p3="",
    p4="",
    cbk="http://localhost:8000/callback",
    cst="1",
    crl="0",
    secret_key="demo",
    hsh=""
)

i_pay_data2 = IPayDataV1(
    live=0,
    oid="123456789",
    inv="123456789",
    amount=100,
    tel="254712345678",
    eml="johndoe@email.com",
    vid="demo",
    curr="KES",
    cst=1,
    cbk="http://localhost:8000/api/v1/ipn",
    crl=0,
    hash_value="",
    auto_pay=1
)


def test_ipay_data_v1():
    assert i_pay_data1.to_map() == {
        "live": 0,
        "oid": "123456789",
        "inv": "123456789",
        "amount": 100,
        "tel": "254712345678",
        "eml": "johndoe@email.com",
        "vid": "demo",
        "curr": "KES",
        "p1": "123456789",
        "p2": "123456789",
        "p3": "123456789",
        "p4": "123456789",
        "cst": 1,
        "cbk": "http://localhost:8000/api/v1/ipn",
        "crl": 0,
        "hash": "",
        "autopay": 1
    }


def test_ipay_data_v2():
    assert i_pay_data2.to_map() == {
        "live": 0,
        "oid": "123456789",
        "inv": "123456789",
        "ttl": 100,
        "tel": "254712345678",
        "eml": "johndoe@email.com",
        "vid": "demo",
        "curr": "KES",
        "p1": "",
        "p2": "",
        "p3": "",
        "p4": "",
        "cbk": "http://localhost:8000/callback",
        "cst": "1",
        "crl": "0",
        "hsh": ""
    }


def test_mobile_money_transaction_data():
    mobile_money_transaction_data = MobileMoneyTransactionData(
        vid="demo",
        sid="123456789",
        hash_value=""
    )
    assert mobile_money_transaction_data.to_map() == {
        "vid": "demo",
        "sid": "123456789",
        "hash": ""
    }


def test_card_trigger_payload():
    card_trigger_payload = CardTriggerPayload(
        vid="demo",
        sid="123456789",
        hash_value=""
    ).attach_hash("demo")
    hash_gen_data = card_trigger_payload.to_json()
    assert json.dumps(card_trigger_payload.to_map()) == hash_gen_data


def test_card_trigger_payload_fails_when_expecting_null_hash():
    card_trigger_payload = CardTriggerPayload(
        vid="demo",
        sid="123456789",
        hash_value=""
    )
    assert card_trigger_payload.to_map() != {
        "vid": "demo",
        "sid": "123456789",
        "hash": ""
    }
