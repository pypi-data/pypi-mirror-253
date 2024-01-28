from src.ipay.domain import IPayDataV2


class C2BV2:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(C2BV2, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @staticmethod
    def get_instance():
        return C2BV2()

    @classmethod
    def initiate_payment(cls, i_pay_data: IPayDataV2):
        """
        This method is used to initiate a payment.
        Args:
            i_pay_data (IPayDataV2): The IPayDataV2 object.
        Returns:
            dict: The response from the request.
        """
        try:
            return {"link": i_pay_data.generate_url()}
        except Exception as e:
            return {"error": str(e)}
