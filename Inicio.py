import getpass
import subprocess
import platform
from datetime import datetime
import time

def mostrar_menu_apartados():
    print('''
Apartados:

- B1(BLOC DE NOTAS)
- C2(CALCULADORA)
- A3(ACERCA DEL SISTEMA)
- R4(REPRODUCTOR)
- A5(ADMINISTRADOR DE RECURSOS(BETA))
- A6(APAGADO)
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
        print("Bienvenido a PhantomAK Codename B-Star")
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

    #elif window == "E4":
        #print ("No se supone que esto deberia estar pasando")

    elif window == "C2":
        print("La Calculadora iniciará en un momento...")
        subprocess.run(["python", "calculadora.py"])

    elif window == "A3":
        subprocess.run(["python", "acerca_sistema.py"])

    elif window == "R4":
        import Musica

    elif window == "A6":
        system_platform = platform.system()
        if system_platform == "Windows":
            # Comando para apagar en Windows
            subprocess.run(["shutdown", "/s", "/t", "0"])
        elif system_platform == "Linux" or system_platform == "Darwin":
            # Comando para apagar en Linux o Mac
            subprocess.run(["shutdown", "-h", "now"])
        else:
            print("Apagado no compatible con el sistema: {system_platform}")

    elif window == "A5":
        exec(open("admin_tareas.py").read())
