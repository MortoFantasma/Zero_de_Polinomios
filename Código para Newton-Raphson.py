import sympy as sp
import numpy as np

def calcular_derivada(coefs):
    x = sp.symbols('x')
    polinomio = sum(coefs[i] * x**(len(coefs)-1-i) for i in range(len(coefs)))
    derivada = sp.diff(polinomio, x)
    return sp.lambdify(x, derivada, 'numpy')

def newton_raphson(coefs, x0, tol=1e-6, max_iter=1000):
    f = lambda x: sum(coefs[i] * x**(len(coefs)-1-i) for i in range(len(coefs)))
    f_prime = calcular_derivada(coefs)
    
    x_n = x0
    for _ in range(max_iter):
        fx_n = f(x_n)
        f_prime_x_n = f_prime(x_n)
        if abs(f_prime_x_n) < tol:
            return None
        x_n1 = x_n - fx_n / f_prime_x_n
        if abs(x_n1 - x_n) < tol:
            return round(x_n1, 6)
        x_n = x_n1
    return None

def encontrar_raizes_newton(coefs):
    raizes_reais = []
    for x0 in np.linspace(-10, 10, 50):
        raiz = newton_raphson(coefs, x0)
        if raiz is not None and all(abs(raiz - r) > 1e-5 for r in raizes_reais):
            raizes_reais.append(raiz)
    return raizes_reais

def calcular_raizes_complexas(coefs):
    x = sp.symbols('x')
    polinomio = sum(coefs[i] * x**(len(coefs)-1-i) for i in range(len(coefs)))
    return sp.solve(polinomio, x)

def is_real_number(expr, tol=1e-6):
    return abs(sp.im(expr.evalf())) < tol

if __name__ == "__main__":
    entrada = input("Digite os coeficientes do polinômio (do maior grau até o termo independente), separados por espaço:\n")
    coefs = [float(c) for c in entrada.strip().split()]

    raizes_reais = encontrar_raizes_newton(coefs)
    raizes_simbolicas = calcular_raizes_complexas(coefs)

    # Imprimir raízes reais
    if raizes_reais:
        print("\nRaízes reais encontradas:")
        for r in raizes_reais:
            print(f"{r:.6f}")
    else:
        print("\nNenhuma raiz real encontrada.")

    # Filtrar as complexas que já apareceram como reais
    raizes_complexas = []
    for raiz in raizes_simbolicas:
        valor = raiz.evalf()
        if not is_real_number(valor) or all(abs(float(valor) - r) > 1e-5 for r in raizes_reais):
            raizes_complexas.append(valor)

    if raizes_complexas:
        print("\nRaízes complexas encontradas:")
        for rc in raizes_complexas:
            print(rc)
