import sys
from ObjetoSeguro import ObjetoSeguro
#  import logging
from socket import socket


def main():
    s = socket()
    s.connect(("localhost", 6030))
    alice = ObjetoSeguro("Alice")
    bob = ObjetoSeguro("Bob")
    bob_key = bob.public_key

    while True:
        output_data = input("Mensaje > ")
        msg_hello = alice.sayhello(bob.objetc_name, alice.cypher(output_data, bob_key))
        ObjetoSeguro.storemsg(alice, "say hello to" + bob.objetc_name)
        if output_data == "adios":
            s.close()
            sys.exit()
        s.send(msg_hello.encode("utf-8"))
        ObjetoSeguro.storemsg(alice, msg_hello)

        # Recibir respuesta.
        input_data = s.recv(1024)
        if input_data:
            ObjetoSeguro.storemsg(bob, "mensaje de respuesta")
            message_answer = bob.answer(ObjetoSeguro.decipher(bob, input_data))
            print(message_answer)


if __name__ == "__main__":
    main()
