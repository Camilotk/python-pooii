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
import re
import os

musicas = []
caminhos = []
i = 0
class Musica(object):
    def __init__(self):
        """
        Initialize the class with the necessary values about a song
        Variables:
        nome = name of the song
        artista = name of artist
        album = name of the album
        caminho = path where the mp3 is alocated
        """
        self.nome = "Desconhecido"
        self.artista = "Desconhecido"
        self.album = "Desconhecido"
        self.caminho = ""

    def limpa_bits(self, b):
        """
        Recieves one variable in bits and returns
        in one String without the reading garbage
        """
        limpo = []
        for a in b:
            if a.isalpha():
                limpo.append(a)
        return ''.join(limpo)

    def limpa_string(self, s):
        """
        Recives one String and removes all repeted \'x\'
        that are stored because the bits reading
        """
        limpo = []
        ant = ''
        for l in s:
            if l == 'x' and ant == 'x':
                continue
            ant = l
            limpo.append(l)
        return ''.join(limpo)

    def separa_titulo(self, t):
        """
        Recieves one String and alocates one blank space between the Camel Case
        """
        regex = re.compile('(?!^)(?=[A-Z])', re.MULTILINE)
        resultado = re.sub(regex, " ", t)
        return resultado

    def imprime_metadados(self):
        """
        Prints songs informations
        """
        print("Nome: %s" % Musica.nome)
        print("Artista: %s" % Musica.artista)
        print("Album: %s" % Musica.album)

    def cria_musica(self, caminho):
        with open(caminho, "rb") as binary_file:
            """
            Reads the file in binary data and returns it's metadata
            variables:
            _a = readed bits
            resto = cleaned bits
            _i = readed information
            """
            self.caminho = caminho
            # Read the whole file at once
            data = binary_file.read()
            _a = str(data[-128:])
            _a = Musica.limpa_bits(self, _a)
            resto = Musica.limpa_string(self, _a[4:])
            _i = []
            _i = resto.split('x')
            self.nome = Musica.separa_titulo(self, _i[0])
            self.artista = Musica.separa_titulo(self, _i[1])
            self.album = Musica.separa_titulo(self, _i[2])

class Reprodutor(object):
    def __init__(self):
        """
        Constructor method
        """
        mixer.init()

    def reproduz(self, i=0):
        """
        Initialize the player and plays all music
        in saved paths of array musicas
        """
        for item in musicas:
            mixer.music.load(item.caminho)
            mixer.music.play()
            i += 1

    def pausa(self):
        """
        Pauses the playing song
        """
        musica_atual = mixer.music.pause()

    def para(self):
        """
        Stops the playing song
        """
        musica_atual = mixer.music.stop()

    def retoma(self):
        """
        Returns the Stoped song where
        """
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
        musica = Musica()
        musica.cria_musica(selecionar)
        musicas.append(musica)

    def grava(self, nome="biblioteca.txt"):
        """
        Saves the playlist in the OS
        """
        arquivo = open(nome, "w", encoding="UTF-8")
        for e in musicas:
            arquivo.write("%s" % e.caminho)
            arquivo.write('\n')
        arquivo.close()

    def le(self):
        """
        Reads the file in OS and mounts the Playlist
        """
        path = askopenfilename(initialdir="\\usr",
                           filetypes =(("Arquivos de Texto", "*.txt"),("All Files","*.*")),
                           title = "Carregar a Playlist")
        arquivo = open (path, "r", encoding="UTF-8")
        for l in arquivo.readlines():
            musicaS = Musica()
            musicaS.cria_musica(l[0:-1])
            musicas.append(musicaS)
        arquivo.close()

    def pesquisa(self):
        """
        Searchs for a song name and ask for play it
        """
        chave = input("Pesquisar por : ")
        encontrados = []
        play = False
        for p,e in enumerate(musicas):
            if chave in e.nome:
                play = True
                encontrados.append(e)
        if play:
            for p,e in enumerate(encontrados):
                print("Encontradas: ")
                print(str(p) + " - " + e.nome)
            chave = int(Reprodutor.valida_faixa_inteiro("Qual deseja tocar? [digite o n]", 0, len(encontrados)))
            mixer.music.load(encontrados[chave].caminho)
            mixer.music.play()
        else:
            print("Música não encontrada")

    def proxima(self):
        """
        Plays the next song in vector
        """
        Reprodutor.para(self)
        musica_atual = mixer.music.load(musicas)
        musica_atual = mixer.music.play()

    def anterior(self):
        """
        Plays the foward song
        """
        for item in range(len(musicas)):
            item -= 1
            musica_atual = mixer.music.load(musicas[item])
            musica_atual = mixer.music.play()

    def valida_faixa_inteiro(pergunta, inicio, fim):
        """
        Validates the entries in Program
        """
        while True:
            try:
                valor = int(input(pergunta))
                if inicio <= valor <= fim:
                    return(valor)
            except ValueError:
                print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

    def imprime_menu():
        """
        Shows the options and asks for an entry
        """
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
   10 - Pesquisa
   0 - Sai
    """)
        return Reprodutor.valida_faixa_inteiro("Escolha uma opção: ",0,10)

    def menu(self):
        """
        Executes the entries in loop until the User asks to exit
        """
        while True:
         opcao = Reprodutor.imprime_menu()
         if opcao == 0:
             break
         elif opcao == 1:
             Reprodutor.nova(self)
         elif opcao == 2:
             Reprodutor.reproduz(self)
         elif opcao == 3:
             Reprodutor.pausa(self)
         elif opcao == 4:
             Reprodutor.para(self)
         elif opcao == 5:
             Reprodutor.retoma(self)
         elif opcao == 6:
             Reprodutor.proxima(self)
         elif opcao == 7:
             Reprodutor.anterior(self)
         elif opcao == 8:
             Reprodutor.grava(self)
         elif opcao == 9:
             Reprodutor.le(self)
         elif opcao == 10:
             Reprodutor.pesquisa(self)

#intancia a Classe Reprodutor
player = Reprodutor()
#executa a funcao menu
player.menu()
