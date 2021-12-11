from ObjetoSeguro import ObjetoSeguro
import logging


def main():
    logging.basicConfig(filename='objetoseguro.log',
                        filemode='a', format='%(asctime)s : %(levelname)s : %(message)s',
                        datefmt='%d/%m/%y %H:%M:%S',
                        level=logging.DEBUG)
    logging.debug("Creating alice's object")
    alice = ObjetoSeguro("Alice")
    logging.debug("Creating bob's object")
    bob = ObjetoSeguro("Bob")
    logging.debug("Creating bob's key")
    bob_key = bob.public_key

    logging.debug("Send say hello in a message")
    ObjetoSeguro.storemsg(alice, "say hello to" + bob.objetc_name)
    msg_hello = alice.sayhello(bob.objetc_name, alice.cypher("Hello Bob, I am Alice", bob_key))
    logging.debug("Store message")
    ObjetoSeguro.storemsg(alice, msg_hello)
    logging.debug("Bob answered the message")
    message_answer = bob.answer(ObjetoSeguro.decipher(bob, msg_hello))
    logging.debug("decrypted message show in terminal")
    print(message_answer)
    logging.debug("Store message")
    ObjetoSeguro.storemsg(bob, "mensaje de respuesta")

    logging.debug("Creating alice's key")
    alice_key = alice.public_key
    logging.debug("Bob say hello to Alice")
    ObjetoSeguro.storemsg(bob, "say hello to" + alice.objetc_name)
    msg_hello = bob.sayhello(alice.objetc_name, alice.cypher("Hi Alice, how's going?", alice_key))
    logging.debug("Store message crypted")
    ObjetoSeguro.storemsg(bob, msg_hello)

    logging.debug("Alice answered the message")
    message_answer = alice.answer(ObjetoSeguro.decipher(alice, msg_hello))
    logging.debug("decrypted message show in terminal")
    print(message_answer)
    ObjetoSeguro.storemsg(alice, "mensaje de respuesta")


if __name__ == "__main__":
    main()
