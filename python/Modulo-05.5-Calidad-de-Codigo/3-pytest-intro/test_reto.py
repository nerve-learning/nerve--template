def es_contrasena_segura(contrasena: str) -> bool:
    """Devuelve True si la contraseña tiene 8 caracteres o más."""
    return len(contrasena) >= 8

def test_contrasena_corta():
    assert es_contrasena_segura("123") == False

def test_contrasena_larga():
    assert es_contrasena_segura("secreto123") == True
