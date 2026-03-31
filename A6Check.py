# Exercícios de Revisão - Corrija os Bugs
 
# =============================================
# Exercício 1 - Estoque de Produtos
# =============================================
# Enunciado: Corrija o código para adicionar um produto na lista apenas se ele ainda não existir.
# O programa deve mostrar o estoque atualizado após cada tentativa.
print('\n Exercicio 1: ')
estoque = ["Notebook", "Mouse", "Teclado"]

def adicionar_produto(lista, produto):
    if produto not in lista:
        lista.append(produto)
    print("Estoque atual:", lista)
 
adicionar_produto(estoque, "Monitor")
adicionar_produto(estoque, "Mouse")
print('\n')
# =============================================
# Exercício 2 - Cadastro de Alunos
# =============================================
# Enunciado: Corrija a função para adicionar ou atualizar a nota de um aluno.
# Se o aluno não existir no dicionário, ele deve ser criado.
print('\n Exercicio 2: ')
alunos = {"João": 8.5, "Maria": 9.0}
 
def atualizar_nota(nome, nota):
    if nome in alunos:
        alunos[nome] = nota
    else:
        alunos[nome] = nota
    print(f"Nota de {nome} atualizada para {nota}")
 
atualizar_nota("Pedro", 7.5)
atualizar_nota("João", 7.5)
print(alunos)

print('\n')
# =============================================
# Exercício 3 - Validação de Entrada com try/except
# =============================================
# Enunciado: Corrija a função para ler uma quantidade do usuário.
# Deve tratar erros de entrada e repetir até receber um número válido.
print('\n Exercicio 3')
def ler_quantidade():
    try:
        qtd = int(input("Quantidade: "))
        return qtd
    except ValueError:
        print("escreva apenas numeros")
        return 0
    except:
        print("Erro! Digite apenas números.")
        return 0
 
print("Quantidade válida:", ler_quantidade())
 
print('\n')
# =============================================
# Exercício 4 - Busca Sequencial
# =============================================
# Enunciado: Corrija a busca sequencial para retornar o índice do item ou -1 se não for encontrado.
print('\n Exercicio 4:')
estoque = ["Mouse", "Teclado", "Monitor", "Notebook"]
 
def busca_sequencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1
 
print("Índice do Monitor:", busca_sequencial(estoque, "Monitor"))
print("Índice do Celular:", busca_sequencial(estoque, "Celular"))
 
print('\n')
# =============================================
# Exercício 5 - Busca Binária
# =============================================
# Enunciado: Corrija a busca binária para funcionar corretamente com a lista ordenada de códigos.
print('\n Exercicio 5: ')
catalogo = [101, 205, 310, 450, 520]
precos = [50.0, 120.0, 80.0, 200.0, 150.0]
 
def busca_binaria(codigos, precos, codigo):
    baixo = 0
    alto = len(codigos) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if codigos[meio] == codigo:
            return precos[meio]
        elif codigos[meio] < codigo:
            baixo = meio + 1
        else:
            alto = meio - 1
    return "Produto não encontrado"
 
print("Preço do código 310:", busca_binaria(catalogo, precos, 310))
print('\n')
# =============================================
# Exercício 6 - Inventário com Dicionário
# =============================================
# Enunciado: Corrija a função para consultar um produto e mostrar quantidade e preço corretamente.
print('\n Exercicio 6: ')
inventario = {
    "Notebook": {"qtd": 10, "preco": 2500},
    "Mouse": {"qtd": 50, "preco": 80}
}
 
def consultar_produto(nome):
    if nome in inventario:
        dados = inventario.get(nome)
        print(f"{nome} - Estoque: {dados['qtd']} | Preço: R${dados['preco']}")
    else:
        print("Produto não encontrado")
 
consultar_produto("Mouse")
consultar_produto("Headset")

print('\n')
# =============================================
# Exercício 7 - Busca Sequencial com try/except
# =============================================
# Enunciado: Corrija a função para converter a matrícula e realizar a busca sequencial tratando erros.
print('\n Exerccicio 7: ')
alunos = [
    {"matricula": 1001, "nome": "Ana"},
    {"matricula": 1002, "nome": "Bruno"}
]
 
def buscar_por_matricula(mat):
    try:
        mat = int(mat)
    except ValueError:
        print("Matrícula deve ser número!")
        return
 
    for aluno in alunos:
        if aluno["matricula"] == mat:
            return aluno["nome"]
    return "Aluno não encontrado"
 
print(buscar_por_matricula("1001"))
print(buscar_por_matricula("abc"))
print('\n')
# =============================================
# Exercício 8 - Busca Binária com Ordenação
# =============================================
# Enunciado: Corrija a função para ordenar a lista antes de realizar a busca binária.
print('\n Exercicio 8: ') 
vendas = [150, 80, 220, 90, 300]
 
def busca_binaria_vendas(lista, valor):
    lista.sort()
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1
 
print("Índice do valor 220:", busca_binaria_vendas(vendas, 220))

print('\n')
# =============================================
# Exercício 9 - Relatório de Vendas com Dicionário
# =============================================
# Enunciado: Corrija o cálculo do total de vendas tratando possíveis erros de conversão.
print('\n Exercicio 9')
vendas_dia = {"Notebook": "2500", "Mouse": 80, "Teclado": "150"}
 
def total_vendas(vendas):
    total = 0
    for valor in vendas.values():
        try:
            total += float(valor)
        except:
            pass
    return total
 
print("Total de vendas:", total_vendas(vendas_dia))

print('\n')
# =============================================
# Exercício 10 - Estudo de Caso: Sistema de Controle de Estoque da TechZone
# =============================================
# Enunciado:
# A TechZone precisa de um sistema de estoque. O código abaixo contém vários bugs.
# Corrija todos os problemas para que o sistema funcione corretamente com as seguintes funcionalidades:
# - Cadastrar novo produto
# - Buscar produto (busca sequencial)
# - Atualizar quantidade em estoque
# - Encontrar o produto mais barato acima de um determinado preço (usando busca binária)
# - Gerar relatório completo do estoque
# Trate todos os erros de entrada do usuário de forma amigável.
print('\n Exercicio 10: ')
estoque = [
    {"nome": "Notebook Dell", "quantidade": 8, "preco": 2899.90},
    {"nome": "Mouse Logitech", "quantidade": 45, "preco": 89.90},
    {"nome": "Teclado Mecânico", "quantidade": 12, "preco": 249.90},
    {"nome": "Monitor 24''", "quantidade": 15, "preco": 899.90}
]
 
def cadastrar_produto():
    nome = input("Nome do produto: ")
    try:
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário: "))
    except:
        print("Erro: quantidade e preço devem ser números!")
        return
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    print(f"Produto {nome} cadastrado com sucesso!")
 
 
def buscar_produto(nome_busca):
    for produto in estoque:
        if produto["nome"] == nome_busca:
            return produto
    return None
 
 
def atualizar_quantidade(nome, quantidade_alterada):
    produto = buscar_produto(nome)
    if produto:
        produto["quantidade"] += quantidade_alterada
        print(f"Estoque atualizado! {nome} agora tem {produto['quantidade']} unidades.")
    else:
        print("Produto não encontrado!")
 
 
def produto_mais_barato_acima_de(preco_minimo):
    precos = []
    for p in estoque:
        precos.append(p["preco"])
    precos.sort()
    baixo = 0
    alto = len(precos) - 1
    resultado = None
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if precos[meio] >= preco_minimo:
            resultado = precos[meio]
            alto = meio - 1
        else:
            baixo = meio + 1
    if resultado is None:
        return "Nenhum produto encontrado acima desse preço."
    return f"Produto mais barato acima de R${preco_minimo}: {p["nome"]}"
 
 
def gerar_relatorio():
    if not estoque:
        print("Estoque vazio!")
        return
    total_estoque = 0
    print("\n--- Relatório de Estoque ---")
    for produto in estoque:
        valor_total = produto["quantidade"] * produto["preco"]
        total_estoque += valor_total
        print(f"{produto['nome']:20} | Qtd: {produto['quantidade']:3} | Preço: R${produto['preco']:.2f} | Total: R${valor_total:.2f}")
    print(f"\nValor total em estoque: R${total_estoque}")
 
 
def menu():
    while True:
        print("\n=== TechZone - Controle de Estoque ===")
        print("1. Cadastrar novo produto")
        print("2. Buscar produto")
        print("3. Atualizar quantidade")
        print("4. Produto mais barato acima de um preço")
        print("5. Gerar relatório completo")
        print("6. Sair")
 
        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue
 
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            nome = input("Digite o nome do produto: ")
            prod = buscar_produto(nome)
            if prod:
                print(f"Encontrado: {prod['nome']} - Qtd: {prod['quantidade']} - R${prod['preco']:.2f}")
            else:
                print("Produto não encontrado.")
        elif opcao == 3:
            nome = input("Nome do produto: ")
            try:
                qtd = int(input("Quantidade a adicionar/subtrair (use negativo para saída): "))
                atualizar_quantidade(nome, qtd)
            except:
                print("Quantidade inválida!")
        elif opcao == 4:
            try:
                preco = float(input("Preço mínimo: R$"))
                print(produto_mais_barato_acima_de(preco))
            except ValueError:
                print("Preço inválido!")
        elif opcao == 5:
            gerar_relatorio()
        elif opcao == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
 
# Para executar o Estudo de Caso, descomente a linha abaixo:
menu()
