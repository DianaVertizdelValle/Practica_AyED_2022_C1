# -*- coding: utf-8 -*-
"""
Algoritmo recursivo de fibonacci con técnica de optimización:
memoización, usando decoradores, explicado por Bruno Breggia
"""
# caso recursivo
# f(n) = f(n-1) + f(n-2)

def decorador(func_recursiva):
    memo = {}    
    def func_rapida(n):
        if n not in memo:
            memo[n] = func_recursiva(n)
        return memo[n]
    
    return func_rapida

@decorador
def fibonacci_rec(posicion):    
    if posicion <=1:
        return posicion
    return fibonacci_rec(posicion-1)+ fibonacci_rec(posicion-2)

# fibonacci_rec = decorador(fibonacci_rec)

if __name__ == '__main__':
    fib = ''
    for i in range(0,10):
        fib += str(fibonacci_rec(i)) + ' '
    print(fib)