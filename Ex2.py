import os
livros = []



def adicionar_livro():
    titulo = str(input("Digite o titulo do livro. "))
    autor = str(input("Digite o autor do livro. "))
    while True:
        try:
            ano = int(input("Digite o ano do livro. "))
            if ano > 0:
                break
            else:
                print("Digite corretamente o ano. ")
        except ValueError:
            print("entrada invalida")
    while True:
        try:
            paginas = int(input("Digite a quantidade de paginas. "))
            if paginas > 0:
                break
            else:
                print("Digite corretamente o numero de paginas. ")
        except ValueError:
            print("entrada invalida")

    

    livro = {"titulo": titulo, "autor": autor, "ano": ano, "paginas": paginas}
    livros.append(livro)
    print(f"o livro: {titulo} foi adicionado com sucesso. ")

def lista_livros():
    for l in livros:
        print(l["titulo"])
    
def ordenar_livros():
    escolha = int(input("Digite (1) se quiser ordenar em cresente ou (2) para decrescente. "))
    if escolha == 1:
        livros.sort(key=lambda x: x["ano"], reverse=False)
        for p in livros:
            print(p["titulo"],p["ano"])
        print
    else:
        livros.sort(key=lambda x: x["ano"], reverse=True)
        for p in livros:
            print(p["titulo"],p["ano"])
def salvar_livros():
    try:
        if os.path.exists("biblioteca.txt"):
            escolha = input("O arquivo ja existe. Deseja sobreescrever? (sim/nao): ")
            if escolha.lower() != "sim":
                print("Operaçao cancelada.")
                return
            with open("biblioteca.txt", "w") as arquivo:
                for livro in livros:
                    arquivo.write(f"{livro["titulo"]},{livro["autor"]},{livro["ano"]},{livro["paginas"]}\n")
            print("Dados salvos em alunos.txt")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
def carregar_livros():
    try:
        if not os.path.exists("biblioteca.txt"):
            print("nenhum arquivo encontrado. ")
            return
        
        with open("biblioteca.txt", "r") as arquivo:
            for linha in arquivo:
                try:
                    titulo, autor, anostr, paginasstr = linha.strip().split(",")
                    ano = float(anostr)
                    paginas = float(paginasstr)
                    livro = {"titulo": titulo, "autor": autor, "ano": ano, "paginas": paginas}
                    livros.append(livro)
                except ValueError:
                    print(f"linha invalida no arquivo: {linha.strip()}")
    except Exception as e:
        print(f"erro ao carregar o arquivo: {e}")



while True:
    print("\n===Bem-vindo a Biblioteca Digital===")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Ordenar livros")
    print("4. Salvar livros")
    print("5. Carregar livros")
    print("0. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        lista_livros()
    elif opcao == "3":
        ordenar_livros()
    elif opcao == "4":
        salvar_livros()
    elif opcao == "5":
        carregar_livros()
    elif opcao == "0":
        print("Até logo! ")
        break