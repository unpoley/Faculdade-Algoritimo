#1.1
print("================================================\n            Atividade 1.01\n================================================")
listaf = [ "maçã", "banana", "laranja"]
print(listaf)

#1.2
print("================================================\n            Atividade 1.02\n================================================")
listaf.append("uva")
listaf.pop(1)
print(listaf)

#1.3
print("================================================\n            Atividade 1.03\n================================================")
listan = []

for i in range(1,11):
    listan.append(i)
print(len(listan))
print(listan)
#1.4
print("================================================\n            Atividade 1.04\n================================================")
if 7 in listan:
    print("sim")
else:
    print("nao")

#1.5
print("================================================\n            Atividade 1.05\n================================================")
print(listan[:3])

#1.6
print("================================================\n            Atividade 1.06\n================================================")
notas = [8.5, 7.0, 9.5, 6.0]
notas.sort()
print(notas)

#1.7
print("================================================\n            Atividade 1.07\n================================================")
if 5 in listan:
    conta5 = listan.count(5)
    print(conta5)
else:
    print("nao")

#1.8
print("================================================\n            Atividade 1.08\n================================================")
listanI = listan[::-1]
print(listanI)

#1.9
print("================================================\n            Atividade 1.09\n================================================")
listaq = [i**2 for i in range(1,9)]
print(listaq)

#1.10
print("================================================\n            Atividade 1.10\n================================================")
palavras = ["python", "lista", "exercicio", "legal"]
listap5 = []
n = 0
for n in range(len(palavras)):
    if len(palavras[n]) >= 5:
        listap5.append(palavras[n])
    n = n+1
print(listap5)

#1.11
print("================================================\n            Atividade 1.11\n================================================")
a = [1, 2, 3] 
b = [4, 5, 6]
a.extend(b)
print(a)

#1.12
print("================================================\n            Atividade 1.12\n================================================")
lista12 = [1, 2, 2, 3, 4, 4, 5]
lista12u = list(set(lista12))
print(lista12u)

#1.13
print("================================================\n            Atividade 1.13\n================================================")
lista13 = []
for i in range(1,11):
    lista13.append(i)
print(lista13)
maior = max(lista13)
menor = min(lista13)
print(maior)
print(menor)

#1.14
print("================================================\n            Atividade 1.14\n================================================")
lista14 = [
    [1,2,3,4],
    [5,6,7,8]
]
print(lista14[0][1])

#1.15
print("================================================\n            Atividade 1.15\n================================================")
import copy 
matriz = [
    [1,2],
    [3,4]
]
matrizz = copy.deepcopy(matriz)
matrizz[0].pop(1)
matrizz[0].append(5)
print(matrizz)
print(matriz)

#1.16
print("================================================\n            Atividade 1.16\n================================================")
lista16 = [i for i in range(21) if i % 2 ==0]
print(lista16)

#2.1
print("================================================\n            Atividade 2.1\n================================================")
livro = {
    "nome": "joao",
    "idade": 18,
    "nota": 9.5,
}
print(livro["idade"])

#2.2
print("================================================\n            Atividade 2.2\n================================================")
livro.update(cidade = "Sao paulo")
print(livro)

#2.3
print("================================================\n            Atividade 2.3\n================================================")
for x,y in livro.items():
    print(f"{x}:{y}")


#3
print("================================================\n            Atividade 3\n================================================")

def show_menu():
    print("1. Adicionar tarefa\n2. Listar todas as tarefas\n3. Marcar tarefa como concluída\n4. Remover tarefa\n5. Sair")
def add_tarefa(tarefas):
    qual_tarefa = input("Qual tarefa quer fazer: ")
    tarefas.append({"nome": qual_tarefa, "feito": False})
    print(f"tarefa adcionada: {qual_tarefa}")
def list_tarefa(tarefas):
    if not tarefas:
        print("Sem tarefas.")
    else:
        for i, p in enumerate(tarefas, 1):
            status = "feito" if p["feito"] else " "
            print(f"{i}. {p['nome']} - {status}")
def mark_tarefa(tarefas):
    list_tarefa(tarefas)
    if tarefas:
        try:
            numb_tarefa = int(input("Digite o numero da tarefa que quer marcar: "))
            if 1 <= numb_tarefa <= len(tarefas):
                tarefas[numb_tarefa - 1]['feito'] = True
                print(f"Tarefa: {tarefas[numb_tarefa - 1]['nome']} foi marcada como concluida")
            else:
                print("numero invalido.")
        except ValueError:
            print("Entre um numero valido")
def remove_tarefa(tarefas):
    list_tarefa(tarefas)
    if tarefas:
        try:
            numb_tarefa = int(input("Digite o numero da tarefa que quer remover: ")) 
            if 1 <= numb_tarefa <= len(tarefas):
                tarefa_remove = tarefas.pop(numb_tarefa - 1)
                print(f"Tarefa  foi removida")
            else:
                print("Numero invalido")
        except ValueError:
            print("Entre um numero valido")
def main():

    tarefas = []
    while True:
        show_menu()
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            print("Você escolheu 1. Adicionar tarefa")
            add_tarefa(tarefas)
        elif escolha == 2:
            print("Você escolheu 2. Listar todas as tarefas")
            list_tarefa(tarefas)
        elif escolha == 3:
            print("Você escolheu 3. Marcar tarefa como concluída")
            mark_tarefa(tarefas) 
        elif escolha == 4:
            print("Você escolheu 4. Remover tarefa")
            remove_tarefa(tarefas)
        elif escolha == 5:
            print("Você escolheu 5. Sair")
            print("Tchau. \nDesligando......")
            break
        else:
            print("escolha invalida. tente denovo")
main()
