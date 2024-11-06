'''
André Holanda
Bruna Neves
Esdras de Menezes
Felipe Monteiro
Ithalo Teodósio
José Neto
Priscilla Lima
Samuel Ferreira
'''

opcao = 1
manifestacoes = []
print("====== Ouvidoria - Universidade XYZ ======")
menu = ('''
    Menu de Opções:
    1) Listagem das manifestações
    2) Criar uma nova manifestação
    3) Exibir quantidade de manifestações
    4) Pesquisar uma manifestação por código
    5) Excluir uma manifestação pelo código
    6) Sair do sistema
    ''')

while opcao != 6:
    
    print(menu)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        if len(manifestacoes) > 0:
            print("Lista de manifestações")
            for i, item in enumerate(manifestacoes):
                print(f"{i + 1} - {item}")
            print("\n")

        else:
            print("\nNão existem manifestações a serem exibidas.\n")

    elif opcao == 2:
        novaManifestacao = input("\nDigite aqui a sua nova manifestação: ")
        manifestacoes.append(novaManifestacao)
        print("Manifestação criada com sucesso!\n")

    elif opcao == 3:
        quantidade = len(manifestacoes)
        if quantidade == 0:
            print("\nAtualmente não temos manifestações registradas em nosso sistema.\n")

        elif quantidade == 1:
            print("\nAtualmente temos 1 manifestação registrada em nosso sistema.\n")

        else:
            print("\nAtualmente temos", quantidade, "manifestações registradas em nosso sistema.\n")

    elif opcao == 4:
        if len(manifestacoes) == 0:
            print("\nNão há nenhuma manifestação para pesquisar!\n")

        else:
            codigoManifestacao = int(input("\nDigite o código da manifestação que deseja pesquisar: "))
            if codigoManifestacao >= 1 and codigoManifestacao <= len(manifestacoes):
                print(f"\nManifestação encontrada: {manifestacoes[codigoManifestacao - 1]} \n")
            else:
                print("\nManifestação não encontrada.\n")

    elif opcao == 5:
        if len(manifestacoes) == 0:
            print("\nNão existem manifestações a serem removidas\n")

        else:
            print("\nManifestações: ")
            for index in range(len(manifestacoes)):
                print(index + 1, "-", manifestacoes[index])

            excluirPosicao = int(input("\nDigite o código da manifestação que deseja excluir: "))

            if excluirPosicao >= 1 and excluirPosicao <= len(manifestacoes):
                confirmar = int(
                    input(f"\nDeseja realmente remover a manifestação \"{manifestacoes[excluirPosicao - 1]}\"?  \n   1) para Sim e 2 para Não "))
                if confirmar == 1:
                    manifestacoes.pop(excluirPosicao - 1)
                    print("   Manifestação removida com sucesso\n")
                elif confirmar != 2:
                    print("   Opção inválida\n")
            else:
                print("Manifestação inválida\n")

    elif opcao != 6:
        print("\nOpção Inválida! Tente novamente.")

print("\n====== Obrigado por usar o programa da Ouvidoria. Até a próxima! ======")
