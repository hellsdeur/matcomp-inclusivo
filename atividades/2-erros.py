# %% [markdown]
# Cabeçalho

"""
"""

# ---

# %% [markdown]
# Importações

import unittest

# ---

# %% [markdown]
# Funções a implementar

# %%
def decimal_to_binary(n):
    """
    Converte um número decimal inteiro não negativo em sua representação binária
    como uma string.

    :param n: Número decimal inteiro não negativo.
    :returns: Representação binária do número como uma string.
    """
    
    pass

# %%
def binary_to_decimal(b):
    """
    Converte uma string representando um número binário em seu valor decimal
    inteiro.

    :param b: String representando um número binário.
    :returns: Valor decimal inteiro correspondente.
    """
    
    pass

def round_number(x, n):
    """
    Arredonda um número de ponto flutuante para n casas decimais.

    :param x: Número de ponto flutuante a ser arredondado.
    :param n: Número de casas decimais para arredondar.
    :returns: Número arredondado como um float.
    """

    pass

def truncate_number(x, n):
    """
    Trunca um número de ponto flutuante para n casas decimais.

    :param x: Número de ponto flutuante a ser truncado.
    :param n: Número de casas decimais para truncar.
    :returns: Número truncado como um float.
    """

    pass

# %%
def absolute_error(approx, exact):
    """
    Calcula o erro absoluto entre um valor aproximado e um valor exato.

    :param approx: Valor aproximado.
    :param exact: Valor exato.
    :returns: Erro absoluto como um float.
    """

    pass

# %%
def relative_error(approx, exact):
    """
    Calcula o erro relativo entre um valor aproximado e um valor exato.

    :param approx: Valor aproximado.
    :param exact: Valor exato.
    :returns: Erro relativo como um float.
    """

    pass

# %%
def sum_error(x, y):
    """
    Calcula o erro relativo da soma entre dois valores.

    :param x: Primeiro valor.
    :param y: Segundo valor.
    :returns: Soma dos erros como um float.
    """

    pass

# %%

# ---

# %% [markdown]
# Testes

class TestErrors(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(255), '11111111')

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('1010'), 10)
        self.assertEqual(binary_to_decimal('0'), 0)
        self.assertEqual(binary_to_decimal('11111111'), 255)

    def test_round_number(self):
        self.assertEqual(round_number(3.14159, 2), 3.14)
        self.assertEqual(round_number(2.675, 2), 2.68)

    def test_truncate_number(self):
        self.assertEqual(truncate_number(3.14159, 2), 3.14)
        self.assertEqual(truncate_number(2.6789, 3), 2.678)

    def test_absolute_error(self):
        self.assertAlmostEqual(absolute_error(3.14, 3.14159), 0.00159)

    def test_relative_error(self):
        self.assertAlmostEqual(relative_error(3.14, 3.14159), 0.000506)

    def test_sum_error(self):
        self.assertAlmostEqual(sum_error(1.0, 2.0), 0.0)
