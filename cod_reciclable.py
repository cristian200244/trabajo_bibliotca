#importamos la libreria de Tkinter

import tkinter as tk

# -----------------------------
# Función que muestra la página principal
# -----------------------------
def mostrar_principal():
    frame_login.pack_forget()                 # Oculta el frame de login
    frame_principal.pack(fill="both", expand=True)  # Muestra el frame principal

# -----------------------------
# Ventana principal
# -----------------------------
root = tk.Tk()
root.title("Biblioteca")
root.geometry("300x200+550+250")
root.minsize(300, 200)
root.configure(bg="lightblue")


# ============================================================
#                     FRAME DE LOGIN
# ============================================================
frame_login = tk.Frame(root, bg="skyblue", bd=5)
frame_login.pack(fill="both", expand=True)

# Etiquetas del login
etiqueta = tk.Label(frame_login, text="Bienvenido al sistema de biblioteca", bg="skyblue")
etiqueta_2 = tk.Label(frame_login, text="Ingresa usuario y contraseña", bg="skyblue")

# Entrada de usuario
entrada_usuario = tk.Entry(frame_login)

# Botón para ingresar
boton_ingresar = tk.Button(frame_login, text="Ingresar", command=mostrar_principal)

# Empaquetado de widgets
etiqueta.pack(pady=5)
etiqueta_2.pack(pady=5)
entrada_usuario.pack(pady=5)
boton_ingresar.pack(pady=10)


# ============================================================
#                     FRAME PRINCIPAL
# ============================================================
frame_principal = tk.Frame(root, bg="white")

label_principal = tk.Label(frame_principal, text="Bienvenido a la sección principal", bg="white")
label_principal.pack(pady=20)


boton_salir = tk.Button(frame_principal, text="Salir", command=root.destroy)
boton_salir.pack()



# -----------------------------
# Iniciar la aplicación
# -----------------------------
root.mainloop()


