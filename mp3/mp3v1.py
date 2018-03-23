#!/home/cazevedo/.pypy/bin/pypy3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Camilo Cunha <Camilotk@gmail.com>
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

class Reprodutor:
    def __init__(self):
        pass

    def reproduz():
        mixer.init()
        for item in musicas:
            musica_atual = mixer.music.load(item)
            musica_atual = mixer.music.play()

    def pausa():
        musica_atual = mixer.music.pause()

    def para():
        musica_atual = mixer.music.stop()

    def retoma():
        musica_atual = mixer.music.unpause()
    
    def nova():
        selecionar = askopenfilename(initialdir="\\usr",
                           filetypes =(("Arquivo de audio", "*.mp3"),("All Files","*.*")),
                           title = "Selecione as musicas")
        musicas.append(selecionar)
        
    def grava():
        arquivo = open("bilbioteca.txt", "w", encoding="UTF-8")
        for e in agenda:
            arquivo.write("%s" % musica[0])
        arquivo.close()

    def proxima():
        for item in range(len(musicas)):
            item += 1
            musica_atual = mixer.music.load(musicas[item])  
            musica_atual = mixer.music.play()

    def anterior():
        for item in range(len(musicas)):
            item -= 1 
            musica_atual = mixer.music.load(musicas[item])
            musica_atual = mixer.music.play()
        
    def menu():
        janela = Tk()
        janela.title("PYTHON Reprodutor")

        bt_escolher = Button(janela, width=20, text="ADICIONAR MUSICAS", command=Reprodutor.nova)
        bt_proxima  = Button(janela, width=10, text="PROXIMA", command=Reprodutor.proxima)
        bt_anterior = Button(janela, width=10, text="ANTERIOR", command=Reprodutor.anterior)
        bt_play    = Button(janela, width=10, text="PLAY", command=Reprodutor.reproduz)
        bt_pause   = Button(janela, width=10, text="PAUSAR", command=Reprodutor.pausa)
        bt_stop    = Button(janela, width=10, text="PARAR", command=Reprodutor.para)
        bt_return  = Button(janela, width=10, text="RETOMAR", command=Reprodutor.retoma)
        
        bt_escolher.place (x=10,  y=50 )
        bt_proxima.place  (x=170, y=50)
        bt_anterior.place (x=270, y=50)
        bt_play.place   (x=10,  y=0)
        bt_pause.place  (x=110, y=0)
        bt_stop.place   (x=210, y=0)
        bt_return.place (x=310, y=0)
        
        janela.geometry("410x80+450+350")
        janela.mainloop()
        
Reprodutor.menu()
