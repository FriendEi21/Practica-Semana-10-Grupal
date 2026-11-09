#!/usr/bin/env python3
"""Orquestador CLI del Sistema de Gestión de Productos IS093A Semana 10."""

from models import Electronico, Libro
from utils import validar_numero, validar_categoria, ValidationError, NotFoundError


def menu() -> str:
    """Imprime el menú de opciones y retorna la elección del usuario."""
    print("\n=== GESTIÓN DE PRODUCTOS (CLI) ===")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Calcular Precio Final")
    print("4. Salir")
    return input("Opción > ").strip()


def main():
    """Función principal que maneja el ciclo de ejecución del programa."""
    inventario = {}  # Diccionario {id: objeto_producto}
    contador_id = 1

    while True:
        try:
            opcion = menu()

            if opcion == "1":
                cat_input = input("Categoría ('electronico' o 'libro'): ")
                categoria = validar_categoria(cat_input)

                nombre = input("Nombre del producto: ").strip()
                if not nombre:
                    raise ValidationError("El nombre no puede estar vacío.")

                precio = validar_numero(input("Precio base: "), tipo=float, min_val=0)
                stock = validar_numero(input("Stock: "), tipo=int, min_val=0)

                if categoria == "electronico":
                    garantia = validar_numero(input("Garantía (meses): "), tipo=int, min_val=0)
                    producto = Electronico(nombre, precio, stock, garantia)
                else:
                    autor = input("Autor: ").strip()
                    if not autor:
                        raise ValidationError("El autor no puede estar vacío.")
                    producto = Libro(nombre, precio, stock, autor)

                inventario[contador_id] = producto
                print(f"\n[+] Producto '{nombre}' agregado con ID {contador_id}")
                contador_id += 1

            elif opcion == "2":
                if not inventario:
                    print("\n[-] El inventario está vacío.")
                else:
                    print("\n--- LISTA DE PRODUCTOS ---")
                    for p_id, prod in inventario.items():
                        print(f"ID {p_id} | {prod}")

            elif opcion == "3":
                id_input = validar_numero(input("Ingrese ID: "), tipo=int, min_val=1)

                if id_input not in inventario:
                    raise NotFoundError(f"No existe un producto con el ID {id_input}")

                producto = inventario[id_input]
                precio_final = producto.calcular_precio_final()
                print(f"\n[=] {producto.nombre} -> Precio Final: S/ {precio_final:.2f}")

            elif opcion == "4":
                print("Cerrando sistema...")
                break

            else:
                raise ValidationError("Opción inválida. Ingrese un número del 1 al 4.")

        except ValidationError as e:
            print(f"\n[!] Error de validación: {e}")
        except NotFoundError as e:
            print(f"\n[!] No encontrado: {e}")
        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"\n[X] Error inesperado: {e}")


if __name__ == "__main__":
    main()
