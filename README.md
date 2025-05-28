# Zero de Polinômios

# 📌 Cálculo de Zeros de Polinômios – Método de Newton Briot-Ruffini
📚 Bibliotecas
O código importa a biblioteca cmath, que oferece suporte ao cálculo com números complexos. Ela é essencial para resolver raízes quadráticas com discriminante negativo, fornecendo o resultado corretamente com parte imaginária.

cmath.sqrt() é usada para calcular a raiz quadrada mesmo quando o valor do discriminante (Δ) é negativo.

O restante do código é implementado com funções nativas do Python, sem uso de bibliotecas externas adicionais.

⚙️ Função ruffini
A função ruffini implementa a divisão sintética de polinômios, permitindo dividir um polinômio 
𝑃
(
𝑥
)
P(x) por 
(
𝑥
−
𝑟
)
(x−r), onde 
𝑟
r é uma raiz candidata. Ela retorna os novos coeficientes do quociente e o resto da divisão.

🧮 Função encontrar_zeros
Recebe os coeficientes do polinômio e utiliza tentativas de raízes reais 
𝑟
r entre -100 e 100. Se o resto da divisão for próximo de zero, o valor é considerado uma raiz real. Quando restam apenas dois ou três coeficientes, a equação de 1º ou 2º grau é resolvida diretamente (inclusive para raízes complexas).

📥 Entrada de Dados
O usuário deve fornecer os coeficientes do polinômio, do maior grau até o termo independente, separados por espaços.

📌 Exemplo:
1 -3 -4 (representa 
𝑥
2
−
3
𝑥
−
4
x 
2
 −3x−4)

🖨️ Saída
O código imprime:

Raízes reais encontradas (com 6 casas decimais).

Raízes complexas, formatadas como parte_real ± parte_imaginária i.

# 📌 Cálculo de Zeros de Polinômios – Método de Newton-Raphson
📚 Bibliotecas
Este código utiliza duas bibliotecas principais:

sympy: Permite manipulação simbólica de expressões matemáticas. É usada para:

Montar o polinômio a partir dos coeficientes.

Calcular a derivada simbólica de forma automática.

Resolver o polinômio simbolicamente para encontrar as raízes (inclusive complexas).

Representar resultados em formato algébrico.

numpy: Utilizada para:

Gerar um conjunto de pontos iniciais para aplicar o método de Newton-Raphson (ex: np.linspace(-10, 10, 20)).

Facilitar operações numéricas com arrays.

🧠 Método de Newton-Raphson
Este método aproxima raízes reais de uma função 
𝑓
(
𝑥
)
f(x) usando iterações sucessivas com a fórmula:

𝑥
𝑛
+
1
=
𝑥
𝑛
−
𝑓
(
𝑥
𝑛
)
𝑓
′
(
𝑥
𝑛
)
x 
n+1
​
 =x 
n
​
 − 
f 
′
 (x 
n
​
 )
f(x 
n
​
 )
​
 
⚙️ Função Principal
Calcula a derivada simbólica do polinômio.

Testa diversos pontos iniciais no intervalo [-10, 10] para tentar encontrar diferentes raízes reais.

Armazena e exibe apenas raízes distintas (sem repetições visuais).

💡 Tratamento de Complexas
Mesmo quando o método não encontra raízes reais, o código usa sympy.solve() para calcular e exibir as raízes complexas de forma simbólica, garantindo sempre uma resposta.

📥 Entrada de Dados
O usuário fornece os coeficientes do polinômio como uma única linha com números separados por espaço.

📌 Exemplo:
1 0 -4 (representa 
𝑥
2
−
4
x 
2
 −4)

🖨️ Saída
Raízes reais aproximadas, com 6 casas decimais.

Raízes complexas exibidas simbolicamente, no formato parte_real ± parte_imaginária * i.

Mensagem amigável caso nenhuma raiz real seja encontrada.
