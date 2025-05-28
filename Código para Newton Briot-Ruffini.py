import cmath

def ruffini(coefs, r):
    n = len(coefs)
    new_coefs = [coefs[0]]
    for i in range(1, n):
        new_coefs.append(new_coefs[-1] * r + coefs[i])
    resto = new_coefs.pop()
    return new_coefs, resto

def encontrar_zeros(coefs):
    coefs = [float(c) for c in coefs]
    raizes_reais = []
    raizes_complexas = []

    while len(coefs) > 3:
        encontrou_raiz = False
        for r in range(-100, 101):
            r = float(r)
            _, resto = ruffini(coefs, r)
            if abs(resto) < 1e-6:
                raizes_reais.append(round(r, 6))
                coefs, _ = ruffini(coefs, r)
                encontrou_raiz = True
                break
        if not encontrou_raiz:
            break

    if len(coefs) == 3:
        a, b, c = coefs
        delta = b**2 - 4*a*c
        sqrt_delta = cmath.sqrt(delta)
        r1 = (-b + sqrt_delta) / (2*a)
        r2 = (-b - sqrt_delta) / (2*a)
        for r in (r1, r2):
            if abs(r.imag) < 1e-8:
                raizes_reais.append(round(r.real, 6))
            else:
                raizes_complexas.append(r)
    elif len(coefs) == 2:
        a, b = coefs
        r = -b / a
        raizes_reais.append(round(r, 6))

    return raizes_reais, raizes_complexas

if __name__ == "__main__":
    entrada = input("Digite os coeficientes do polinômio (do maior grau até o termo independente), separados por espaço:\n")
    coefs = entrada.strip().split()
    reais, complexas = encontrar_zeros(coefs)

    if reais:
        print("\nRaízes reais encontradas:")
        for r in reais:
            print(f"{r:.6f}")
    else:
        print("\nNenhuma raiz real encontrada.")

    if complexas:
        print("\nRaízes complexas encontradas:")
        for c in complexas:
            parte_real = f"{c.real:.6f}"
            parte_imag = f"{abs(c.imag):.6f}"
            sinal = "+" if c.imag >= 0 else "-"
            print(f"{parte_real} {sinal} {parte_imag}i")
