import hashlib
import hmac
import json


class IPayDataV1:
    def __init__(self, live=0, oid="", inv="", amount=0, tel="", eml="", vid="", curr="", p1=None, p2=None, p3=None,
                 p4=None, cst=1, cbk="", crl=0, hash_value="", auto_pay=1):
        self.live = live
        self.oid = oid
        self.inv = inv
        self.amount = amount
        self.tel = tel
        self.eml = eml
        self.vid = vid
        self.curr = curr
        self.p1 = p1 or oid
        self.p2 = p2 or oid
        self.p3 = p3 or oid
        self.p4 = p4 or oid
        self.cst = cst
        self.cbk = cbk
        self.crl = crl
        self.hash = hash_value
        self.auto_pay = auto_pay

    def to_map(self):
        return {
            "live": self.live,
            "oid": self.oid,
            "inv": self.inv,
            "amount": self.amount,
            "tel": self.tel,
            "eml": self.eml,
            "vid": self.vid,
            "curr": self.curr,
            "p1": self.p1,
            "p2": self.p2,
            "p3": self.p3,
            "p4": self.p4,
            "cst": self.cst,
            "cbk": self.cbk,
            "crl": self.crl,
            "hash": self.hash,
            "autopay": self.auto_pay
        }

    def attach_hash(self, i_pay_secret):
        fields_to_hash = [str(value) for key, value in self.to_map().items() if key not in ["crl", "hash", "autopay"]]
        data_to_hash = ''.join(fields_to_hash).encode('utf-8')
        hmac_key = hashlib.sha256(i_pay_secret.encode('utf-8')).hexdigest()
        hmac_value = hmac.new(hmac_key.encode('utf-8'), data_to_hash, hashlib.sha256).hexdigest()
        self.hash = hmac_value
        return self

    def to_json(self):
        return json.dumps(self.to_map())


class MobileMoneyTransactionData:
    def __init__(self, vid="", sid="", hash_value=""):
        self.vid = vid
        self.sid = sid
        self.hash = hash_value

    def to_map(self):
        return {
            "sid": self.sid,
            "vid": self.vid,
            "hash": self.hash
        }

    def attach_hash(self, i_pay_secret):
        fields_to_hash = [str(value) for key, value in self.to_map().items() if key != "hash"]
        data_to_hash = ''.join(fields_to_hash).encode('utf-8')
        hmac_key = hashlib.sha256(i_pay_secret.encode('utf-8')).hexdigest()
        hmac_value = hmac.new(hmac_key.encode('utf-8'), data_to_hash, hashlib.sha256).hexdigest()
        self.hash = hmac_value
        return self

    def to_json(self):
        return json.dumps(self.to_map())


class TransactionQueryData:
    def __init__(self, oid="", vid="", hash_value=""):
        self.oid = oid
        self.vid = vid
        self.hash = hash_value

    def to_map(self):
        return {
            "oid": self.oid,
            "vid": self.vid,
            "hash": self.hash
        }

    def attach_hash(self, i_pay_secret):
        fields_to_hash = [str(value) for key, value in self.to_map().items() if key != "hash"]
        data_to_hash = ''.join(fields_to_hash).encode('utf-8')
        hmac_key = hashlib.sha256(i_pay_secret.encode('utf-8')).hexdigest()
        hmac_value = hmac.new(hmac_key.encode('utf-8'), data_to_hash, hashlib.sha256).hexdigest()
        self.hash = hmac_value
        return self

    def to_json(self):
        return json.dumps(self.to_map())


class MobileMoneyTriggerPayload:
    def __init__(self, phone="", sid="", vid="", hash_value=""):
        self.phone = phone
        self.sid = sid
        self.vid = vid
        self.hash = hash_value

    def to_map(self):
        return {
            "phone": self.phone,
            "vid": self.vid,
            "sid": self.sid,
            "hash": self.hash
        }

    def attach_hash(self, i_pay_secret):
        fields_to_hash = [str(value) for key, value in self.to_map().items() if key != "hash"]
        data_to_hash = ''.join(fields_to_hash).encode('utf-8')
        hmac_key = hashlib.sha256(i_pay_secret.encode('utf-8')).hexdigest()
        hmac_value = hmac.new(hmac_key.encode('utf-8'), data_to_hash, hashlib.sha256).hexdigest()
        self.hash = hmac_value
        return self

    def to_json(self):
        return json.dumps(self.to_map())


class CardTriggerPayload:
    def __init__(self, sid="", vid="", email="", card_id="", phone="", hash_value=""):
        self.sid = sid
        self.vid = vid
        self.email = email
        self.card_id = card_id
        self.phone = phone
        self.hash = hash_value

    def to_map(self):
        return {
            "sid": self.sid,
            "vid": self.vid,
            "cardid": self.card_id,
            "phone": self.phone,
            "email": self.email,
            "hash": self.hash
        }

    def attach_hash(self, i_pay_secret):
        fields_to_hash = [str(value) for key, value in self.to_map().items() if key != "hash"]
        data_to_hash = ''.join(fields_to_hash).encode('utf-8')
        hmac_key = hashlib.sha256(i_pay_secret.encode('utf-8')).hexdigest()
        hmac_value = hmac.new(hmac_key.encode('utf-8'), data_to_hash, hashlib.sha256).hexdigest()
        self.hash = hmac_value
        return self

    def to_json(self):
        return json.dumps(self.to_map())


class RefundPayload:
    def __init__(self, code="", vid="", hash_value="", amount=0):
        self.code = code
        self.vid = vid
        self.hash = hash_value
        self.amount = amount

    def to_map(self):
        return {
            "code": self.code,
            "vid": self.vid,
            "hash": self.hash,
            "amount": self.amount
        }

    def attach_hash(self, i_pay_secret):
        fields_to_hash = [str(value) for key, value in self.to_map().items() if key != "hash"]
        data_to_hash = ''.join(fields_to_hash).encode('utf-8')
        hmac_key = hashlib.sha256(i_pay_secret.encode('utf-8')).hexdigest()
        hmac_value = hmac.new(hmac_key.encode('utf-8'), data_to_hash, hashlib.sha256).hexdigest()
        self.hash = hmac_value
        return self

    def to_json(self):
        return json.dumps(self.to_map())
