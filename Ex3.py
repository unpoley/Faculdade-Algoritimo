import os
produtos = []

def adicionar_produtos():
    nome = str(input("Digite o nome do produto. "))
    categoria = str(input("Digite a categoria do produto. "))
    while True:
        try:
            preco = float(input("Digite o preco unitario do produto. "))
            if preco > 0:
                break
            else:
                print("Digite corretamente o preco. ")
        except ValueError:
            print("entrada invalida")
    while True:
        try:
            quantidade = int(input("Digite a quantidade. "))
            if quantidade > 0:
                break
            else:
                print("Digite corretamente o preco. ")
        except ValueError:
            print("entrada invalida")

    produto = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)    

def atualizar_estoque():
    while True:
        nome = input("Digite o nome do produto. ")
        qtd = float(input("Digite a quantidade. "))
        for p in produtos:
            if p["nome"].lower() == nome.lower():
                if qtd > 0:
                    p["quantidade"] += qtd
                    print(f"estoque do produto {p["nome"]} foi atualizado para {p["quantidade"]}")
                elif qtd < 0:
                    p["quantidade"] -= qtd
                    print(f"estoque do produto {p["nome"]} foi atualizado para {p["quantidade"]}")
                else:
                    print("vai mudar nada nao")
                    break

def lista_produtos():
    for p in produtos:
        print(p["nome"] - p["quantidade"])

def ordenar_produtos():
    escolha = int(input("vai querer odernar por preco(1) ou por produto(2)"))
    if escolha == 1:
        escolha2 = int(input("Digite (1) se quiser ordenar em cresente ou (2) para decrescente. "))
        if escolha2 == 1:
            produtos.sort(key=lambda x: x["preco"], reverse=False)
            for p in produtos:
                print(p["nome"],p["preco"])
        else:
            produtos.sort(key=lambda x: x["preco"], reverse=True)
            for p in produtos:
                print(p["nome"],p["preco"])
    else:
        escolha2 = int(input("Digite (1) se quiser ordenar em cresente ou (2) para decrescente. "))
        if escolha2 == 1:
            produtos.sort(key=lambda x: x["quantidade"], reverse=False)
            for p in produtos:
                print(p["nome"],p["quantidade"])
        else:
            produtos.sort(key=lambda x: x["quantidade"], reverse=True)
            for p in produtos:
                print(p["nome"],p["quantidade"])

def salvar_produtos():
    try:
        if os.path.exists("estoque.txt"):
            escolha = input("O arquivo ja existe. Deseja sobreescrever? (sim/nao): ")
            if escolha.lower() != "sim":
                print("Operaçao cancelada.")
                return
            with open("biblioteca.txt", "w") as arquivo:
                for produto in produtos:
                    arquivo.write(f"{produto["titulo"]},{produto["autor"]},{produto["ano"]},{produto["paginas"]}\n")
            print("Dados salvos em estoque.txt")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def carregar_produtos():
    try:
        if not os.path.exists("estoque.txt"):
            print("nenhum arquivo encontrado. ")
            return
        
        with open("estoque.txt", "r") as arquivo:
            for linha in arquivo:
                try:
                    nome, categoria, precostr, quantidadestr = linha.strip().split(",")
                    preco = float(precostr)
                    quantidade = float(quantidadestr)
                    produto = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
                    produtos.append(produto)
                except ValueError:
                    print(f"linha invalida no arquivo: {linha.strip()}")
    except Exception as e:
        print(f"erro ao carregar o arquivo: {e}")
    

while True:
    print("\n===Bem-vindo ao Sistema de Gestao de Estoque===")
    print("1. Adicionar produtos")
    print("2. Listar produtos")
    print("3. Ordenar produtos")
    print("4. Salvar produtos")
    print("5. Carregar produtos")
    print("0. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_produtos()
    elif opcao == "2":
        lista_produtos()
    elif opcao == "3":
        ordenar_produtos()
    elif opcao == "4":
        salvar_produtos()
    elif opcao == "5":
        carregar_produtos()
    elif opcao == "0":
        print("Até logo! ")
        break