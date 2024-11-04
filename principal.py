'''

'''

opcao = 1;
manifestacoes = [ ];
print("Ouvidoria - Universidade XYZ")

while opcao != 7:
    print("\nOpções: \n1)Listagem das Manifestações\n2)Criar uma nova Manifestação\n3)Exibir quantidade de manifestações\n"
          "4)Pesquisar uma manifestação por código\n5)Excluir uma Manifestação pelo Código\n6)Sair do Sistema.");
    opcao = int(input("Digite sua opção: "));

    if opcao == 1:
        if len(manifestacoes) > 0:
            print("Lista de Manifestações:")
            for index in range(len(manifestacoes)):
                print(index+1,"-",manifestacoes[index]);

        else:
            print("Não existem manifestações a serem exibidas!");

    elif opcao == 2:
        novaManifestacao = input("Digite a manifestação: ");
        manifestacoes.append(novaManifestacao);
        print("Manifestação cadastrada com sucesso!")

    elif opcao == 3:
        palavraPlural = "manifestações cadastradas" if len(manifestacoes) > 1 else "manifestação cadastrada"
        print(f'Temos um total de {len(manifestacoes)} {palavraPlural} em sistema');

