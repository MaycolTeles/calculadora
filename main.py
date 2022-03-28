import os

from src.interface.interface import Interface


def main():

    # Limpando o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    interface = Interface()
    
    interface.menu()


if __name__ == '__main__':
    main()

