def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el area de un triangulo dadas su base y altura.

    Args:
        base: La longitud de la base del triangulo.
        altura: La longitud de la altura del triangulo.

    Returns:
        El area calculada del triangulo como numero decimal.
    """
    return (base * altura) / 2

def es_mayor_de_edad(edad: int) -> bool:
    """
    Verifica si una persona es mayor de edad.

    Args:
        edad: La edad de la persona en anos.

    Returns:
        True si la persona tiene 18 anos o mas, False en caso contrario.
    """
    return edad >= 18

def crear_usuario(nombre: str, correo: str) -> dict:
    """
    Crea un diccionario con los datos del usuario.

    Args:
        nombre: El nombre del usuario.
        correo: El correo electronico del usuario.

    Returns:
        Un diccionario con las claves 'user', 'email' y un estado 'activo' en True.
    """
    return {"user": nombre, "email": correo, "activo": True}

# Invocar help para verificar el docstring
help(crear_usuario)
