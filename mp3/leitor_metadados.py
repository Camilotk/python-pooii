import re

"""
Um leitor simples para a leitura de metadados MP3
"""

def limpa_bits(b):
    """
    Recebe uma variavel em bits e retorna
    em String sem o lixo da leitura
    """
    limpo = []
    for a in b:
        if a.isalpha():
            limpo.append(a)
    return ''.join(limpo)

def limpa_string(s):
    """
    Recebe uma String e retira as repetições de x 
    ocasionadas pela leitura de bits
    """
    limpo = []
    ant = ''
    for l in s:
        if l == 'x' and ant == 'x':
            continue
        ant = l
        limpo.append(l)
    return ''.join(limpo)

def separa_titulo(t):
    """
    Recebe uma String e adiciona um espaço entre o Camel Case
    """
    regex = re.compile('(?!^)(?=[A-Z])', re.MULTILINE)
    resultado = re.sub(regex, " ", t)
    return resultado

with open("/arquivos/musicas/Omonoko_-_Empty_Streets.mp3", "rb") as binary_file:
    """
    Le o arquivo em binario e retorna os metadados.

    variaveis:
    _a = bits lidos
    resto = bits limpos
    _i = informacoes lidas
    """
    data = binary_file.read()
    _a = str(data[-128:])
    _a = limpa_bits(_a)
    resto = limpa_string(_a[4:])
    _i = []
    _i = resto.split('x')
    nome_musica = separa_titulo(_i[0])
    nome_artista = separa_titulo(_i[1])
    nome_album = separa_titulo(_i[2])
