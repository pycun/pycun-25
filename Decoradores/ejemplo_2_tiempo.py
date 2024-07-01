import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tomó {fin - inicio} segundos")
        return resultado
    return wrapper

@medir_tiempo
def contar_hasta(n):
    for i in range(n):
        pass

contar_hasta(1000000)
