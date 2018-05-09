#!/home/cazevedo/.pypy/bin/pypy3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Camilo Cunha <Camilotk@gmail.com> e Renan <:email>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
A simple mp3 player
"""

from pygame  import mixer 
from tkinter.filedialog import askopenfilename
from tkinter import *

musicas = []
i = 0

class Reprodutor(object):
    def __init__(self):
        """
        Constructor method
        """
        pass
    
    def reproduz(self, i=0):
        """
        Initialize the player and plays all music
        in saved paths of array musicas
        """
        mixer.init()
        for item in musicas:
            mixer.music.load(item)
            mixer.music.play()
            i += 1
            print(i)

    def pausa(self):
        musica_atual = mixer.music.pause()

    def para(self):
        musica_atual = mixer.music.stop()

    def retoma(self):
        musica_atual = mixer.music.unpause()
    
    def nova(self):
        """
        Use the GUI function to take the path of a file
        and store in the variable selecionar, then 
        store all paths in array musicas
        """
        selecionar = askopenfilename(initialdir="\\usr",
                           filetypes =(("Arquivo de audio", "*.mp3"),("All Files","*.*")),
                           title = "Selecione as musicas")
        musicas.append(selecionar)
        
    def grava(self):
        arquivo = open("bilbioteca.txt", "w", encoding="UTF-8")
        for e in musicas:
            arquivo.write("%s \n" % e)
        arquivo.close()

    def proxima(self):
        Reprodutor.para(self)
        musica_atual = mixer.music.load(musicas[i])
        musica_atual = mixer.music.play()

    def anterior(self):
        for item in range(len(musicas)):
            item -= 1 
            musica_atual = mixer.music.load(musicas[item])
            musica_atual = mixer.music.play()
            
    def valida_faixa_inteiro(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))
               

    def imprime_menu():
        print("""
   1 - Adicionar Músicas
   2 - Play
   3 - Pausar
   4 - Parar
   5 - Retomar
   6 - Próxima
   7 - Anterior
   8 - Salvar a Playlist
   9 - Le a Playlist

   0 - Sai
    """)
        return Reprodutor.valida_faixa_inteiro("Escolha uma opção: ",0,9)
    
    def menu(self):
        while True:
         opção = Reprodutor.imprime_menu()
         if opção == 0:
             break
         elif opção == 1:
             Reprodutor.nova(self)
         elif opção == 2:
             Reprodutor.reproduz(self)
         elif opção == 3:
             Reprodutor.pausa(self)
         elif opção == 4:
             Reprodutor.para(self)
         elif opção == 5:
             Reprodutor.retoma(self)
         elif opção == 6:
             Reprodutor.proxima(self)
         elif opção == 7:
             Reprodutor.anterior(self)
         elif opção == 8:
             Reprodutor.grava(self)
         elif opção == 9:
             lê()
        
#intancia a Classe Reprodutor
player = Reprodutor()
#executa a funcao menu
player.menu()
