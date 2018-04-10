# Stefan e Sofia não se lembram da segurança e utilizam senhas simples para tudo.
# Ajude Nicolas desenvolver um modulo de verificação de segurança de senhas.
# A senha é considerada forte o suficiente se o seu comprimento for superior ou
# igual a 10 caracteres, contenha pelo menos um caractere numérico, uma letra
# maiúscula e uma letra minúscula. A senha contém apenas caracteres latinos ASCII
# ou dígitos.

# Entrada: Uma senha no formato de string.

# Saída: Segurança da senha na forma de um valor boleano (bool) ou qualquer tipo
# de dados que pode ser convertido e processado como um boleano. Nos resultados,
# você verá os resultados convertidos para verdadeiro ou falso (True ou False)

# Como é utilizado: Se você está preocupado com a segurança do seu aplicativo ou
# serviço, você pode verificar a complexidade das senhas de seus usuários.
# Você pode usar essas habilidades para exigir que seus usuários possuam senhas
# que satisfaçam os requisitos de senha (pontuações ou Unicode).

def verifica():
    """
    Retorna True se a senha for forte ou False caso contrário.

    Uma senha forte necessita de no mínimo 10 dígitos, um número, uma letra
    minúscula e uma letra mauiúscula.
    """
    s = input ("Digite sua senha: ")
    lg = False
    up = False
    lw = False
    nm = False
    if len(s) >= 10:
        lg = True
        for c in s:
            if c.isupper():
                up = True
            if c.islower():
                lw = True
            if c.isnumeric():
                nm = True
        if lg and up and lw and nm:
            return True
        else:
            return False
    return False

print (verifica())

# ---------------------------------------------------
#                   versão 2
# ---------------------------------------------------
def pass_check(pass_):
    """
    Retorna True se a senha for forte ou False caso contrário.

    Uma senha forte necessita de no mínimo 10 dígitos, um número, uma letra
    minúscula e uma letra mauiúscula.
    """
    # length is greater than or equal to 10 symbols
    greater = len(pass_) > 10
    has_upper = False
    has_lower = False
    has_num = False
    for s in pass_:
        if (s.isnumeric()):
            has_num = True
        elif(s.islower()):
            has_lower = True
        elif(s.isupper()):
            has_upper = True
        else:
            continue
    if has_upper and has_lower and has_num and greater:
        return True
    return False


