# main.py
from bypasssafe.account import MasterAccount, Account
from bypasssafe.database import Database
from bypasssafe.pass_gen import PasswordGenerator
import os
import sys
import time
import pathlib as Path

"""
Adicionando o diretório raiz do projeto ao path do Python.
"""
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def login(cached_email=None):
    """
    Realiza o processo de login do usuário.

    Args:
        cached_email (str): O email armazenado em cache. Pode ser None se não houver nenhum em cache.

    Returns:
        tuple: Uma tupla contendo o ID do mestre e o email do usuário logado. Retorna (None, None) em caso de falha no login.
    """
    email = input("Email: ")
    password = input("Senha Mestre: ")

    try:
        master_id = Database.authenticate_user(email, password)
        if master_id is not None:
            print("Login realizado com sucesso.")
            return master_id, email
        else:
            print("Falha no Login. Email ou senha inválido.")
            return None, None
    except Exception as e:
        print(f"Um erro ocorreu durante o login: {e}")
        return None, None

def create_master_account():
    """
    Cria uma conta mestre no sistema.

    Solicita informações do usuário, cria uma conta mestre e a salva no banco de dados.
    """
    username = input("Digite seu nome: ")
    email = input("Digite seu Email: ")
    password = input("Digite sua senha mestra: ")

    master_account = MasterAccount(username, password, email)

    try:
        if Database.save_master_account(master_account):
            print("Falha ao criar a conta.")
        else:
            print("Conta Criada com sucesso! Faça login já.")
    except Exception as e:
        print(f"ERRO: {e}")

def create_account(master_id):
    """
    Cria uma nova conta associada à conta mestre fornecida.

    Solicita informações do usuário, cria uma conta e a salva no banco de dados.

    Args:
        master_id (int): O ID da conta mestre à qual a nova conta será associada.
    """
    username = input("Digite o username: ")
    email = input("Digite o email: ")
    choice = input("Deseja digitar ou gerar uma senha? (1 - Digitar / 2 - Gerar): ")

    if choice == "1":
        password = input("Digite a senha: ")
    elif choice == "2":
        password = generate_password()
    else:
        print("Por favor, digite uma opção válida. (1 ou 2)")
        return

    account = Account(master_id, username, password, email)
    Database.save_account(account)

def generate_password():
    """
    Gera uma senha aleatória com base nas preferências do usuário.

    Retorna:
        str: A senha gerada.
    """
    password_generator = PasswordGenerator()
    length = int(input("Qual o tamanho da senha: "))
    digits = int(input("Digite a quantidade de números: "))
    symbols = int(input("Digite a quantidade de símbolos: "))
    uppercase = (input("Deseja misturar letras maiúsculas com minúsculas? (S/N): ").lower() == "S")

    password = password_generator.generate_password(length, digits, symbols, uppercase)
    print(f"Senha Gerada: {password}")
    return password

def search_account(master_id, username_to_search):
    """
    Procura e exibe informações sobre uma conta associada à conta mestre.

    Args:
        master_id (int): O ID da conta mestre à qual a conta a ser pesquisada está associada.
        username_to_search (str): O nome de usuário da conta a ser pesquisada.
    """
    try:
        account = Database.get_account_by_username(master_id, username_to_search)
        if account:
            print(f"Informações da Conta:")
            print(f"Nome: {account.username}")
            print(f"Email: {account.email}")
            print(f"Senha: {account.password}")
            input("Pressione Enter para voltar ao menu...")
        else:
            print(f"Conta com nome '{username_to_search}' não encontrada.")
            input("Pressione Enter para voltar ao menu...")
    except Exception as e:
        print(f"Erro durante a pesquisa: {e}")
        input("Pressione Enter para voltar ao menu...")

def clear_console():
    """Limpa a tela do console."""
    os.system("cls" if os.name == "nt" else "clear")

cached_email = None

def main():
    """
    Função principal do programa.

    Controla o fluxo principal do programa, incluindo a exibição de menus, chamadas de funções e interações com o usuário.
    """
    global cached_email

    master_id = None

    while master_id is None:
        clear_console()
        print("1 - Fazer Login")
        print("2 - Criar Conta Master")
        ja = int(input("Escolha uma opção: "))
        if ja == 1:
            master_id, cached_email = login(cached_email)
        elif ja == 2:
            create_master_account()
        else:
            print("Opção inválida. Por favor, digite um número entre 1 e 2.")

    while True:
        clear_console()
        print("Welcome!")
        print("\nMenu:")
        print("1. Cadastrar Conta")
        print("2. Gerar Senha")
        print("3. Procurar Conta")
        print("4. Sair")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            create_account(master_id)
            time.sleep(2)  # Aguarda 2 segundos antes de limpar o console e mostrar o próximo menu
        elif choice == "2":
            generate_password()
            time.sleep(2)
        elif choice == "3":
            username_to_search = input("Digite o nome da conta que deseja buscar: ")
            search_account(master_id, username_to_search)
            time.sleep(2)
        elif choice == "4":
            print("Fechando. Até mais!")
            break
        else:
            print("Escolha inválida. Por favor, digite um número entre 1 e 4.")
            time.sleep(2)

def register_script():
    # Obter o caminho do script atual
    script_path = Path(__file__).resolve()

    # Obter o caminho do diretório de scripts local
    scripts_dir = Path.home() / ".local" / "bin"

    # Criar o diretório se não existir
    scripts_dir.mkdir(parents=True, exist_ok=True)

    # Criar um link simbólico para o script no diretório de scripts
    link_path = scripts_dir / script_path.name
    link_path.symlink_to(script_path)

    print(f"Script registrado em {link_path}")

if __name__ == "__main__":
    register_script()
    main()
