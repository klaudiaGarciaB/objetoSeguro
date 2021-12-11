from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
from base64 import b85encode, b85decode


class ObjetoSeguro(object):
    def __init__(self, nombre):
        self.__private_key = generate_eth_key()
        self.__private_key_hex = self.__private_key.to_hex()
        self.nombre = nombre

    @property
    def public_key(self) -> str:
        return self.__private_key.public_key.to_hex()

    @staticmethod
    def __base85_decode(message: str) -> bytes:
        message_to_bytes = message.encode("utf-8")
        b85_decode_message = b85decode(message_to_bytes)
        return b85_decode_message

    def sayhello(self, name: str, msg: str):
        return f'{msg}{name}'

    def answer(self, msg: str):
        return f'{msg}'

    @staticmethod
    def cypher(plain_message: str, publickey: str) -> str:
        # this part obtains the binary data
        plain_message_to_bytes = plain_message.encode("utf-8")
        cypher_message = encrypt(publickey, plain_message_to_bytes)
        b85_cypher = b85encode(cypher_message).decode("utf-8")
        return b85_cypher

    def decipher(self, encrypted_message: str) -> str:
        encrypted_msg_decode = self.__base85_decode(encrypted_message)
        decrypted_message = decrypt(
            self.__private_key_hex, encrypted_msg_decode
        )
        decrypted_message_string = decrypted_message.decode("utf-8")
        return self.decrypt_message(decrypted_message_string)

    def storemsg(self, message: str):
        with open(self.nombre+".csv", "a") as fl:
            fl.writelines([self.nombre+" ", message+" \n"])

    @staticmethod
    def decrypt_message(encrypted_message):
        decrypted_message = "mensaje de salida: " + encrypted_message
        return decrypted_message
