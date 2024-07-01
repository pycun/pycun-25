def saludar(): 
    print('Hola soy una función') 

def super_funcion(funcion): 
    funcion() 

funcion = saludar  # Asignamos la función a una variable!

super_funcion(funcion)