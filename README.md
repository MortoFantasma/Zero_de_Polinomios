# Cálculo de Zeros de Polinômios

## 🧠 Métodos Utilizados

### Método de Newton-Raphson

Este método aproxima raízes reais de uma função \( f(x) \) utilizando a fórmula iterativa:

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

Ele começa com um valor inicial \( x_0 \) e aplica a fórmula sucessivamente até encontrar uma raiz ou atingir o número máximo de iterações.

#### 📚 Bibliotecas

- **`sympy`**: Para manipulação simbólica de expressões matemáticas.
- **`numpy`**: Para facilitar operações numéricas com arrays.

#### ⚙️ Funções do Código

1. **Cálculo do polinômio** a partir dos coeficientes fornecidos.
2. **Cálculo da derivada simbólica** do polinômio com `sympy`.
3. **Iterações do Método de Newton-Raphson** aplicadas a múltiplos pontos iniciais.
4. **Filtragem de raízes reais** e exibição com até 6 casas decimais.
5. Caso não haja raízes reais, o código calcula as **raízes complexas**.

#### 💬 Entrada de Dados

O usuário deve inserir os coeficientes do polinômio **do maior grau até o termo independente**, separados por espaço.

**Exemplo:**  
`1 0 -5` → Representa \( x^2 - 5 \)

#### 📤 Saída de Resultados

- Exibe as **raízes reais** encontradas.
- Caso não haja raízes reais, o código exibe as **raízes complexas** no formato: parte_real ± parte_imaginaria*i


---

### Método de Briot-Ruffini

Este método é uma forma eficiente de dividir um polinômio por um fator conhecido (raiz) usando o esquema de Briot-Ruffini.

#### 📚 Bibliotecas

- **`cmath`**: Para manipulação de números complexos e cálculo da raiz quadrada de números negativos.

#### ⚙️ Funções do Código

1. **Divisão do polinômio** pelos fatores \( (x - r) \) usando o método de Briot-Ruffini.
2. **Encontrar raízes reais inteiras** por tentativa e erro.
3. **Resolução direta** com a fórmula de Bhaskara para polinômios quadráticos.
4. Caso não sejam encontradas raízes reais, o código calcula as **raízes complexas**.

#### 💬 Entrada de Dados

O usuário deve inserir os coeficientes do polinômio **do maior grau até o termo independente**, separados por espaço.

**Exemplo:**  
`1 -3 -4` → Representa \( x^2 - 3x - 4 \)

#### 📤 Saída de Resultados

- Exibe as **raízes reais** encontradas.
- Exibe as **raízes complexas** se o discriminante for negativo, no formato: parte_real ± parte_imaginaria*i


---

## 📝 Como Rodar os Códigos

Lembrando que é necessário ter python instalado.

1. Clone o repositório:

Se você tiver logado no GitHub, clone: https://github.com/MortoFantasma/Zero_de_Polinomios.git

Se não, apenas baixe os dois arquivos dos códigos e salve e uma mesma pasta.

2. Navegue até o diretório do repositório (o local onde os dois códigos estão salvos):

cd Zero-de-Polinomios 

3. Execute os códigos em seu terminal:

Para o Método de Newton-Raphson: 
python3 newton_raphson.py

Para o Método de Briot-Ruffini: 
python3 briot_ruffini.py

4. Insira os coeficientes do polinômio quando solicitado.

