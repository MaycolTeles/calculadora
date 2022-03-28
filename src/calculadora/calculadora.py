
class Calculadora():
    '''
    Classe para representar uma calculadora.

    Methods
    -------
    realizar_soma() : int, float
        - Se for possível realizar a soma, retorna a soma do valor a pelo valor b.
        - Se não for possível, retorna False.

    realizar_subtracao() : int, float
        - Se for possível realizar a subtração, retorna a subtração do valor a pelo valor b.
        - Se não for possível, retorna False.

    realizar_multiplicacao() : int, float
        - Se for possível realizar a multiplicação, retorna a multiplicação do valor a pelo valor b.
        - Se não for possível, retorna False.

    realizar_divisao() : int, float
        - Se for possível realizar a divisão, retorna a divisão do valor a pelo valor b.
        - Se não for possível, retorna False.
    '''

    def __init__(self):
        print("Instanciando uma nova calculadora...")


    # DOCUMENTAÇÃO BASEADA EM: - Numpydoc
    def __somar(self, a, b):
        '''
        Método para retornar a soma dos valores recebidos como parâmetros.
        (a + b)

        Parameters
        ----------
        a : int, float
            Um valor qualquer a ser somado.

        b: int, float
            Um valor qualquer a ser somado.

        Returns
        -------
        int, float:
            A soma dos dois valores recebidos como parâmetros.
        '''

        return a + b


    # DOCUMENTAÇÃO BASEADA EM: - reST
    def __subtrair(self, a, b):
        '''
        Método para retornar a subtração dos valores recebidos como parâmetros.
        (a - b)

        :param a: Um valor qualquer.
        :param b: Um valor qualquer a ser subtraído.

        :returns: A subtração do valor a pelo valor b.
        '''

        return a - b


    def __multiplicar(self, a, b):
        '''
        Método para retornar a multiplicação dos valores recebidos como parâmetros.
        (a * b)

        Parameters
        ----------
        a : int, float
            Um valor qualquer a ser multiplicado.

        b : int, float
            Um valor qualquer a ser multiplicado.

        Returns
        -------
        int, float:
            A multiplicação entre os valores recebidos como parâmetros.
        '''

        return a * b


    def __dividir(self, a, b):
        '''
        Método para retornar a divisão dos valores recebidos como parâmetros.
        (a / b)

        :param a: Um valor qualquer para ser o numerador.
        :param b: Um valor qualquer para ser o denominador, diferente de 0.

        :returns: A divisão do valor a pelo valor b.
        '''

        return a / b


    def __realizar_operacao(self, a, b, operacao):
        '''
        Método para verificar se é possível realizar a operação recebida como parâmetro,
        utilizando as variáveis recebidas como parâmetros.
        - Se possível, retorna o resultado da operação;
        - Senão, printa o motivo e retorna False.

        Parameters
        ----------
        a : int, float
            Um valor qualquer.

        b : int, float
            Um valor qualquer.

        operacao : str
            A operação desejada ("somar", "subtrair", "multiplicar" e "dividir").


        Returns
        -------
        int, float, bool:
            - Se for possível realizar a operação desejada, retorna o resultado da operação.
            - Se não for possível, retorna False.
        '''

        try:
            if operacao == 'somar':
                resultado = self.__somar(a, b)

            elif operacao == 'subtrair':
                resultado = self.__subtrair(a, b)

            elif operacao == 'multiplicar':
                resultado = self.__multiplicar(a, b)

            elif operacao == 'dividir':
                resultado = self.__dividir(a, b)

        # TODO: Maybe implement the differents types of possible exceptions here?
        except Exception as e:
            print(f"Não foi possível realizar a operação. Motivo: {e}")
            return False

        # Chamado somente se não houver a interrupção.
        return resultado


    def realizar_soma(self, a, b):
        '''
        Método para verificar se é possível realizar uma soma.
        - Se possível, retorna o valor da soma (a + b);
        - Senão, retorna False.
        
        :param a: Um valor qualquer a ser somado.
        :param b: Um valor qualquer a ser somado.

        :returns:
            - Se for possível realizar a soma, retorna a soma dos dois valores recebidos como parâmetros.
            - Se não for possível, retorna False.
        '''

        return self.__realizar_operacao(a, b, 'somar')


    def realizar_subtracao(self, a, b):
        '''
        Método para verificar se é possível realizar uma subtração.
        - Se possível, retorna o valor da subtração (a - b);
        - Senão, retorna False.

        Parameters
        ----------
        a : int, float
            Um valor qualquer.

        b: int, float
            Um valor qualquer a ser subtraído.

        Returns
        -------
        int, float, bool:
            - Se for possível realizar a subtração, retorna a subtração do valor a pelo valor b.
            - Se não for possível, retorna False.
        '''

        return self.__realizar_operacao(a, b, 'subtrair')


    def realizar_multiplicacao(self, a, b):
        '''
        Método para verificar se é possível realizar uma multiplicação.
        - Se possível, retorna o valor da multiplicação (a * b);
        - Senão, retorna False.
        
        :param a: Um valor qualquer a ser somado.
        :param b: Um valor qualquer a ser somado.

        :returns:
            - Se for possível realizar a soma, retorna a soma dos dois valores recebidos como parâmetros.
            - Se não for possível, retorna False.
        '''

        return self.__realizar_operacao(a, b, 'multiplicar')


    def realizar_divisao(self, a, b):
        '''
        Método para verificar se é possível realizar uma divisão.
        - Se possível, retorna o valor da divisão (a / b);
        - Senão, retorna False.

        Parameters
        ----------
        a : int, float
            Um valor qualquer para ser o numerador.

        b: int, float
            Um valor qualquer para ser o denominador, diferente de 0.

        Returns
        -------
        int, float, bool:
            - Se for possível realizar a divisão, retorna a divisão do valor a pelo valor b.
            - Se não for possível, retorna False.
        '''

        return self.__realizar_operacao(a, b, 'dividir')