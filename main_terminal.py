# main.py
from atributos import *
from dominios import *

dentistas = []
tecnicos = []
pacientes = []
trabalhos = []


def registrar_dentista():
    print("\n=== Registrar Dentista ===")
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")
    try:
        dentista = Dentista(nome, login, senha)
        dentistas.append(dentista)
        print("Dentista registrado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")


def registrar_tecnico():
    print("\n=== Registrar Técnico ===")
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")
    try:
        tecnico = Tecnico(nome, login, senha)
        tecnicos.append(tecnico)
        print("Técnico registrado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")


def login_usuario(lista, tipo_usuario):
    print(f"\n=== Login de {tipo_usuario} ===")
    login = input("Login: ")
    senha = input("Senha: ")
    for usuario in lista:
        if usuario.login.login == login and usuario.senha.verificar(senha):
            print(f"Login bem-sucedido! Bem-vindo(a), {usuario.nome}.")
            return usuario
    print("Login ou senha incorretos.")
    return None


def registrar_paciente(dentista):
    print(f"\n=== Registrar Paciente ({dentista.nome}) ===")
    nome = input("Nome do paciente: ")
    id_paciente = len(pacientes) + 1
    paciente = Paciente(nome, id_paciente)
    pacientes.append(paciente)
    print(f"Paciente registrado com sucesso! ID: {id_paciente}")


def criar_trabalho(dentista):
    print(f"\n=== Criar Trabalho ({dentista.nome}) ===")
    if not pacientes:
        print("Nenhum paciente registrado.")
        return
    if not tecnicos:
        print("Nenhum técnico registrado.")
        return

    # Escolher paciente
    print("\nPacientes:")
    for p in pacientes:
        print(f"{p.idPaciente} - {p.nome}")
    id_pac = int(input("ID do paciente: "))
    paciente = next((p for p in pacientes if p.idPaciente == id_pac), None)
    if not paciente:
        print("Paciente não encontrado.")
        return

    # Escolher técnico
    print("\nTécnicos disponíveis:")
    for i, t in enumerate(tecnicos, start=1):
        print(f"{i} - {t.nome}")
    idx = int(input("Escolha o técnico: ")) - 1
    if idx < 0 or idx >= len(tecnicos):
        print("Técnico inválido.")
        return
    tecnico = tecnicos[idx]

    # Dados do trabalho
    data_inicio = input("Data de início (DD/MM/AAAA): ")
    data_final = input("Data final (DD/MM/AAAA): ")
    tipo = input("Tipo de trabalho (Coroa, Inlay, Faceta...): ")
    dentes = input("Dentes (ex: 11,12,13): ").split(",")
    cor = input("Cor (ex: A2): ")
    translucidez = input("Translucidez (ex: LT, HT) (Pressione Enter para nenhum): ")

    try:
        trabalho = Trabalho(paciente, tecnico, data_inicio, data_final, tipo, dentes, cor, translucidez)
        trabalhos.append(trabalho)
        print("\n✅ Trabalho registrado com sucesso!")
        print(trabalho)
    except Exception as e:
        print(f"Erro: {e}")


def listar_trabalhos():
    print("\n=== Trabalhos Registrados ===")
    if not trabalhos:
        print("Nenhum trabalho cadastrado.")
        return
    for i, t in enumerate(trabalhos, start=1):
        print(f"\n{i}. {t}")


def menu_principal():
    while True:
        print("\n===== CLÍNICA ODONTOLÓGICA =====")
        print("1. Registrar Dentista")
        print("2. Registrar Técnico")
        print("3. Login Dentista")
        print("4. Login Técnico")
        print("0. Sair")

        opc = input("Escolha: ")

        if opc == "1":
            registrar_dentista()
        elif opc == "2":
            registrar_tecnico()
        elif opc == "3":
            dentista = login_usuario(dentistas, "Dentista")
            if dentista:
                menu_dentista(dentista)
        elif opc == "4":
            tecnico = login_usuario(tecnicos, "Técnico")
            if tecnico:
                menu_tecnico(tecnico)
        elif opc == "0":
            print("Saindo... 👋")
            break
        else:
            print("Opção inválida.")


def menu_dentista(dentista):
    while True:
        print(f"\n=== Menu Dentista ({dentista.nome}) ===")
        print("1. Registrar Paciente")
        print("2. Criar Trabalho")
        print("3. Listar Trabalhos")
        print("0. Voltar")

        opc = input("Escolha: ")

        if opc == "1":
            registrar_paciente(dentista)
        elif opc == "2":
            criar_trabalho(dentista)
        elif opc == "3":
            listar_trabalhos()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")


def menu_tecnico(tecnico):
    print(f"\n=== Menu Técnico ({tecnico.nome}) ===")
    print("Trabalhos atribuídos:")
    encontrados = [t for t in trabalhos if t.tecnico == tecnico]
    if not encontrados:
        print("Nenhum trabalho encontrado.")
    else:
        for t in encontrados:
            print(t)
    input("\nPressione Enter para voltar.")


if __name__ == "__main__":
    menu_principal()