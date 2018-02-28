import pygame

'''
Cria uma tabela com 6 cores
'''

# Guarda as cores da tabela
cols = ['#0000ff','#0000aa','#000088','#000055','#000033', '#000011']

# Define as dimensões
w = 700
h = 500
y = h/6

# Cria a tela 
d = pygame.display.set_mode((w,h))

# Cria as colunas
for i, c in enumerate (cols):
    d.fill(pygame.Color(c), rect = (0, i*y, w, y*(i+1)))

# Atualiza a tela
pygame.display.flip()
# Salva a imagem criada
pygame.image.save(d, 'gradiente.png')
