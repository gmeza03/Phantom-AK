import msvcrt
import getpass
import subprocess
import sys
from datetime import datetime
import time

def mostrar_menu_apartados():
    print('''
Apartados:

- B1(BLOC DE NOTAS)

- C2(CALCULADORA)
  
- A3(ACERCA DEL SISTEMA)

- E4(EASTEREGGS)

- R5(REPRODUCTOR)

- A6(ADMINISTRADOR DE RECURSOS(BETA))

- A7(APAGADO)
          

    ''')

print('''
 xxxxxxxxxxxxxxxxxxxxxx
 x--------------------x
 x-----Phantom AK------x
 x--------------------x
 xxxxxxxxxxxxxxxxxxxxxx
''')

print("Bienvenido")

nombre = str(input("Escribe tu nombre:"))
password = getpass.getpass("Ingrese el password:")

while password != "3112003":
    password = getpass.getpass("Ingrese el password correctamente:")

    if password == "3112003":
        break

primera_vez = True

while True:
    if primera_vez:
        print("Bienvenido a PhantomAK 1.8")
        print(nombre)
        print("Creado por Gael Meza")
        print("Hoy es:")
        print(time.strftime("%d/%m/%y"))
        hora_actual = datetime.now().strftime("%H:%M:%S")
        print(f"La hora es: {hora_actual}")
        primera_vez = False
    else:
        mostrar_menu_apartados()

    B1 = ('''
El bloc de notas abrirá en un momento
    ''')

    

    window = str(input("¿Qué apartado deseas abrir (M imprime los apartados) ? : ")) 
   

    if window == "":
        print("Por favor, ingrese un apartado.")
        continue

    if window == "B1":
        print(B1)
        import Bloc

    elif window == "E4":
        EE = getpass.getpass("Ingresa la palabra secreta: ")
        if EE == "ferel":
            print("bueno, encontraste el primer easter egg, el segundo se encuentra en acerca del sistema, la pista es:  F")
        elif EE == "babosa":
            print("Échale ganas we")
        else:
            print("Palabra clave incorrecta")
    
    elif window == "C2":
        print("La Calculadora iniciara en un momento...")
        subprocess.run(["python", "calculadora.py"])
        

    elif window == "A3":
         subprocess.run(["python", "acerca_sistema.py"])

    elif window == "R5":
        import Musica

    elif window == "A7":
        import os
        os.system('shutdown -s')

    elif window == "A6":
        exec(open("admin_tareas.py").read())
