📌 Cálculo de Zeros de Polinômios – Método de Newton Briot-Ruffini
📚 Bibliotecas
Este código utiliza a biblioteca cmath, que oferece suporte a números complexos. Ela é necessária para calcular raízes quando o discriminante (Δ) é negativo.

cmath.sqrt(): usada para obter a raiz quadrada de números negativos (resultando em números complexos).

O restante do código utiliza apenas recursos nativos do Python (sem bibliotecas externas como sympy ou numpy).

🧠 Método de Briot-Ruffini
Este método é uma forma eficiente de dividir um polinômio por uma raiz conhecida. Ele também auxilia na identificação de raízes reais inteiras do polinômio por tentativa e erro (método direto).

⚙️ Funções do Código
ruffini(coefs, r): divide o polinômio pelos fatores (x - r) usando o esquema de Briot-Ruffini.

encontrar_zeros(coefs): tenta encontrar raízes reais inteiras por substituição sucessiva. Quando restam apenas três ou dois coeficientes, aplica a fórmula de Bhaskara ou resolução direta.

💬 Entrada de Dados
O usuário deve digitar os coeficientes do polinômio do maior grau até o termo independente, separados por espaço.

Exemplo:
1 -3 -4 → representa o polinômio 
𝑥
2
−
3
𝑥
−
4
x 
2
 −3x−4

📤 Saída de Resultados
As raízes reais encontradas são exibidas com 6 casas decimais.

As raízes complexas (quando o discriminante é negativo) são apresentadas no formato:

css
Copiar
Editar
parte_real ± parte_imaginaria*i
📌 Cálculo de Zeros de Polinômios – Método de Newton-Raphson
📚 Bibliotecas
O código usa duas bibliotecas:

sympy: para manipulação simbólica de expressões matemáticas. Utilizada para:

Construir o polinômio a partir dos coeficientes.

Calcular a derivada automaticamente.

Resolver o polinômio simbolicamente (inclusive com raízes complexas).

Exibir as raízes em formato algébrico.

numpy: para facilitar operações numéricas, como:

Criar um conjunto de valores iniciais para aplicar o método.

Trabalhar com arrays e cálculos numéricos vetorizados.

🧠 Método de Newton-Raphson
Esse método aproxima as raízes reais de uma função 
𝑓
(
𝑥
)
f(x) utilizando a fórmula iterativa:

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
 
A partir de um valor inicial 
𝑥
0
x 
0
​
 , a fórmula é aplicada repetidamente até atingir a convergência ou um limite de iterações.

⚙️ Funções do Código
Geração do polinômio a partir dos coeficientes digitados.

Cálculo da derivada simbólica com sympy.

Iterações do método de Newton-Raphson para múltiplos pontos iniciais.

Filtragem de raízes únicas, evitando repetições ou aproximações redundantes.

Se não forem encontradas raízes reais, o código recorre à solução simbólica com sympy.solve().

💬 Entrada de Dados
O usuário insere os coeficientes do polinômio, separados por espaço.

Exemplo:
1 0 -5 → representa 
𝑥
2
−
5
x 
2
 −5

📤 Saída de Resultados
Raízes reais encontradas numericamente são exibidas com 6 casas decimais.

Quando não houver raízes reais, o código calcula e exibe as raízes complexas com sympy, no formato:

css
Copiar
Editar
parte_real ± parte_imaginaria*i
