# #ex.1
try:
    x = float(input("Digite o dividendo: "))
    y = float(input("Digite o divisor: "))
    resultado = x/y
    print(f"O resultado da divisao e: {resultado:.2f}")

except ValueError:
    print("Erro: digite um numero.")

except ZeroDivisionError:
    print("Zero não e divisor")


#ex.2
cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul':
(0, 0, 255)}
try:
    sua_cor = str(input("Digite uma das cores RGB: "))
    if sua_cor in cores:
        print(f"O valor do {sua_cor} e {cores[sua_cor]}")
except ValueError:
    print("Escreva uma cor das cores RGB")


#ex.3

try:
    numero = int(input("Digite um numero: "))
    if numero > 10:
        print("Numero maior que 10, numero valdio")
    else:
        print("Numero menor ou igual a 10")
except ValueError:
    print("Erro: Digite um numero.")
else:
    print("O programa foi executado com sucesso")
finally:
    print("Programa encerrado.")

#ex.4
class SenhaInvalidaError(Exception):
    pass
def check_senha(senha):
    if len(senha) < 8:
        raise ValueError("Deu erro aqui")
    if not any(char.isdigit() for char in senha):
        raise SenhaInvalidaError("deve conter pelo menos um numero")
    return True

try:
    senha = input("Digite sua senha: ")
    if check_senha(senha):
        print("senha valida")
except SenhaInvalidaError as e:
    print(f"erro: {e}")
    

#ex5
def transferencia():
    try:
        saldo = float(input("Digite o saldo da conta: "))
        valor = float(input("Digite o valor da transferencia: "))
        if valor > saldo:
            raise ValueError("Saldo insuficente.")
        saldo -= valor
        print(f"Transferencia realizada com sucesso! saldo atual: R$ {saldo:.2f}")   
    except ValueError as e:
        print(f"Erro: {e}")
    finally:
        print("operacao encerrada.") 
print(transferencia())