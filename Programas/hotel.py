# Bibliotecas
import os, time
from colorama import init, Fore, Style

# Inicializa o Colorama para colorir o texto no terminal
init(autoreset=True)

# Classe que representa um quarto de hotel
class HotelRoom:
    def __init__(self, preco_base):
        # Define o preço base do quarto
        self.preco_base = preco_base

    # Método para reservar o quarto e calcular o custo total
    def reservar(self, pessoas, dias):
        # Verifica se a quantidade de pessoas e o número de dias são válidos
        if 1 <= pessoas <= 6 and dias > 0:
            # Calcula o preço total com base no número de pessoas e dias
            preco_total = (self.preco_base + (pessoas - 1) * 8) * dias
            print(f"\n{Fore.GREEN}Quarto reservado para {pessoas} pessoa(s) por {dias} dia(s).")
            print(f"Preço total: {Fore.YELLOW}R${preco_total:.2f}.{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Obrigado pela reserva!{Style.RESET_ALL}")
            return preco_total
        else:
            print(f"\n{Fore.RED}Número de pessoas ou dias inválido. O máximo é 6 pessoas e o mínimo é 1 dia.{Style.RESET_ALL}")
            return 0

# Função para limpar a tela do terminal, funciona em Windows e Unix
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal da aplicação
def main():
    limpar_tela()  # Limpa a tela para iniciar a aplicação
    print(f"{Fore.BLUE}Bem-vindo ao Sistema de Hotel!{Style.RESET_ALL}\n")

    nome = input("Para começar, por favor, informe seu nome: ").strip()
    if not nome:
        # Se o nome não for informado, exibe uma mensagem de erro e reinicia
        print(f"{Fore.RED}Nome não pode ser vazio. Tente novamente.{Style.RESET_ALL}\n")
        time.sleep(1)
        return main()
    
    # Avança para a tela de login
    tela_login(nome)

# Função que exibe a tela de boas-vindas após o login
def tela_login(nome):
    limpar_tela()  # Limpa a tela para mostrar a tela de boas-vindas
    print(f"{Fore.GREEN}Olá, {nome}! Seja bem-vindo(a) ao nosso hotel.{Style.RESET_ALL}\n")

    time.sleep(1.5)  # Pausa por 1.5 segundos para a transição

    tela_reserva(nome)  # Avança para a tela de reserva

# Função que exibe a tela para reserva de quartos
def tela_reserva(nome):
    limpar_tela()  # Limpa a tela para mostrar a tela de reserva
    print(f"{Fore.BLUE}Sistema de Hotel - Logado como {nome}{Style.RESET_ALL}\n")
    
    # Define os preços base para 5 quartos
    preco_quartos = [20, 30, 200, 680, 1024]
    quartos = [HotelRoom(preco) for preco in preco_quartos]  # Cria uma lista de objetos HotelRoom

    # Exibe a lista de quartos disponíveis
    print(f"{Fore.YELLOW}Aqui estão os quartos disponíveis:{Style.RESET_ALL}")
    for i, quarto in enumerate(quartos, start=1):
        print(f"{Fore.CYAN}Quarto {i}: A partir de R${quarto.preco_base:.2f}")

    # Obtém a escolha do quarto do usuário
    escolha = obter_escolha(f"Escolha o número do quarto que deseja reservar (1-{len(quartos)}): ", 1, len(quartos))

    # Obtém a quantidade de pessoas e o número de dias
    quarto_selecionado = quartos[escolha - 1]
    pessoas = obter_escolha("Quantas pessoas ficarão no quarto? (1-6): ", 1, 6)
    dias = obter_escolha("Quantos dias você pretende ficar? (1 ou mais): ", 1, 365)

    # Faz a reserva do quarto
    quarto_selecionado.reservar(pessoas, dias)

# Função para obter uma escolha válida do usuário
def obter_escolha(mensagem, minimo, maximo):
    while True:
        try:
            # Solicita a entrada do usuário
            escolha = int(input(f"{Fore.GREEN}{mensagem}{Style.RESET_ALL}"))
            # Verifica se a escolha está dentro do intervalo permitido
            if minimo <= escolha <= maximo:
                return escolha
            else:
                print(f"{Fore.RED}Por favor, escolha um número entre {minimo} e {maximo}.{Style.RESET_ALL}")
        except ValueError:
            # Trata entradas inválidas
            print(f"{Fore.RED}Entrada inválida. Digite um número.{Style.RESET_ALL}")

# Inicia a aplicação
if __name__ == '__main__':
    main()