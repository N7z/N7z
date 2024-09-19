# Calculadora de equações do segundo grau

# Bibliotecas
from os import system
from time import sleep
from math import sqrt
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Aplicação Principal
def main():
    title_helper()

    # Pergunta os valores a, b e c.
    a = input_helper("Qual o valor A: ")
    b = input_helper("Qual o valor B: ")
    # Valor C pode ser vazio em expressões de segundo grau, então se
    # usuário não escrever nada, fica 0 mesmo
    c = input_helper("Qual o valor C: ", podeSerVazio=True) or 0

    resolver_equacao(a, b, c)
    
def resolver_equacao(a, b, c):
    title_helper()
    print(f"{Fore.YELLOW}A = {a} ｜ B = {b} ｜ C = {c}\n")

    # Função helper para resolver delta de forma organizada
    delta = resolver_delta(a, b, c)

    # Se delta for negativo, informar que não há soluções reais
    if delta < 0:
        print(f"{Fore.RED}Delta negativo. Não há soluções reais.")
        return

    # Função helper para resolver o resto da bhaskara
    bhaskara = resolver_bhaskara(a, b, c, delta)

    print(f"\n{Fore.GREEN}O resultado da operação é")
    print(f"{Fore.CYAN}X¹ = {bhaskara[0]:.2f} ｜ X² = {bhaskara[1]:.2f}")

def resolver_delta(a, b, c):
    # Delta é b² - 4 x a x c
    print(f"{Fore.MAGENTA}Δ = {b}² - 4 × {a} × {c}")
    print(f"{Fore.MAGENTA}Δ = {b**2} - {4*a*c}")

    delta = (b ** 2) - (4 * a * c)
    print(f"{Fore.MAGENTA}Δ = {delta}\n")
    return delta

def resolver_bhaskara(a, b, c, delta):
    # Lembrando que bhaskara é (-b ± sqrt(delta)) / 2 x a
    menos_b = b * -1

    print(f"{Fore.BLUE}          -{b} ± √{delta}")
    print(f"{Fore.BLUE}X = ———————————————")
    print(f"{Fore.BLUE}        2 × {a}")

    # Bhaskara tem dois resultados
    resultado_1 = (menos_b + sqrt(delta)) / (2 * a)
    resultado_2 = (menos_b - sqrt(delta)) / (2 * a)

    return [resultado_1, resultado_2]

def input_helper(message, podeSerVazio=False):
    while True:
        resposta = input(message).strip()
        if podeSerVazio and resposta == "":
            return 0
        try:
            return float(resposta)
        except ValueError:
            if podeSerVazio:
                return 0
            print(f"{Fore.RED}Erro de digitação. Tente novamente!")
            sleep(1)

def title_helper():
    system('clear')
    print(f"{Fore.YELLOW}Calculadora de Equações do 2° Grau\n")

if __name__ == '__main__':  
    main()