"""
¿Sabría implementar un decorador para ordenar el resultado de cualquier función
tomando un parámetro opcional que indique si la ordenación es ascendente o descendente?

    Entrada = 8,1,4,2,5
    Salida = 2, 4, 8
"""
def sort (asc = True):
    def decorator (func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, (list, tuple)):
                if asc:
                    sorted_result = sorted(result)
                else:
                    sorted_result = sorted(result, reverse=True)
            return sorted_result
        return wrapper
    return decorator





@sort()
def extract_evens (*values):
    return (v for v in values if v % 2 ==0)


sorted_result = extract_evens(8,1,4,2,5)
print(sorted_result)
