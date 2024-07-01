def logueo(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} terminó")
        return resultado
    return wrapper

@logueo
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Mundo")