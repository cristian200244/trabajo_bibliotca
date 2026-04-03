#importamos la libreria de Tkinter

import tkinter as tk

def mostrar_principal():
    frame_login.pack_forget()
    frame_principal.pack(fill="both", expand=True)


#ventana de incio de sesion

login = tk.Tk()
login.title("Biblioteca") # titulo
login.geometry("300x200+550+250")
login.minsize(300,200)#limite del tamaño de ventana
login.configure(bg="lightblue")


#============================================================
#                     FRAME DE LOGIN
# ============================================================

#etiquetas de login
frame_login =tk.Frame(login, bg="skyblue", bd=5)
frame_login.pack(fill="both",expand=True)

etiqueta = tk.Label(frame_login, text="Bienvenido al sistema de biblioteca", bg="skyblue")
usuario = tk.Label(frame_login, text="Ingresa Usuario", bg="skyblue")
contrasena = tk.Label(frame_login, text="Ingresa Contraseña", bg="skyblue")

#entrada de usuario
entrada_usuario = tk.Entry(frame_login)
#boton para ingresar
boton_ingresar = tk.Button(frame_login,text="ingresar", command= mostrar_principal)


etiqueta.pack()
usuario.pack()
contrasena.pack()
entrada_usuario.pack()
boton_ingresar.pack()    

#=======================================================
#                pagina principal
#=======================================================

frame_principal = tk.Frame(login, bg="white")
label_principal = tk.Label(frame_principal, text="bienvenido a la pagina principal")
label_principal.pack(pady=20)

boton_salir = tk.Button(frame_principal,text="salir", command=login.destroy)
boton_salir.pack
login.mainloop()



