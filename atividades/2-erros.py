# %% [markdown]
# Cabeçalho

"""
Este módulo implementa funções para conversão entre representações
numéricas (decimal e binário), arredondamento e truncamento de números
de ponto flutuante, e cálculo de erros absolutos e relativos. O objetivo
é implementar ferramentas básicas para manipulação e análise de números em
diferentes formatos, bem como para avaliar a precisão de aproximações numéricas.
"""

# ---

# %% [markdown]
# Importações

# %%
import unittest

# %% [markdown]
# ---

# %% [markdown]
# Funções a implementar

# %%
def decimal_to_binary(n):
    """
    Converte um número inteiro positivo em sua representação binária como uma string.

    :param n: Número inteiro positivo.
    :returns: Representação binária do número como uma string.
    """
    
    pass

# %%
def binary_to_decimal(b):
    """
    Converte uma string representando um número binário em seu valor inteiro.

    :param b: String representando um número binário.
    :returns: Valor decimal inteiro correspondente.
    """
    
    pass

# %%
def round_number(x, n):
    """
    Arredonda um número de ponto flutuante para n casas decimais.

    :param x: Número de ponto flutuante a ser arredondado.
    :param n: Número de casas decimais para arredondar.
    :returns: Número arredondado como um float.
    """

    pass

# %%
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

# %% [markdown]
# ---

# %% [markdown]
# Testes

# %%
class TestErrors(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(10), '1010')
        self.assertEqual(decimal_to_binary(0), '0')
        self.assertEqual(decimal_to_binary(255), '11111111')
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(2), '10')
        self.assertEqual(decimal_to_binary(3), '11')
        self.assertEqual(decimal_to_binary(4), '100')
        self.assertEqual(decimal_to_binary(5), '101')
        self.assertEqual(decimal_to_binary(8), '1000')
        self.assertEqual(decimal_to_binary(1024), '10000000000')

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('1010'), 10)
        self.assertEqual(binary_to_decimal('0'), 0)
        self.assertEqual(binary_to_decimal('11111111'), 255)
        self.assertEqual(binary_to_decimal('1'), 1)
        self.assertEqual(binary_to_decimal('10'), 2)
        self.assertEqual(binary_to_decimal('11'), 3)
        self.assertEqual(binary_to_decimal('100'), 4)
        self.assertEqual(binary_to_decimal('101'), 5)
        self.assertEqual(binary_to_decimal('1000'), 8)
        self.assertEqual(binary_to_decimal('0001010'), 10)

    def test_round_number(self):
        self.assertEqual(round_number(3.14159, 2), 3.14)
        self.assertEqual(round_number(2.675, 2), 2.68)
        self.assertEqual(round_number(1.2345, 3), 1.235)
        self.assertEqual(round_number(1.2345, 4), 1.2345)
        self.assertEqual(round_number(1.235, 2), 1.24)
        self.assertEqual(round_number(1.225, 2), 1.23)
        self.assertEqual(round_number(0.0, 5), 0.0)
        self.assertEqual(round_number(3.14159, 3), 3.142)
        self.assertEqual(round_number(999.9999, 3), 1000.0)
        self.assertEqual(round_number(123.0, 0), 123.0)

    def test_truncate_number(self):
        self.assertEqual(truncate_number(3.14159, 2), 3.14)
        self.assertEqual(truncate_number(2.6789, 3), 2.678)
        self.assertEqual(truncate_number(1.9999, 0), 1.0)
        self.assertEqual(truncate_number(1.2345, 1), 1.2)
        self.assertEqual(truncate_number(1.2345, 4), 1.2345)
        self.assertEqual(truncate_number(0.0, 3), 0.0)
        self.assertEqual(truncate_number(10.0, 3), 10.0)
        self.assertEqual(truncate_number(123.456789, 5), 123.45678)
        self.assertEqual(truncate_number(3.14159, 3), 3.141)
        self.assertEqual(truncate_number(2.6789, 2), 2.67)

    def test_absolute_error(self):
        self.assertAlmostEqual(absolute_error(3.14, 3.14159), 0.00159)
        self.assertAlmostEqual(absolute_error(3.14159, 3.14), 0.00159)
        self.assertAlmostEqual(absolute_error(0.0, 0.0), 0.0)
        self.assertAlmostEqual(absolute_error(-1.0, -1.0), 0.0)
        self.assertAlmostEqual(absolute_error(-1.0, 1.0), 2.0)
        self.assertAlmostEqual(absolute_error(1.0, -1.0), 2.0)
        self.assertAlmostEqual(absolute_error(10.5, 10.0), 0.5)
        self.assertAlmostEqual(absolute_error(10.0, 10.5), 0.5)
        self.assertAlmostEqual(absolute_error(1e-9, 0.0), 1e-9)
        self.assertAlmostEqual(absolute_error(123456.789, 123456.788), 0.001)

    def test_relative_error(self):
        self.assertAlmostEqual(relative_error(3.14, 3.14159), 0.000506, places=6)
        self.assertAlmostEqual(relative_error(3.14159, 3.14), 0.000506, places=6)
        self.assertAlmostEqual(relative_error(10.0, 10.0), 0.0)
        self.assertAlmostEqual(relative_error(-10.0, -10.0), 0.0)
        self.assertAlmostEqual(relative_error(9.0, 10.0), 0.1)
        self.assertAlmostEqual(relative_error(11.0, 10.0), 0.1)
        self.assertAlmostEqual(relative_error(-9.0, -10.0), 0.1)
        self.assertAlmostEqual(relative_error(-11.0, -10.0), 0.1)
        self.assertAlmostEqual(relative_error(0.0, 10.0), 1.0)
        self.assertAlmostEqual(relative_error(1e-9, 1e-8), 0.9)
