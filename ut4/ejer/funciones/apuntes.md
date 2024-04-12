# Apuntes de funciones

## 𓂀 𓋹 SUERTE 𓋹 𓂀 

### Generadores

- ¿Cómo funciona?

Una función generadora en Python se crea utilizando la palabra clave ```yield``` en lugar de return dentro de la definición de la función. Cuando una función generadora se llama, no ejecuta su código inmediatamente. En su lugar, devuelve un objeto generador, que es iterable y puede generar valores sobre la marcha utilizando la instrucción ```yield```.

Veamos un ejemplo simple de una función generadora que genera números pares:

```python
def get_evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Usar la función generadora (llamarla)
generator = get_evens(10)
for number in generator:
    print(number)
```
> NOTA: Recuerda el concepto "congelar la función" para que recordar su estado. La próxima vez que se llame a la función, continuará ejecutándose desde donde se suspendió.


### Función interna

- ¿Cómo funciona?

Una función interna en Python es una función definida dentro de otra función.

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    
    return inner_function

# Llamada a la función externa para obtener la función interna
add_five = outer_function(5)

# Llamada a la función interna con un parámetro
result = add_five(10)
print(result)  # Output: 15
```

Las funciones internas pueden ser útiles para definir funciones auxiliares que se utilizan solo dentro de la función externa.
Esto puede ayudar a evitar la repetición de código al encapsular la lógica común dentro de la función interna.

### Clausura

- ¿Cómo funciona?

Una clausura es una función que recuerda el entorno en el que fue creada. Esto significa que puede acceder y manipular variables locales de la función externa en la que fue definida, incluso después de que esa función haya terminado de ejecutarse. 

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Creamos una clausura con x = 10
closure = outer_function(10)

# Ahora podemos usar la clausura para agregar 5 a x (que es 10)
result = closure(5)
print(result)  # Output: 15

```



 >_DIFERENCIAS_: Una función interna se define dentro de otra función y puede acceder a las variables locales de la función externa mientras se está ejecutando, pero no retiene una copia del entorno una vez que la función externa ha finalizado su ejecución. Por otro lado, una clausura es una función que retiene una copia del entorno en el que fue creada, lo que le permite acceder y modificar las variables locales de la función externa incluso después de que esta haya terminado de ejecutarse.



### Decoradores

- ¿Cómo funciona?

Los decoradores son funciones en Python que modifican o extienden el comportamiento de otras funciones o métodos. Permiten añadir funcionalidades adicionales a una función sin modificar su código interno.

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

@decorator
def greet(name):
    print("Hello,", name)

greet("John")
```
En este ejemplo, el decorador decorador toma una función como argumento y devuelve otra función `(wrapper)` que envuelve a la función original. Dentro de wrapper, se puede ejecutar código antes y después de llamar a la función original. Cuando llamamos a `saludar` `("Juan")`, en realidad estamos llamando a wrapper, que a su vez llama a `saludar` . Esto nos permite ejecutar código adicional antes y después de la llamada a `saludar` .

### Funciones Recursivas

- ¿Cómo funcionan?

Una función recursiva es una función que se llama a sí misma dentro de su definición. Esto permite que la función resuelva problemas dividiéndolos en subproblemas más pequeños y similares.

```python
def pow(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return base * pow(base, exponent - 1)


pow(2, 4)
16

pow(3, 5)
243
```

**TENER EN CUENTA:**
**Condición de parada**:
En todo código recursivo es necesario establecer una condición de parada. En el ejemplo la condición de parada se da cuando el exponente es 0, siendo el resultado 1, ya que todo número elevado a 0 es igual a 1.

**Llamada recursiva**:
Obviamente en todo código recursivo debe haber una llamada recursiva. En el ejemplo anterior la recursividad se apoya en la idea de que 24=2∗23
. Por tanto podemos hacer uso de la misma función recursiva para calcular el resto de valores.





