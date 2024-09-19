# IMC = Peso / Altura em metros²

# Bibliotecas
from os import system
from time import sleep
from colorama import Fore, Style, init

# Inicia o colorama
init(autoreset=True)

# Tipos de IMC
imc_tipo = {
    0:    "Abaixo do normal",
    18.5: "Normal",
    24.9: "Sobrepeso",
    29.9: "Obesidade Grau I",
    34.9: "Obesidade Grau II",
    39.9: "Obesidade Grau III"
}

# Aplicação principal
def main():
    title_helper()

    # Pergunta peso e altura
    peso = input_helper("Por favor insira seu peso (ex: 60.5): ", isFloat=True)
    altura = input_helper("Por favor insira sua altura em centímetros (ex: 165): ")

    # Chama helper pra manter o código limpo
    resolver_imc(peso=peso, altura=altura)

# Função Helper para resolver o IMC com peso e altura
def resolver_imc(peso, altura):
    # Converte altura de cm para m
    altura_em_metros = altura / 100

    # Faz o cálculo de IMC que é Peso em kg / Altura em metros²
    imc = peso / (altura_em_metros ** 2)

    # Encontra o tipo de IMC
    imc_classificacao = classificar_imc(imc)

    title_helper()
    print(f"Seu IMC é de: {Fore.CYAN}{imc:.2f}{Style.RESET_ALL}")
    print(f"Classificação: {Fore.GREEN}{imc_classificacao}\n{Style.RESET_ALL}")

    # Calcula o peso ideal para IMC normal (entre 18.5 e 24.9)
    peso_normal_min = 18.5 * (altura_em_metros ** 2)
    peso_normal_max = 24.9 * (altura_em_metros ** 2)

    if imc < 18.5:
        # Pessoa abaixo do peso, precisa engordar até peso normal
        peso_necessario = peso_normal_min - peso
        print(f"{Fore.YELLOW}Você precisa engordar {peso_necessario:.2f} kg para atingir um IMC normal.{Style.RESET_ALL}")
    elif imc > 24.9:
        # Pessoa acima do peso, precisa emagrecer até peso normal
        peso_necessario = peso - peso_normal_max
        print(f"{Fore.RED}Você precisa emagrecer {peso_necessario:.2f} kg para atingir um IMC normal.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Seu peso já está dentro da faixa de IMC normal.{Style.RESET_ALL}")

# Função para classificar o IMC baseado nos valores
def classificar_imc(imc):
    for limite in sorted(imc_tipo.keys(), reverse=True):
        if imc > limite:
            return imc_tipo[limite]
    return imc_tipo[0]

# Função Helper para pegar input limpo e válido
# com parâmetro float sendo padrão falso pra não precisar de outra função
def input_helper(message, isFloat=False):
    while True:
        try:
            title_helper()
            
            # Expressão Condicional / Operador ternário para não usar if else
            resposta = float(input(message)) if isFloat else int(input(message))
            break
        except ValueError:
            title_helper()
            print(f"{Fore.RED}Erro de digitação. Digite novamente!{Style.RESET_ALL}")
            sleep(1)
            
    return resposta

def title_helper():
    system('clear')  # Limpa o console
    print(f"{Fore.CYAN}Calculadora de IMC\n{Style.RESET_ALL}")

# Inicia a aplicação
if __name__ == '__main__':
    main()