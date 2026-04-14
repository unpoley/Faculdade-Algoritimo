import os

alunos = []

def ad_aluno():
    nome = input("Digite o nome do aluno: ")
    notas = []

    while True:
        try:
            qtd_notas = int(input("Quantas notas deseja inserir(minimo 2 e maximo 5):  "))
            if qtd_notas < 2 or qtd_notas > 5:
                print("Quantidade invalida. Digite entre 2 e 5 notas. ")
                continue
            break
        except ValueError:
            print("Digite um numero valido. ") 
    for i in range(qtd_notas):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota invalida. Digite um numero enre 0 e 10. ")
            except ValueError:
                print("Entrada invalida. Digite um numero. ")
    media = sum(notas)/len(notas)
    aluno = {"nome": nome, "notas": notas, "media": media}
    alunos.append(aluno)
    for a in alunos:
        print(f"o aluno: {a["nome"]} foi adicionado")
def ordenar_alunos():
    alunos.sort(key=lambda x: x["media"], reverse=True)
def salvar_arquivo():
    try:
        if os.path.exists("alunos.txt"):
            escolha = input("O arquivo ja existe. Deseja sobreescrever? (sim/nao): ")
            if escolha.lower() != "sim":
                print("Operaçao cancelada.")
                return
            with open("alunos.txt", "w") as arquivo:
                for aluno in alunos:
                    arquivo.write(f"{aluno["nome"]},{aluno["media"]:.2f}\n")
            print("Dados salvos em alunos.txt")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


while True:
    print("\n===Bem-vindo ao Sistema de Gestao de Estoque===")
    print("1. Adicionar alunos")
    print("2. Ordenar alunos")
    print("3. Salvar arquivo")
    print("0. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        ad_aluno()
    elif opcao == "2":
        ordenar_alunos()
    elif opcao == "3":
        salvar_arquivo()
    elif opcao == "0":
        print("Até logo! ")
        break
            
            

