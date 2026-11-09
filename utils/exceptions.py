"""Módulo de excepciones personalizadas del sistema."""


class ValidationError(Exception):
    """Excepción lanzada cuando los datos ingresados no cumplen las reglas de negocio."""


class NotFoundError(Exception):
    """Excepción lanzada cuando no se encuentra un producto en el inventario."""
