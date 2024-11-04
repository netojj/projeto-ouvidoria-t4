'''

'''

opcao = 1;
manifestacoes = [ ];

while opcao != 7:
    print("\nOpções: \n1)Listagem das Manifestações\n2)Criar uma nova Manifestação\n3)Exibir quantidade de manifestações\n"
          "4)Pesquisar uma manifestação por código\n5)Excluir uma Manifestação pelo Código\n6)Sair do Sistema.");
    opcao = int(input("Digite sua opção: "));

    if opcao == 1:
        if len(manifestacoes) > 0:
            print("Lista de Manifestações:")
            for index in range(len(manifestacoes)):
                print(index+1,"-",manifestacoes[index])

        else:
            print("Não existem manifestações a serem exibidas!")
