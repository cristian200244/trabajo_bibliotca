
# Lista de libros
libros = []

# Lista de usuarios
usuarios = []

# Cola de préstamos
from collections import deque
cola_prestamos = deque()

# Pila de historial
historial = []

# Agregar libro
def agregar_libro(id, titulo, autor, año):
    libros.append({
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "estado": "disponible"
    })

# Registrar usuario
def registrar_usuario(id, nombre, tipo):
    usuarios.append({
        "id": id,
        "nombre": nombre,
        "tipo": tipo
    })

# Solicitar préstamo
def solicitar_libro(usuario_id, libro_id):
    for libro in libros:
        if libro["id"] == libro_id:
            if libro["estado"] == "disponible":
                libro["estado"] = "prestado"
                historial.append(f"Libro {libro_id} prestado a usuario {usuario_id}")
            else:
                cola_prestamos.append((usuario_id, libro_id))