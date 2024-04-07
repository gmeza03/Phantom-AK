import tkinter as tk
import os
import platform


def mostrar_informacion_tecnica():
    def on_key_press(event):
        if event.char.lower() == 'f':
            actualizar_mensaje()

    def actualizar_mensaje():
        mensaje = f"""
        Phantom AK Codename nose
        (Compilacion PA-1.9.0.227)
        
        Este programa se ha roto xd
        
        Escrito el 21 De diciembre del 2023
        
        Creado por Gael Meza
        
        Información Técnica:
        SO: {os.name if os.name != 'posix' else 'Linux'}
        Arquitectura: {arquitectura}
        """
        etiqueta_info.config(text=mensaje_ferel)

    ventana_info = tk.Tk()
    ventana_info.title("Acerca De Phantom AK")

    mensaje_inicial = f"""
        Phantom AK 1.9 
        (Compilacion PA-1.9.0.227)
        
        El programa PhantomAK se distribuye bajo los términos de
        la Licencia Pública General de GNU
        
        Información Técnica:
        SO: {os.name if os.name != 'posix' else 'Linux'}
        Arquitectura: {arquitectura}
    """

    etiqueta_info = tk.Label(ventana_info, text=mensaje_inicial)
    etiqueta_info.pack()

    ventana_info.bind('<KeyPress>', on_key_press)

    ventana_info.mainloop()


if __name__ == "__main__":
    arquitectura = platform.machine()
    mostrar_informacion_tecnica()
