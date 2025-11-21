def function_con_docstring(param1: int, param2: str) -> str:
    """
    Esta función toma un entero y una cadena como parámetros
    y devuelve una cadena que combina ambos.

    :param param1: Un número entero.
    :param param2: Una cadena de texto.
    :return: Una cadena que combina el entero y la cadena.

    EXCEPTIONS:
    Esta función no lanza excepciones.

    EXAMPLES:
    >>> function_con_docstring(5, "hola")
    "El número es 5 y el texto es 'hola'"
    """
    return f"El número es {param1} y el texto es '{param2}'"

def function_sin_docstring(param1, param2):
    return param1 + param2  

print(function_con_docstring.__doc__)
#print(function_sin_docstring.__doc__)


def clean_text(text: str) -> str:
    """Return a normalized version of the input text.

    This function validates that the input is a string, and then returns
    the text stripped of leading and trailing whitespace and converted
    to lowercase. If the input string is empty, an empty string is returned.

    Parameters
    ----------
    text : str
        The text to be cleaned.

    Returns
    -------
    str
        The cleaned and normalized text.

    Raises
    ------
    TypeError
        If the provided value is not a string.

    Examples
    --------
    >>> clean_text("  Hola Mundo  ")
    'hola mundo'
    >>> clean_text("")
    ''
    >>> clean_text("PYTHON")
    'python'
    """
    if not isinstance(text, str):
        raise TypeError("El parámetro 'text' debe ser de tipo str.")

    if not text:
        return ""

    return text.strip().lower()
