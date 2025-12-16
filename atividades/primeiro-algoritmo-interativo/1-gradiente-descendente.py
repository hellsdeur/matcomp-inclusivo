# %% [markdown]
# Cabeçalho

"""
Este módulo demonstra o algoritmo do gradiente descendente para ajustar uma reta aos dados.
O objetivo é compreender como os parâmetros de uma linha (intercept e slope) são atualizados
interativamente para minimizar o erro entre as previsões e os valores observados.

Conceitos a serem explorados:
- Custo: usamos o erro quadrático médio (MSE) para medir o quão
distante a reta está dos pontos observados.  Quanto menor o custo, melhor o
ajuste.
- Gradiente: indica a direção de maior aumento do custo em relação a cada
parâmetro.  Para minimizar o custo, movemos os parâmetros na direção oposta
ao gradiente.
- Gradiente descendente: algoritmo que atualiza os parâmetros em pequenos
passos repetidos, reduzindo o custo até encontrar uma solução razoável.
"""

# ---

# %% [markdown]
# Importações

import unittest

# ---

# %% [markdown]
# Dados de exemplo

# ---

# %% [markdown]
# Funções fornecidas

def compute_cost(intercept, slope, x, y):
    """Calcula o erro quadrático médio (MSE) entre a linha definida por
    intercept e slope e os pontos (x, y).

    O MSE é definido como a média do quadrado das diferenças entre as
    previsões ``intercept + slope * xi`` e os valores reais ``yi``.

    :param intercept: interceção da reta.
    :param slope: inclinação da reta.
    :param x: valores de entrada.
    :param y: valores alvo correspondentes.
    :returns: valor do erro quadrático médio.
    """
    if len(x) != len(y):
        raise ValueError("As listas x e y devem ter o mesmo comprimento.")
    
    m = len(x)

    if m == 0:
        raise ValueError("As listas de dados não podem estar vazias.")
    
    total_error = 0.0

    for xi, yi in zip(x, y):
        prediction = intercept + slope * xi
        diff = prediction - yi
        total_error += diff * diff

    return total_error / m

# ---

# %% [markdown]
# Funções a implementar

def numerical_gradient(intercept, slope, x, y, h):
    """
    Docstring for numerical_gradient
    
    :param intercept: Description
    :param slope: Description
    :param x: Description
    :param y: Description
    :param h: Description
    """
    pass

def gradient_descent(initial_intercept, initial_slope, x, y, learning_rate, n_iterations):
    """
    Executa o algoritmo do gradiente descendente para encontrar os valores
    de intercept e slope que minimizam o MSE.

    A função começa com valores iniciais fornecidos para os parâmetros e executa
    uma quantidade ``n_iterations`` de passos. Em cada passo, calcula o gradiente numérico e
    atualiza os parâmetros na direção contrária e registra o custo atual.
    
    :param initial_intercept: valor inicial para o intercept.
    :param initial_slope: valor inicial para a inclinação.
    :param x: sequência de valores de entrada.
    :param y: sequência de valores alvo.
    :param learning_rate: tamanho do passo em cada atualização.
    :param n_iterations: número de iterações do algoritmo.
    :returns: uma tupla `(final_intercept, final_slope, historico_custo)`.
    """

    pass

# ---

# %% [markdown]
# Exemplo simples

def exemplo_simples() -> None:
    """Executa um exemplo simples de gradiente descendente.

    Esta função é chamada quando o módulo é executado diretamente.  Ela
    define dados simples de regressão linear, executa o gradiente descendente
    com uma taxa de aprendizagem e número de iterações padrão e imprime os
    resultados.  Altere ``learning_rate`` e ``n_iterations`` para observar
    diferentes comportamentos.
    """
    x_data = [0, 1, 2, 3, 4]
    y_data = [1.1, 2.9, 5.2, 7.0, 9.1]

    initial_intercept = 0.0
    initial_slope = 0.0
    learning_rate = 0.1
    n_iterations = 100

    final_intercept, final_slope, cost = gradient_descent(
        initial_intercept, initial_slope, x_data, y_data, learning_rate, n_iterations
    )

    print("Resultados do gradiente descendente:")
    print(f"Intercept final: {final_intercept:.4f}")
    print(f"Slope final: {final_slope:.4f}")
    print(f"Custo final: {cost[-1]:.4f}")

# ---

# %% [markdown]
# Testes

class TestGC(unittest.TestCase):

    def test_compute_cost_zero(self):

        x = [0, 1, 2, 3]
        y = [1, 3, 5, 7]

        _, _, cost_history = gradient_descent(0.0, 0.0, x, y, learning_rate=0.1, n_iterations=20)

        self.assertTrue(cost_history[1] < cost_history[0])
        self.assertTrue(cost_history[2] < cost_history[1])

if __name__ == "__main__":
    exemplo_simples()
