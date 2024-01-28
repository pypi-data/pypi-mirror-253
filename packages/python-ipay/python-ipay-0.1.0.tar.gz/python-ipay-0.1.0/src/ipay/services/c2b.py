import json

from src.ipay.domain.data import IPayDataV1
from src.ipay.utils import HttpClient
from src.ipay.domain.data import MobileMoneyTransactionData, CardTriggerPayload, TransactionQueryData


class C2B:
    """
    This class is used to make requests to the iPay V2 API.

    """

    def __init__(self):
        """
        This is the constructor method for the IPayService class.
        """
        self.base_url = "https://apis.ipayafrica.com/payments/v2"
        self.http_client = HttpClient(self.base_url)

    def initiate_payment(self, i_pay_data: IPayDataV1, i_pay_secret: str):
        """
        This method is used to initiate a payment.
        Args:
            i_pay_data (IPayDataV1): The IPayDataV1 object.
            i_pay_secret (str): The secret key provided by iPay.
        Returns:
            dict: The response from the request.
        """
        try:
            i_pay_data.attach_hash(i_pay_secret)
            data = i_pay_data.to_json()
            headers = {"Content-Type": "application/json"}
            response = self.http_client.post(url="/transact", data=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def initiate_mobile_money_payment_call(self, mobile_money_transact_data, i_pay_secret: str):
        """
        This method is used to initiate a mobile money payment.
        Args:
            mobile_money_transact_data (MobileMoneyTransactionData): The MobileMoneyTransactionData object.
            i_pay_secret (str): The secret key provided by iPay.
        Returns:
            dict: The response from the request.
        """
        try:
            mobile_money_transact_data.attach_hash(i_pay_secret)
            data = mobile_money_transact_data.to_json()
            headers = {"Content-Type": "application/json"}
            response = self.http_client.post(url="/transact/mobilemoney", data=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def query_transaction_status(self, transaction_query_data: TransactionQueryData, i_pay_secret: str):
        """
        This method is used to query the status of a transaction.
        Args:
            transaction_query_data (TransactionQueryData): The TransactionQueryData object.
            i_pay_secret (str): The secret key provided by iPay.
        Returns:
            dict: The response from the request.
        """
        try:
            transaction_query_data.attach_hash(i_pay_secret)
            data = transaction_query_data.to_json()
            headers = {"Content-Type": "application/json"}
            response = self.http_client.post(url="/transaction/search", data=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def initiate_stk_push_payment(self, mobile_money_trigger_payload: MobileMoneyTransactionData, provider, i_pay_secret: str):
        """
        This method is used to initiate a mobile money payment.
        Args:
            mobile_money_trigger_payload (MobileMoneyTransactionData): The MobileMoneyTransactionData object.
            provider (str): The mobile money provider.
            i_pay_secret (str): The secret key provided by iPay.
        Returns:
            dict: The response from the request.
        """
        try:
            mobile_money_trigger_payload.attach_hash(i_pay_secret)
            data = mobile_money_trigger_payload.to_json()
            if provider is None:
                return {"error": "Provider is required"}
            if provider.upper() not in ["SAFARICOM", "AIRTELTIGO", "EQUITEL"]:
                return {"error": "Provider must be either SAFARICOM, AIRTEL, or EQUITEL"}
            service_provider = ""
            if provider.upper() == "EQUITEL":
                service_provider = "equitel"
            elif provider.upper() == "AIRTELTIGO":
                service_provider = "airtel"
            else:
                service_provider = "mpesa"
            url = f"{self.base_url}/transact/push/{service_provider}"
            headers = {"Content-Type": "application/json"}
            response = self.http_client.post(url=url, data=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def initiate_card_payment(self, card_trigger_payload: CardTriggerPayload, i_pay_secret: str):
        """
        This method is used to initiate a card payment.
        Args:
            card_trigger_payload (CardTriggerPayload): The CardTriggerPayload object.
            i_pay_secret (str): The secret key provided by iPay.
        Returns:
            dict: The response from the request.
        """
        try:
            card_trigger_payload.attach_hash(i_pay_secret)
            data = card_trigger_payload.to_json()
            headers = {"Content-Type": "application/json"}
            response = self.http_client.post(url="/transact/card", data=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}
