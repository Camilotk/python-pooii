# Dado um texto que contém várias letras em inglês e sinais de pontuação.
# Você deve encontrar a letra mais frequente no texto. A letra retornada deve
# ser uma letra minúscula.Ao procurar a letra mais frequente, diferenças entre
# maiúsculas e minusculas não importam, de modo que para a busca assuma que
# "A" == "a". Certifique-se de não considerar pontuação, números e espaços
# em branco na busca, apenas letras.

# Se o texto possui duas ou mais letras com a mesma frequência, então o resultado
# será a letra que vem primeiro no alfabeto latino. Por exemplo -- "one" contém
# "o", "n", "e" apenas uma vez para cada um, de modo que nós escolhemos "e".

# Entrada: Um texto para análise no formato de string.

# Saída: A letra mais frequente em letra minúscula no formato de string.

# Como é utilizado: Para a maioria das tarefas de decriptografia, você precisa
# saber a frequência de ocorrência de várias letras em uma seção de texto. 
# Por exemplo: podemos facilmente quebrar um algoritmo de criptografia simples
# de adição ou substituição se soubermos a frequência em que as letras aparecem.
# Também pode ser informação útil para linguistas!

def procura_letra(texto):
    texto = texto.lower()
    letras = []
    c = ' '
    for t in texto:
        if t.isalpha():
            if ((t, texto.count(t))) not in letras:
                letras.append((t, texto.count(t)))
    letras.sort(key=lambda x: x[0])
    letras.reverse()
    maior = max(map(lambda y: y[1], letras))
    retorno = min(filter(lambda y: y[1] == maior, letras))
    return retorno[0]
    
print(procura_letra("How do you do?"))

# ------------------------------------------------------
#                   VERSÃO 2
# ------------------------------------------------------

def procura_letraS(texto):
    texto = texto.lower()
    chars = []
    maior = [0, 'a']
    for letra in texto:
      if texto.count(letra) > maior[0] and letra.isalpha():
        maior[0] = texto.count(letra)
        maior[1] = letra
      elif texto.count(letra) == maior[0] and letra.isalpha():
        if maior[1] > letra:
          maior[1] = letra
      else:
        pass
    return maior[1]
# -------------------------------------------------------
#                solution
# -------------------------------------------------------

import string
def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


