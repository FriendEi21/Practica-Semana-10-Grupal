# Sistema de Gestión de Productos (CLI) - Python POO

Práctica grupal de Desarrollo de Aplicaciones Web (IS093A) demostrando principios de Programación Orientada a Objetos en Python.

## 1. Diagrama de Clases

Estructura y Jerarquía de Clases:

[ Producto ]
  - _nombre: str
  - _precio_base: float
  - _stock: int
  + calcular_precio_final(): float
  + __str__(): str

      ^
      | (Superclase)
      |
+-----------------------------------+-----------------------------------+
|                                                                       |
[ Electronico ]                                                         [ Libro ]
  (Hereda de: DescuentoMixin, Producto)                                   (Hereda de: Producto)
  # _garantia_meses: int                                                  - __autor: str
  + calcular_precio_final(): float                                        + calcular_precio_final(): float

[ DescuentoMixin ]
  + aplicar_descuento_por_stock(precio: float, stock: int): float


## 2. Metodología Method Resolution Order (MRO)
Se implementó **Herencia Múltiple** en la clase `Electronico`, la cual hereda tanto de `DescuentoMixin` como de `Producto`. 
* **Elección de Herencia vs Composición:** Se eligió herencia mediante un *Mixin* porque el descuento es un comportamiento modular transversal ("Es capaz de recibir descuento") que extiende la funcionalidad de la clase sin alterar la jerarquía principal de `Producto`.
* **C3 Linearization:** Al llamar métodos compartidos o utilizar `super()`, Python aplica el algoritmo C3 Linearization. En nuestro código, la resolución de la clase `Electronico` sigue el orden: `Electronico -> DescuentoMixin -> Producto -> object`.

## 3. Evidencias de Ejecución
Todas las capturas de pantalla de la terminal (Ruta feliz, excepciones ValidationError y NotFoundError) se encuentran detalladas visualmente en el informe técnico en formato PDF adjunto a este repositorio.