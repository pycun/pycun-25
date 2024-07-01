def requiere_autenticacion(func):
    def wrapper(usuario, *args, **kwargs):
        if not usuario["autenticado"]:
            print("Acceso denegado")
            return None
        return func(usuario, *args, **kwargs)
    return wrapper

@requiere_autenticacion
def mostrar_datos_sensibles(usuario):
    print(f"Datos sensibles para {usuario['nombre']}")

usuario = {"nombre": "Juan", "autenticado": False}
mostrar_datos_sensibles(usuario)

usuario["autenticado"] = True
mostrar_datos_sensibles(usuario)
