from tkinter import *
#Button
#Progressbar -> fim da música
#Scale -> volume
#Treeview -> lista de músicas
# Menu -> Submenu (nome) -> Command (func) -> Separator
def donothing():
    pass

class Interface(object):
    def __init__(self):
        janela = Tk()
        janela.title("Reprodutor MP3")
        janela["bg"] = "darkgray"
        menubar = Menu(janela)
        # -------------------------
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Adicionar Música", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Salvar Playlist", command=donothing)
        filemenu.add_command(label="Carregar Playlist", command=donothing)
        filemenu.add_command(label="Limpar Playlist", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=janela.quit)
        # Arquivos
        menubar.add_cascade(label="Arquivos", menu=filemenu)
        # --------------------------
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Buscar...", command=donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Tocar", command=donothing)
        editmenu.add_command(label="Pausar", command=donothing)
        editmenu.add_command(label="Retomar", command=donothing)
        editmenu.add_command(label="Parar", command=donothing)
        # Comandos
        menubar.add_cascade(label="Comandos", menu=editmenu)
        # --------------------------
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Licença", command=donothing)
        helpmenu.add_command(label="Sobre", command=donothing)
        # Ajuda
        menubar.add_cascade(label="Ajuda", menu=helpmenu)
        # -------------------------
        descricao = "Título:  %s\nArtista: %s\nAlbum: %s" % ("Desconhecido", "Desconhecido", "Desconhecido")
        msgTela = Message(janela, text=descricao, width=300)
        #msg = tk.Message(master, text = whatever_you_do)
        #msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msgTela.place(x=5, y=5)
        btnPlay = Button(janela, width=5, text="Play")
        btnPlay.place(x=5, y=60)
        btnStop = Button(janela, width=5, text="Stop")
        btnStop.place(x=75, y=60)
        # -------------------------
        janela.configure(menu=menubar)
        janela.geometry("450x350")
        janela.mainloop()

r = Interface()

