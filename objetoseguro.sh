#!/bin/bash
clear
echo "*******************************************"
echo "*******************************************"
echo "Ejecutar la primera parte del proyecto"
echo "Claudia García Blanquel"
echo "Nombre del programas ObjetoSeguro.py, comunica.py"
echo "bibliotecas necesarias ecies, base64"
echo "*******************************************"
echo -e "*******************************************\n"
sleep 1
echo "*******************************************"
echo "*******************************************"
echo "Ejecuta el programa comunica.py"
echo "*******************************************"
echo -e "*******************************************\n"
python3 comunica.py
sleep .5
echo "*******************************************"
echo "*******************************************"
echo "Muestra el log del programa"
echo "*******************************************"
echo -e "*******************************************\n"
cat objetoseguro.log
sleep .5
echo "*******************************************"
echo "*******************************************"
echo "Muestra el contenido del archivo de Alice"
echo "*******************************************"
echo -e "*******************************************\n"
cat Alice.csv
sleep .5
echo "*******************************************"
echo "*******************************************"
echo "Muestra el contenido del archivo de Bob"
echo "*******************************************"
echo -e "*******************************************\n"
cat Bob.csv

