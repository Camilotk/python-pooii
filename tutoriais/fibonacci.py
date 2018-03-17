def soma_lista (*args):
    """recebe uma lista e retorna a soma dos elementos"""
    n = 0
    for i in args:
        n += i
    return n

def fibs(n):
    """retorna a seq. de fibonacci até o enésimo n"""
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[-1] + fib[-2])
    return fib


print(soma_lista(*fibs(int(input("Digite o valor de n : ")))))
