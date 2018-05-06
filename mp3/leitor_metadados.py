import re

def limpa_bits(b):
    limpo = []
    for a in b:
        if a.isalpha():
            limpo.append(a)
    return ''.join(limpo)

def limpa_string(s):
    limpo = []
    ant = ''
    for l in s:
        if l == 'x' and ant == 'x':
            continue
        ant = l
        limpo.append(l)
    return ''.join(limpo)

def separa_titulo(t):
    regex = re.compile('(?!^)(?=[A-Z])', re.MULTILINE)
    resultado = re.sub(regex, " ", t)
    return resultado

with open("/arquivos/musicas/Omonoko_-_Empty_Streets.mp3", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    _a = str(data[-128:])
    _a = limpa_bits(_a)
    resto = limpa_string(_a[4:])
    _i = []
    _i = resto.split('x')
    nome_musica = separa_titulo(_i[0])
    nome_artista = separa_titulo(_i[1])
    nome_album = separa_titulo(_i[2])
