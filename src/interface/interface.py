from src.calculadora.calculadora import Calculadora

# TODO: FIX ALL THE DOCSTRINGS BELOW
class Interface():
    '''
    Classe para representar uma interface.
    '''

    def __init__(self):
        print("Instanciando uma nova interface...")

        self.__calculadora = Calculadora()

    
    def __del__(self):
        del self.__calculadora

        print('\nObrigado por usar nossa calculadora!')



    def __exibir_menu(self):
        '''
        Método para exibir somente as opções do menu.
        '''

        print("""
        ==========================================
        | Escolha uma das opções do menu abaixo: |
        |           1 - Soma                     |   
        |           2 - Subtração                |
        |           3 - Multiplicação            |
        |           4 - Divisão                  |
        |           5 - Sair                     |
        ==========================================
        """)


    def __get_input(self, text='Digite a opção desejada: '):
        '''
        Método para ler o texto do usuário.
        '''

        return input(text)


    def __escolher_opcao_menu(self, opcao):
        '''
        Método para escolher qual operação realizar.
        '''

        if opcao == '5':
            self.__del__()
            return False

        return self.__realizar_operacao(opcao)        


    def __realizar_operacao(self, opcao):
        '''
        Método para realizar a operação desejada.
        '''

        a = int( self.__get_input('Digite o primeiro número: ') )
        b = int( self.__get_input('Digite o segundo número: ') )

        if opcao == '1':
            resultado = self.__calculadora.realizar_soma(a, b)
        elif opcao == '2':
            resultado = self.__calculadora.realizar_subtracao(a, b)
        elif opcao == '3':
            resultado = self.__calculadora.realizar_multiplicacao(a, b)
        elif opcao == '4':
            resultado = self.__calculadora.realizar_divisao(a, b)
        else:
            print('Opção inválida. Por favor, digite novamente.')
            return False

        return resultado


    def __printar_resultado(self, resultado):
        print(f'O resultado da operação é: {resultado}')


    def menu(self):
        '''
        Método para exibir o menu, pegar a opção desejada do usuário
        e realizar a operação segundo a opção desejada.
        '''

        self.__exibir_menu()        

        opcao = self.__get_input()

        resultado = self.__escolher_opcao_menu(opcao)

        if resultado:
            self.__printar_resultado(resultado)

        self.menu()
        



    