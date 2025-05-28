from itertools import product

# Função para calcular divisores de um número (para raízes racionais)
def divisores(n):
    n = abs(n)
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
            divs.add(-i)
            divs.add(-(n // i))
    return list(divs)

# Função para realizar a divisão de polinômio usando o método de Briot-Ruffini
def ruffini(coefs, r):
    n = len(coefs)
    new_coefs = [coefs[0]]
    for i in range(1, n):
        new_coefs.append(new_coefs[-1] * r + coefs[i])
    resto = new_coefs.pop()
    return new_coefs, resto

# Função para encontrar as raízes do polinômio
def encontrar_zeros(coefs):
    raizes = []
    # Enquanto o grau do polinômio for maior que 2, tentamos encontrar raízes
    while len(coefs) > 3:
        a0 = coefs[-1]
        an = coefs[0]
        
        # Gerar as raízes possíveis com base nos divisores
        candidatos = [p / q for p, q in product(divisores(a0), divisores(an))]
        candidatos = list(set(candidatos))  # Remove duplicados
        
        encontrou_raiz = False
        for r in candidatos:
            # Usar o método de Briot-Ruffini para testar a raiz
            _, resto = ruffini(coefs, r)
            if abs(resto) < 1e-6:  # Considera a raiz se o resto for praticamente zero
                raizes.append(r)
                coefs, _ = ruffini(coefs, r)  # Dividir o polinômio pelo binômio (x - r)
                encontrou_raiz = True
                break

        if not encontrou_raiz:
            print("Nenhuma raiz racional encontrada. Tentando outra estratégia.")
            break

    # Resolver quadrática restante, se houver
    if len(coefs) == 3:
        a, b, c = coefs
        delta = b**2 - 4*a*c
        if delta >= 0:
            r1 = (-b + delta**0.5) / (2*a)
            r2 = (-b - delta**0.5) / (2*a)
            raizes.extend([r1, r2])
        else:
            print("Raízes complexas restantes:")  # Melhorando a mensagem
            delta_complexo = complex(delta)**0.5
            r1 = (-b + delta_complexo) / (2*a)
            r2 = (-b - delta_complexo) / (2*a)
            raizes.extend([r1, r2])
            # Exibindo detalhes das raízes complexas
            print(f"Raiz 1: {r1}")
            print(f"Raiz 2: {r2}")
    elif len(coefs) == 2:
        # grau 1: ax + b = 0
        a, b = coefs
        raizes.append(-b / a)

    # Caso não tenha raízes reais
    if not raizes:
        print("O polinômio não tem raízes reais.")
    
    # Arredondando as raízes complexas e reais para 2 casas decimais para exibição
    return [round(r.real, 2) + round(r.imag, 2)*1j if isinstance(r, complex) else round(r, 2) for r in raizes]

if __name__ == "__main__":
    # Entrada de coeficientes
    entrada = input("Digite os coeficientes do polinômio (do maior grau até o termo independente), separados por espaço:\n")
    coefs = entrada.strip().split()
    coefs = [float(c) for c in coefs]
    
    raizes = encontrar_zeros(coefs)
    
    # Exibir as raízes encontradas
    print("Raízes encontradas:")
    for r in raizes:
        print(r)
