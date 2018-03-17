fib = lambda n, x=0, y=1 : x if not n else fib(n-1, y, x+y)
n = int( input("Digite o valor de n: ") )
print (" = %s" % sum ([fib(i) for i in range (n)]))
