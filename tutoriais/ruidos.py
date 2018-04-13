# Dada uma lista não vazia de inteiros (X). Para esta tarefa, você deve retornar uma lista consistindo apenas de elementos 
# não únicos nesta lista. Para isso você, você deve remover todos os elementos exclusivos (que estão presentes na lista
# apenas uma vez). Ao resolver este problema, não altere a ordem original dos elementos da lista. Exemplo: [1, 2, 3, 1, 3] 
# em que 1 e 3 não são únicos e o resultado será [1, 3, 1, 3].

# Entrada: Uma lista (list) de inteiros (int).
# Output: A lista (list) de inteiros (int).

# Como é utilizado: Esta missão vai ajudar você a entender como manipular vetores, algo que é a base para a resolução de 
# tarefas mais complexas. O conceito pode ser facilmente generalizado para problemas do mundo real. Por exemplo: se você 
# precisa limpar estatísticas removendo elementos de baixa frequência (ruído)

def limpaRuido (args):
    r = []
    for arg in args:
        if args.count(arg) >= 2:
            r.append(arg)
    return r
