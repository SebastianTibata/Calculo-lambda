from functools import reduce
from math import pi

a= 8
b= 12

# Factorial
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)
print(f"Factorial de {a} es: {factorial(a)}")

# Numero primo
primo = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print(f"El número {a} {'no es' if not primo(a) else 'es'} primo")

#Algoritmo de euclides
euclides = lambda a, b: a if b == 0 else euclides(b, a % b)
print(f"El MCD de {a},{b} es {euclides(a,b)}")

#Algoritmo de biseccion
biseccion = lambda f, a, b, tol: (
    (lambda m: 
        m if abs(f(m)) < tol 
        else biseccion(f, a, m, tol) if f(a) * f(m) < 0 
        else biseccion(f, m, b, tol)
    )((a + b) / 2)
)
f = lambda x: x**2-5
raiz = biseccion(f, 0, 10, 0.1)

print(f"Raíz encontrada: {raiz}")  # Output esperado: ~2.0


#Polinomio de taylor
x= pi/3
n= 10
cos = lambda x, n: reduce( lambda aux, i: aux + ((-1)**i * x**(2*i) / factorial(2*i)), range(n),0)
print (f"El coseno de {x} es {cos(x,n)}")
