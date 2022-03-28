from src.calculadora.calculadora import Calculadora

import unittest

# TODO: FIX ALL THE DOCSTRINGS BELOW
class TestCalculadora(unittest.TestCase):
    '''
    Classe para testar a classe Calculadora.

    Methods
    -------
    test_realizar_soma() : int, float
        - Se for possível realizar a soma, retorna a soma do valor a pelo valor b.
        - Se não for possível, retorna False.

    test_realizar_subtracao() : int, float
        - Se for possível realizar a subtração, retorna a subtração do valor a pelo valor b.
        - Se não for possível, retorna False.

    test_realizar_multiplicacao() : int, float
        - Se for possível realizar a multiplicação, retorna a multiplicação do valor a pelo valor b.
        - Se não for possível, retorna False.

    test_realizar_divisao() : int, float
        - Se for possível realizar a divisão, retorna a divisão do valor a pelo valor b.
        - Se não for possível, retorna False.
    '''

    def __init__(self, *args, **kwargs):
        super(TestCalculadora, self).__init__(args, kwargs)
        self.__test_calculadora = Calculadora()
        print('Iniciando os testes...')


    def __test_realizar_soma(self):
        '''
        Função para testar a soma da calculadora.
        '''

        self.assertEqual(self.__test_calculadora.realizar_soma(3, 2), 5)


    def __test_realizar_subtracao(self):
        '''
        Função para testar a subtração da calculadora.
        '''

        self.assertEqual(self.__test_calculadora.realizar_subtracao(3, 2), 1)


    def __test_realizar_multiplicacao(self):
        '''
        Função para testar a multiplicação da calculadora.
        '''

        self.assertEqual(self.__test_calculadora.realizar_multiplicacao(3, 2), 6)


    def __test_realizar_divisao(self):
        '''
        Função para testar a divisão da calculadora.
        '''

        self.assertEqual(self.__test_calculadora.realizar_divisão(3, 2), 1.5)




if __name__ == '__main__':
    unittest.main()