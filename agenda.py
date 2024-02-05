contatos = []

def mostrar_menu():
    print("\n*** Agenda de Contatos ***")
    print("1. Adicionar Contato")
    print("2. Visualizar Contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar Favorito")
    print("5. Ver Contatos Favoritos")
    print("6. Apagar Contato")
    print("7. Sair")

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    favorito = input("Marcar como favorito? (S/N): ").upper()

    contato = {"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": favorito == "S"}
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

def visualizar_contatos():
    print("\n*** Lista de Contatos ***")
    for indice, contato in enumerate(contatos, start=1):
        print(f"{indice}. {contato['Nome']} - {contato['Telefone']} - {contato['Email']} - Favorito: {contato['Favorito']}")

def editar_contato():
    visualizar_contatos()
    indice = int(input("Digite o número do contato que deseja editar: ")) - 1

    if 0 <= indice < len(contatos):
        nome = input("Novo nome (ou pressione Enter para manter o mesmo): ")
        telefone = input("Novo telefone (ou pressione Enter para manter o mesmo): ")
        email = input("Novo email (ou pressione Enter para manter o mesmo): ")

        contatos[indice]["Nome"] = nome if nome else contatos[indice]["Nome"]
        contatos[indice]["Telefone"] = telefone if telefone else contatos[indice]["Telefone"]
        contatos[indice]["Email"] = email if email else contatos[indice]["Email"]

        print("Contato editado com sucesso!")
    else:
        print("Índice inválido!")

def marcar_desmarcar_favorito():
    visualizar_contatos()
    indice = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1

    if 0 <= indice < len(contatos):
        contatos[indice]["Favorito"] = not contatos[indice]["Favorito"]
        print("Status de favorito atualizado com sucesso!")
    else:
        print("Índice inválido!")

def ver_contatos_favoritos():
    print("\n*** Contatos Favoritos ***")
    favoritos = [contato for contato in contatos if contato["Favorito"]]
    if favoritos:
        for i, favorito in enumerate(favoritos, start=1):
            print(f"{i}. {favorito['Nome']} - {favorito['Telefone']} - {favorito['Email']}")
    else:
        print("Nenhum contato favorito encontrado.")

def apagar_contato():
    visualizar_contatos()
    indice = int(input("Digite o número do contato que deseja apagar: ")) - 1

    if 0 <= indice < len(contatos):
        del contatos[indice]
        print("Contato apagado com sucesso!")
    else:
        print("Índice inválido!")

while True:
    mostrar_menu()
    escolha = input("\nDigite o número da opção desejada: ")

    if escolha == "1":
        adicionar_contato()
    elif escolha == "2":
        visualizar_contatos()
    elif escolha == "3":
        editar_contato()
    elif escolha == "4":
        marcar_desmarcar_favorito()
    elif escolha == "5":
        ver_contatos_favoritos()
    elif escolha == "6":
        apagar_contato()
    elif escolha == "7":
        print("Saindo da aplicação. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
