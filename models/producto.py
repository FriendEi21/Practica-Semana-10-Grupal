"""Módulo que contiene la jerarquía de clases de los productos."""

from utils.exceptions import ValidationError


class DescuentoMixin:
    """Clase Mixin para demostrar Herencia Múltiple y MRO."""

    def aplicar_descuento_por_stock(self, precio: float, stock: int) -> float:
        """Aplica un descuento del 10% si el stock supera las 50 unidades."""
        if stock > 50:
            return precio * 0.90
        return precio


class Producto:
    """Clase base que representa un producto genérico en el inventario."""

    def __init__(self, nombre: str, precio_base: float, stock: int):
        self.nombre = nombre
        self.precio_base = precio_base
        self.stock = stock

    @property
    def precio_base(self) -> float:
        """Obtiene el precio base del producto."""
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor: float):
        if valor < 0:
            raise ValidationError("El precio base no puede ser negativo.")
        self._precio_base = valor

    @property
    def stock(self) -> int:
        """Obtiene el stock actual del producto."""
        return self._stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValidationError("El stock no puede ser negativo.")
        self._stock = valor

    def calcular_precio_final(self) -> float:
        """Calcula el precio final. Debe ser implementado por las subclases."""
        raise NotImplementedError("Subclases deben implementar este método")

    def __str__(self) -> str:
        # Se dividió en dos líneas para cumplir con el límite de 100 caracteres de Pylint
        return (
            f"[{self.__class__.__name__}] {self.nombre} "
            f"- S/ {self.precio_base:.2f} | Stock: {self.stock}"
        )

    def __del__(self):
        print(f"[*] Limpiando recursos: Destruyendo instancia '{self.nombre}'")


class Electronico(DescuentoMixin, Producto):
    """Clase derivada para productos electrónicos."""

    def __init__(self, nombre: str, precio_base: float, stock: int, garantia_meses: int):
        super().__init__(nombre, precio_base, stock)
        self._garantia_meses = garantia_meses  # Atributo protegido

    def calcular_precio_final(self) -> float:
        """Aplica IGV y descuento por stock usando herencia múltiple (Mixin)."""
        precio_igv = self.precio_base * 1.18
        return self.aplicar_descuento_por_stock(precio_igv, self.stock)


class Libro(Producto):
    """Clase derivada para libros."""

    def __init__(self, nombre: str, precio_base: float, stock: int, autor: str):
        super().__init__(nombre, precio_base, stock)
        self.__autor = autor  # Atributo privado estricto (name-mangling)

    def calcular_precio_final(self) -> float:
        """Aplica un descuento estándar del 10% para libros."""
        return self.precio_base * 0.90

    def __str__(self) -> str:
        """Sobrescribe el método __str__ para incluir el autor privado (Polimorfismo)."""
        base_str = super().__str__()
        return f"{base_str} | Autor: {self.__autor}"
