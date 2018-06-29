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
import os
import eyed3
from pygame  import mixer
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk

def donothing():
    pass

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

    def cria_musica(self, caminho):
        """
        Passes the metatags to the current atributes of object
        """
        musica = eyed3.load(caminho)
        self.nome = musica.tag.title
        self.artista = musica.tag.artist
        self.album = musica.tag.album
        self.caminho = caminho

class Reprodutor(object):
    def __init__(self):
        """
        Constructor method
        """
        self.musicas = []
        self.caminhos = []
        mixer.init()

    def reproduz(self, i=0):
        """
        Initialize the player and plays all music
        in saved paths of array musicas
        """
        for item in self.musicas:
            mixer.music.load(item.caminho)
            mixer.music.play()
            i += 1

    def pausa(self):
        """
        Pauses the playing song
        """
        mixer.music.pause()

    def para(self):
        """
        Stops the playing song
        """
        mixer.music.stop()

    def retoma(self):
        """
        Returns the Stoped song where
        """
        mixer.music.unpause()

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
        self.musicas.append(musica)

    def grava(self, nome="biblioteca.txt"):
        """
        Saves the playlist in the OS
        """
        arquivo = open(nome, "w", encoding="UTF-8")
        for e in self.musicas:
            arquivo.write("%s" % e.caminho)
            arquivo.write('\n')
        arquivo.close()

    def le(self):
        """
        Reads the file in OS and mounts the Playlist
        """
        self.musicas.clear()
        path = askopenfilename(initialdir="\\usr",
                           filetypes =(("Arquivos de Texto", "*.txt"),("All Files","*.*")),
                           title = "Carregar a Playlist")
        arquivo = open (path, "r", encoding="UTF-8")
        for l in arquivo.readlines():
            musicaS = Musica()
            musicaS.cria_musica(l[0:-1])
            self.musicas.append(musicaS)
        arquivo.close()

    def ordena(self):
        """
        Sorts the list by music name
        """
        ordenado = sorted(self.musicas, key=lambda musica: musica.nome)
        self.musicas = ordenado[:]

    def proxima(self):
        """
        Plays the next song in vector
        """
        Reprodutor.para(self)
        musica_atual = mixer.music.load(self.musicas)
        musica_atual = mixer.music.play()

    def anterior(self):
        """
        Plays the foward song
        """
        for item in range(len(self.musicas)):
            item -= 1
            musica_atual = mixer.music.load(self.musicas[item])
            musica_atual = mixer.music.play()

    def limpa(self):
        """
        Cleans the playlist
        """
        self.musicas = []

class Interface(object):
    def __init__(self):
        """
        Creates the whole GUI on Global Method... ugly? I fucking know bro'
        just don't had time to make it more well designed.
        """
        self.player = Reprodutor()
        self.pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.play_imagem = os.path.join(os.getcwd(), 'arquivos/imagens/play.png')
        self.pausa_imagem = os.path.join(os.getcwd(), 'arquivos/imagens/pause.png')
        self.para_imagem = os.path.join(os.getcwd(), 'arquivos/imagens/stop.png')
        # ------------------------
        janela = Tk()
        janela.title("Reprodutor MP3")
        janela["bg"] = "darkgray"
        menubar = Menu(janela)
        # -------------------------
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Adicionar Música", command=self.atualiza)
        filemenu.add_separator()
        filemenu.add_command(label="Salvar Playlist", command=self.player.grava)
        filemenu.add_command(label="Carregar Playlist", command=self.carrega)
        filemenu.add_command(label="Limpar Playlist", command=self.apaga)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=janela.quit)
        # Arquivos
        menubar.add_cascade(label="Arquivos", menu=filemenu)
        # --------------------------
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Buscar...", command=self.procura)
        editmenu.add_command(label="Ordenar", command=self.botaordem)
        editmenu.add_separator()
        editmenu.add_command(label="Tocar", command=self.player.reproduz)
        editmenu.add_command(label="Pausar", command=self.player.pausa)
        editmenu.add_command(label="Retomar", command=self.player.retoma)
        editmenu.add_command(label="Parar", command=self.player.para)
        # Comandos
        menubar.add_cascade(label="Comandos", menu=editmenu)
        # --------------------------
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Licença", command=self.licenca)
        helpmenu.add_command(label="Sobre", command=self.sobre)
        # Ajuda
        menubar.add_cascade(label="Ajuda", menu=helpmenu)
        # -------------------------
        descricao = "Título:  %s\nArtista: %s\nAlbum: %s" % ("0", "0", "0")
        msgTela = Message(janela, text=descricao, width=300)
        #msg = tk.Message(master, text = whatever_you_do)
        #msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msgTela.place(x=5, y=5)
        self.play_imagem = PhotoImage(file=self.play_imagem)
        self.pausa_imagem = PhotoImage(file=self.pausa_imagem)
        self.para_imagem = PhotoImage(file=self.para_imagem)
        btnPlay = Button(janela, text="Play", command=self.player.reproduz)
        btnPlay.config(width=55, image=self.play_imagem, compound=LEFT)
        btnPlay.place(x=5, y=60)
        btnPause = Button(janela, text="Pause", command=self.player.pausa)
        btnPause.config(width=65,image=self.pausa_imagem, compound=LEFT)
        btnPause.place(x=90, y=60)
        btnStop = Button(janela, text="Stop", command=self.player.para)
        btnStop.config(width=55, image=self.para_imagem, compound=LEFT)
        btnStop.place(x=185, y=60)
        # -------------------------
        self.tree = ttk.Treeview(janela, columns=('Album', 'Artista    '))
        self.tree.heading('#0', text='Nome')
        self.tree.heading('#1', text='Album')
        self.tree.heading('#2', text='Artista')
        self.tree.column('#1', stretch=YES)
        self.tree.column('#2', stretch=YES)
        self.tree.column('#0', stretch=YES)
        self.tree.place(x=5, y=120)

        janela.configure(menu=menubar)
        janela.geometry("612x350")
        janela.mainloop()

    def atualiza(self):
        """
        Add and displays a new music
        """
        self.player.nova()
        for i in self.tree.get_children():
                self.tree.delete(i)
        for musica in self.player.musicas:
            self.tree.insert('', 'end', text=musica.nome, values=(musica.album, musica.artista))

    def apaga(self):
        """
        Cleans the playlist
        """
        self.player.limpa()
        for i in self.tree.get_children():
            self.tree.delete(i)

    def carrega(self):
        """
        Reads a playlist and display
        """
        self.player.le()
        for i in self.tree.get_children():
                self.tree.delete(i)
        for musica in self.player.musicas:
            self.tree.insert('', 'end', text=musica.nome, values=(musica.album, musica.artista))

    def procura(self):
        """
        GUI for searching
        """
        # ----------
        janela2 = Tk()
        janela2.title("Procurar música...")
        L1 = Label(janela2, text="Nome: ")
        self.E1 = Entry(janela2, width=30)
        B1 = Button(janela2, text="Pesquisar", command=self.encontra)
        B1.config(width=8, compound=LEFT)
        B2 = Button(janela2, text="Sair", command=janela2.destroy)
        B2.config(width=6, compound=LEFT)
        L1.place(x=5, y=0)
        self.E1.place(x=50, y=0)
        B1.place(x=5, y=25)
        B2.place(x=100, y=25)
        janela2.geometry("300x60")
        janela2.mainloop()

    def encontra(self):
        """
        GUI with found results
        """
        chave = self.E1.get()
        encontrado = False
        encontrados = []
        nomes = ""
        janela3 = Tk()
        for p,e in enumerate(self.player.musicas):
            if chave in e.nome:
                encontrado = True
                encontrados.append(e)
                nomes += e.nome + "\n"
        if not encontrado:
            nomes = "404! Música não encontrada!"
        L2 = Label(janela3, text=nomes)
        L2.place(x=0,y=0)
        janela3.geometry("200x300")
        janela3.mainloop()

    def botaordem(self):
        """
        Sort the playlist and displays it
        """
        self.player.ordena()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for musica in self.player.musicas:
            self.tree.insert('', 'end', text=musica.nome, values=(musica.album, musica.artista))

    def licenca(self):
        lic = """
        Copyright 2018 Camilo Cunha de Azevedo

        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at

            http://www.apache.org/licenses/LICENSE-2.0

        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.
        """
        janela4 = Tk()
        janela4.title("Licença Apache 2.0")
        L6 = Label (janela4, text=lic)
        L6.place(x=0, y=0)
        janela4.geometry("600x220")
        janela4.mainloop()

    def sobre(self):
        s = "IFRS \n Aluno: Camilo Cunha de Azevedo \n Disciplina: POO II \n Prof: Jean da Rolt \n Semestre: 2018/01"
        janela5 = Tk()
        janela5.title("Trabalho da Faculdade")
        L7 = Label(janela5, text=s)
        L7.place(x=0, y=0)
        janela5.geometry("220x100")
        janela5.mainloop()

r = Interface()

