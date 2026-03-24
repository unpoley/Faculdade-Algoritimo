# ex:1
def soma(n):
    if n < 10:
        return n
    else:
        return (n % 10) + soma(n // 10)
    
print(soma(1234))
print(soma(5))
print(soma(123))

#ex:2
def cont(n):

    if n < 10:
        return 1
    else:
        return  1 + cont(n // 10)
        
    
print(cont(1234))
print(cont(5))
print(cont(123))

#ex:3
def inv(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + inv(s[:-1])

print(inv('amar'))
print(inv('arara'))
print(inv('abacaxi'))

# ex:4
def palindromo(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindromo(s[1:-1])

print(palindromo('amar'))
print(palindromo('arara'))
print(palindromo('abacaxi'))

#ex:5
def produto(a,b):
    if b == 0 :
        return 0 
    if b == 1:
        return a 
    return a + produto(a,b-1)

print(produto(30,0))
print(produto(0,20))
print(produto(6,10))

#ex:6
def maior(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        restante = maior(lista[1:])
        return lista[0] if lista[0] > restante else restante

print(maior([3,5,6,7]))
print(maior([1,10,9,3]))
print(maior([10,2,8,9]))

#ex:7
def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    return(a * b) // mdc(a, b)

print(mmc(16,8))
print(mmc(20,8))
print(maior(19, 21))