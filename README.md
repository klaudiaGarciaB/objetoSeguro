# objetoSeguro
![ObjetoSeguro](https://user-images.githubusercontent.com/13142349/146285702-1fc49188-2a95-4af3-88e9-622c539bf436.png)

Proyecto para el curso de python INAOE -INTEL
**************************************************************************
Para ejecturar este archivo, se puede apoyar del archivo objetoseguro.bash
NOTA: se requiere de la biblioteca ecies



Proyecto parte 2


    La intención de esta parte del código es que se tenga una caomunicación P2P, donde Alice le mande un mensaje a Bob a traves de un canal inseguro. 
    Para ello se utilizara el ECC.
    
Install de la biblioteca de curvas elipticas en python

pip install eciespy #under Python 3.6+.

Este programa requiere de los siguientes archivos para su ejecución
ObjetoSeg.py contiene la clase del objeto seguro: las llaves, así como el cifrado y descifrado de los mensajes.
main.py Tiene la logica del proyecto para hace uso de los objetos y sus métodos o funciones
tcpServer.py Contiene el objeto de conexión utilizando sockets e hilos

Starting and tests
para la ejecución del programa desde línea de comandos
python3 main.py

