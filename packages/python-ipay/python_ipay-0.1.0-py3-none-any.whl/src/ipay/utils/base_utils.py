from string import ascii_letters, digits
import random


class BaseUtils:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BaseUtils, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        """
        This method returns the singleton instance of the BaseUtils class.
        Returns:
            BaseUtils: Returns the base utils singleton class.
        """
        return BaseUtils()

    @staticmethod
    def generate_random_alphanumeric_string(prefix: str = "", delimiter: str = "", length: int = 10):
        """
        This method is used to generate a random alphanumeric string with parsed prefix,delimiter and length.
        Args:
            prefix (str): The prefix to be attached to the random string, otherwise an empty string.
            delimiter (str):The character used to separate the prefix and random chars, otherwise empty string.
            length (int):The length ot the random string to be generated, otherwise length is 10.
        Returns:
            str: The random string concatenated with the prefix, delimiter and random string.
        """
        characters = ascii_letters + digits
        return f'{prefix}{delimiter}'.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def generate_random_alphabetic_string(prefix: str = "", delimiter: str = "", length: int = 10):
        """
        This method is used to generate a random alphabetic string with parsed prefix,delimiter and length.
        Args:
            prefix (str): The prefix to be attached to the random string, otherwise an empty string.
            delimiter (str):The character used to separate the prefix and random chars, otherwise empty string.
            length (int):The length ot the random string to be generated, otherwise length is 10.
        Returns:
            str: The random string concatenated with the prefix, delimiter and random string.
        """
        characters = ascii_letters
        return f'{prefix}{delimiter}'.join(random.choice(characters) for _ in range(length))



