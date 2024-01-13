import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import platform
import random

def mostrar_advertencia():
    mensajes = [
        "Advertencia: Este programa esta en una version de prueba en esta version, el cual en un futuro ya no puede estar presente o presentar cambios"
    ]
    mensaje_aleatorio = random.choice(mensajes)
    messagebox.showwarning("Advertencia", mensaje_aleatorio)

def mostrar_info_sistema():
    sistema_info = platform.uname()
    info_procesos = list(psutil.process_iter(['name', 'status', 'cpu_percent', 'memory_percent']))

    ventana_info = tk.Toplevel()
    ventana_info.title("Administrador De Recursos (Beta)")

    etiqueta_sistema = tk.Label(ventana_info, text=f"Sistema: {sistema_info.system} {sistema_info.release}")
    etiqueta_sistema.pack()

    etiqueta_phantom = tk.Label(ventana_info, text="Phantom AK 1.8.1")
    etiqueta_phantom.pack()

    etiqueta_procesos = tk.Label(ventana_info, text="Informacion de Procesos:")
    etiqueta_procesos.pack()

    # Etiqueta para el porcentaje total de CPU
    porcentaje_cpu_total = psutil.cpu_percent()
    etiqueta_cpu_total = tk.Label(ventana_info, text=f"Uso total de CPU: {porcentaje_cpu_total}% / 100%")
    etiqueta_cpu_total.pack()

    # Etiqueta para el porcentaje total de memoria
    porcentaje_memoria_total = psutil.virtual_memory().percent
    etiqueta_memoria_total = tk.Label(ventana_info, text=f"Uso total de Memoria: {porcentaje_memoria_total}% / 100%")
    etiqueta_memoria_total.pack()

    # Crear la tabla
    tabla = ttk.Treeview(ventana_info, columns=('Nombre', 'Estado', '% CPU', '% Memoria'), show='headings')
    tabla.heading('Nombre', text='Nombre')
    tabla.heading('Estado', text='Estado')
    tabla.heading('% CPU', text='% CPU')
    tabla.heading('% Memoria', text='% Memoria')
    
    # Configurar líneas verticales para separar las columnas
    tabla.column('Nombre', anchor=tk.W, width=150)
    tabla.column('Estado', anchor=tk.CENTER, width=80)
    tabla.column('% CPU', anchor=tk.CENTER, width=80)
    tabla.column('% Memoria', anchor=tk.CENTER, width=80)

    # Insertar datos en la tabla
    for i, info_proceso in enumerate(info_procesos[:10]):
        try:
            pid = info_proceso.info['pid']
        except KeyError:
            pid = 'N/A'
            
        tabla.insert('', i, values=(info_proceso.info['name'], info_proceso.info['status'],
                                    f"{info_proceso.info['cpu_percent']:.2f}", f"{info_proceso.info['memory_percent']:.2f}"))

    tabla.pack()

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    
    boton_advertencia = tk.Button(ventana_principal, text="Mostrar Advertencia", command=mostrar_advertencia)
    boton_advertencia.pack()

    boton_mostrar_info = tk.Button(ventana_principal, text="Administrar Recursos", command=mostrar_info_sistema)
    boton_mostrar_info.pack()

    ventana_principal.mainloop()

