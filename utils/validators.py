"""Módulo con utilidades de validación y sanitización de entradas."""

from .exceptions import ValidationError


def validar_numero(
    valor: str,
    tipo: type = float,
    min_val: float = 0,
    max_val: float = None
) -> float:
    """Valida que un string sea un número del tipo especificado y esté en rango."""
    try:
        num = tipo(valor)
        if num < min_val or (max_val is not None and num > max_val):
            raise ValidationError(f"Valor fuera de rango: {min_val} - {max_val}")
        return num
    except ValueError as exc:
        # Pylint pide relanzar explícitamente desde la excepción original (chaining)
        raise ValidationError(f"Formato numérico inválido: {valor}") from exc


def validar_categoria(categoria: str) -> str:
    """Valida que la categoría ingresada sea 'electronico' o 'libro'."""
    cat = categoria.strip().lower()
    if cat not in ["electronico", "libro"]:
        raise ValidationError("Categoría inválida. Debe ser 'electronico' o 'libro'.")
    return cat
