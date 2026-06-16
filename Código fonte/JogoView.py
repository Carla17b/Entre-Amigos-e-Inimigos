import ttkbootstrap as tb

#cria a classe principal
class App(tb.Window):
	#função de inicialização
	def __init__(self):
		#iniciando a janela
		super().__init__(title='Jogo Da Discordia')
		self.geometry('1024x576')
		
		#criando o primeiro frame
		frame_principal = tb.LabelFrame(self,text='Entre amigos e Inimigos')
		frame_principal.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)
		#cria uma lista que vai guardar os nomes das classes que vamos criar ainda, que no caso são as telas propriamente ditas
		self.frames = {}
		
		#Esse loop vai criar um frame em cima do outro
		for f in (TelaMenu,TelaJogo):
			frame = f(parent=frame_principal,controller=self)
			self.frames[f] = frame
			
			frame.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)
			
		self.mostrar_frame(TelaMenu)
	
	#função que puxa um frame pra frente    
	def mostrar_frame(self,nome_do_frame):
		frame = self.frames[nome_do_frame]
		frame.tkraise()
			
class TelaMenu(tb.Frame):
	#função de inicialização
	def __init__(self,parent,controller):
		super().__init__(parent)

		frame_menu = tb.LabelFrame(self,text='teste de framelabel')
		frame_menu.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.8)

		#criando as labels
		label_1 = tb.Label(frame_menu,text='Label em contrução')
		label_1.pack(pady=5)

		bt_1 = tb.Button(frame_menu,text='Botão em contrução',command = lambda:controller.mostrar_frame(TelaJogo))
		bt_1.pack(pady=5)
		
class TelaJogo(tb.Frame):
	#função de inicialização
	def __init__(self,parent,controller):
		super().__init__(parent)

		frame_jogo = tb.LabelFrame(self,text='teste de framelabel')
		frame_jogo.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.8)
		
		#criando as labels
		label_1 = tb.Label(frame_jogo,text='Label em contrução 2')
		label_1.pack(pady=5)
		
		bt_1 = tb.Button(frame_jogo,text='Botão em contrução 2',command = lambda:controller.mostrar_frame(TelaMenu))
		bt_1.pack(pady=5)
		
if __name__ == '__main__':
	app = App()
	
	app.mainloop()
