from ObjetoSeguro import ObjetoSeguro
import logging


def main():
    logging.basicConfig(filename='objetoseguro.log',
                        filemode='a', format='%(asctime)s : %(levelname)s : %(message)s',
                        datefmt='%d/%m/%y %H:%M:%S',
                        level=logging.DEBUG)
    logging.debug("Creando a alice")
    alice = ObjetoSeguro("Alice")
    logging.debug("Creando la llave de  alice")
    alice_key = alice.public_key

    logging.debug('Creando a bob')
    bob = ObjetoSeguro("Bob")
    logging.debug('Creando la llave de bob')
    bob_key = bob.public_key

    logging.debug("Generando el mensaje")
    message = "Hola!!!"

    ObjetoSeguro.storemsg(alice, "va a saludar a" + bob.nombre)
    alice.sayhello(bob.nombre, "hola Bob soy Alice")
    msg_ciffer = alice.cypher(message, bob_key)
    ObjetoSeguro.storemsg(alice, msg_ciffer)
    logging.debug(msg_ciffer)
    logging.debug("Descifrando el mensaje")
    message_decipher = ObjetoSeguro.decipher(bob, msg_ciffer)
    print(message_decipher)
    ObjetoSeguro.storemsg(bob, msg_ciffer)
    logging.debug("Se obtiene el mensaje descifrado")


if __name__ == "__main__":
    main()
