from pygame  import mixer # Load the required library
from tkinter.filedialog import askopenfilename
from tkinter import *

#Guard a file path : f = os.path.abspath('/home/cazevedo/Downloads/Omonoko_-_Empty_Streets.mp3')

musicas = []
TAM     = len(musicas)

class Reprodutor :
    def __init__ (self):
       pass

    def escolher ():
        selecionar = askopenfilename(initialdir="C:/Users/",
                           filetypes =(("Arquivo de audio", "*.mp3"),("All Files","*.*")),
                           title = "Selecione as musicas",
                           #multiple = True
                           )
        musicas.append(selecionar)


        for i in musicas:
            print(i, end=" ")
            print()
        print()


        return musicas

    def reproduzir ():
        mixer.init()

        for item in musicas:
            musica_atual = mixer.music.load(item)
            musica_atual = mixer.music.play()

    def parar ():
        musica_atual = mixer.music.stop()

    def pausar ():
        musica_atual = mixer.music.pause()

    def retomar ():
        musica_atual = mixer.music.unpause() #Continua da local pausado

#Próximo e Anterior com Modificações realizadas com base na resposta do Antony Gabriel
    def proxima ():
        for item in range(len(musicas)):

            item += 1
            musica_atual = mixer.music.load(musicas[item])  
            musica_atual = mixer.music.play() 

    def anterior ():
        for item in range(len(musicas)):
            item -= 1 
            musica_atual = mixer.music.load(musicas[item])
            musica_atual = mixer.music.play()


player = Reprodutor

janela =Tk()

janela.title("PYTHON PLAYER 🐍")

#Esta parte é que está com problemas
bt_escolher = Button(janela, width=20, text="ADICIONAR MUSICAS",  command=player.escolher)
bt_proxima  = Button(janela, width=10, text="PROXIMA",            command=player.proxima)
bt_anterior = Button(janela, width=10, text="ANTERIOR",           command=player.anterior)

bt_escolher.place (x=10,  y=50 )
bt_proxima.place  (x=170, y=50)
bt_anterior.place (x=270, y=50)



bt_play    = Button(janela, width=10, text="PLAY",    command=player.reproduzir)
bt_pause   = Button(janela, width=10, text="PAUSAR",  command=player.pausar)
bt_stop    = Button(janela, width=10, text="PARAR",   command=player.parar)
bt_return  = Button(janela, width=10, text="RETOMAR", command=player.retomar)

bt_play.place   (x=10,  y=0)
bt_pause.place  (x=110, y=0)
bt_stop.place   (x=210, y=0)
bt_return.place (x=310, y=0)

janela.geometry("410x80+450+350")
janela.mainloop()
