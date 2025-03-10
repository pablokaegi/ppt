# # Importar clases desde los módulos
from poo.registro_libros import ClaseLibro
from poo.registro_usuarios import ClaseUsuario

# Ahora puedes usar las clases importadas
libro = ClaseLibro("Cien Años de Soledad", "Gabriel García Márquez", "Sudamericana", 1967)
libro2 = ClaseLibro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Sudamericana", 1985)
usuario = ClaseUsuario("Juan", "Pérez", 30)

# Imprimir detalles de los libros y el usuario
print(f"Libro: {libro.titulo}")
print(f"Autor: {libro.autor}")
print(f"Editorial: {libro.editorial}")
print(f"Año: {libro.año}")

print(f"Libro: {libro2.titulo}")
print(f"Autor: {libro2.autor}")
print(f"Editorial: {libro2.editorial}")
print(f"Año: {libro2.año}")

print(f"Nombre: {usuario.nombre}")
print(f"Apellido: {usuario.apellido}")
print(f"Edad: {usuario.edad}")