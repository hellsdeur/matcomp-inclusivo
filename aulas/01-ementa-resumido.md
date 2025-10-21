## Motivação

Nesta primeira seção, discutimos por que o cálculo numérico é fundamental para compreender técnicas modernas de inteligência artificial.

- O cérebro humano interpreta imagens e sons de forma probabilística, por exemplo: uma imagem pode ter 40% de chance de ser um cachorro, 15% de ser um gato e 45% de ser um saco de lixo.

- Redes neurais imitam esse comportamento, ajustando funções de probabilidade para estimar saídas a partir de entradas.

- Um conceito essencial do cálculo é o da área sob uma curva. Isso pode ser aproximado por retângulos cada vez menores e mais numerosos, o que leva à ideia de integral.

- Em otimização, usada em IA e engenharia, o objetivo é encontrar mínimos ou máximos de funções complexas. O método do gradiente descendente realiza pequenos passos na direção de maior inclinação da função, lidando com números com muitas casas decimais.

- Redes neurais precisam dessa otimização: busca-se a melhor combinação de pesos que minimize o erro entre valor previsto e valor esperado. Porém, em problemas de alta dimensionalidade, o gradiente descendente pode ser ineficiente.

- Word embeddings também dependem de operações numéricas. São usados no Processamento de Linguagem Natural para representar palavras como vetores entre 0 e 1, capturando significado semântico.

- Por exemplo, os vetores de "homem" e "mulher" são semelhantes, diferenciando-se apenas pela operação de flexão de gênero. Isso também ocorre com pares como "rei" e "rainha".

---

## A origem de tudo: álgebra linear

Esta seção introduz conceitos básicos de vetores e matrizes, essenciais para entender transformações em modelos de IA.

- Vetores são representados como setas que partem da origem (0,0) e apontam para um ponto no plano, como (1,2).

- Operações com vetores incluem:

  - **Soma**: somar componente a componente.
  - **Multiplicação por escalar**: estica ou encolhe o vetor.

- Transformações lineares usam matrizes para transformar vetores:

  - Exemplo: aplicar uma matriz 2x2 a um vetor (5,7) gera um novo vetor, calculado com multiplicações e somas das linhas da matriz com os valores do vetor original.

  - Essa ideia é usada em word embeddings: a matriz representa uma transformação semântica (como flexão de gênero ou tempo verbal).

- O produto escalar mede o alinhamento entre dois vetores:

  - Resultado positivo → vetores apontam na mesma direção.
  - Resultado zero → vetores perpendiculares.
  - Resultado negativo → vetores opostos.

---

## IA e matemática: alguns exemplos

Esta seção mostra como os conceitos matemáticos discutidos se aplicam em diversas áreas da IA.

### Redes neurais

- Modelos de IA aprendem a mapear entradas em saídas significativas.

- Exemplo: classificar imagens ou gerar textos palavra por palavra.

- Cada neurônio realiza:

  - Uma transformação linear (produto escalar dos dados com os pesos).
  - Soma com um bias.
  - Aplicação de uma função de ativação não linear.

- O treinamento ajusta pesos e bias usando gradiente descendente.

- Regressão linear é um exemplo simples desse princípio, ajustando uma reta para minimizar o erro dos dados.

### Aprendizado por reforço

- Um agente interage com o ambiente e aprende com recompensas e punições.

- Exemplo: em um jogo de labirinto, o agente aprende quais movimentos levam à saída.

- Usado em robótica, jogos, sistemas de recomendação, veículos autônomos etc.

- Conceitos envolvidos: otimização, probabilidade, expectativa matemática.

- Outros usos incluem:

  - Jogos como xadrez e shogi.
  - Controle de plasma em tokamaks.
  - Ajuste de turbinas e circuitos.

### Otimização

- O algoritmo PSO (Particle Swarm Optimization) representa soluções como partículas que se movem em um espaço de busca.

- Cada partícula leva em conta:

  1. Sua melhor posição individual.
  2. A melhor posição do grupo.
  3. Sua velocidade anterior (inércia).

- Esses três vetores orientam sua próxima posição.

- É um exemplo claro do uso de vetores, álgebra linear e otimização.

### Transformers

- Base dos modelos como GPT.

- Utilizam mecanismos de atenção para processar relações entre palavras em uma sequência.

- Capturam o contexto e a semântica, por exemplo, diferentes sentidos da palavra "modelo".

- Fundamentados em:

  - Produtos escalares entre vetores de embeddings.
  - Normalização com softmax.
  - Operações de álgebra linear e cálculo.

### Ciência de dados

- A análise de dados segue processos sistemáticos como:

  - **KDD**: seleção, pré-processamento, transformação, mineração, avaliação.
  - **CRISP-DM**: modelo padronizado em diferentes setores.

- A matemática computacional é essencial nas etapas de transformação e avaliação.

---

## Ementa da disciplina

A disciplina abordará os seguintes tópicos principais:

1. **Erros numéricos**: arredondamento, truncamento e sua influência nos resultados computacionais.

2. **Zeros de funções reais**: métodos numéricos para encontrar raízes de equações, como Newton-Raphson.

3. **Sistemas lineares**: resolução de Ax = b com métodos como Gauss e Jacobi.

4. **Otimização**: busca de mínimos ou máximos de funções com e sem restrições.

---

## Ferramentas utilizadas na disciplina

Serão usadas as seguintes ferramentas durante o curso:

- **Jupyter Notebook**: ambiente interativo que integra código e texto.

- **Python**: linguagem de programação com forte suporte para análise numérica.

- **Git**: controle de versão para organização e colaboração em projetos.