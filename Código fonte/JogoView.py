import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import JogoController as ct
import JogoModel as model
from PIL import Image

# Configuração global de aparência do CustomTkinter
ctk.set_appearance_mode("Light")  # Força o modo claro, já que o tema original é light
ctk.set_default_color_theme("blue")

# cria a classe principal
class App(ctk.CTk):
        # função de inicialização
    def __init__(self):
        # iniciando a janela
        super().__init__()
        self.title('Entre Amigos e Inimigos')
        self.geometry('1024x576')
        
        # Define a cor de fundo da janela principal (mesmo fundo roxo do tema antigo)
        self.configure(fg_color="#674c82")

        # criando o primeiro frame
        frame_principal = ctk.CTkFrame(self, fg_color="transparent") # Fundo transparente para ver o roxo da janela
        frame_principal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        # Labels usam text_color para a cor da fonte. Definido para branco para contrastar com o fundo
        label_1 = ctk.CTkLabel(self, text='ENTRE AMIGOS E INIMIGOS', font=('CinzelDecorate', 35, 'bold'), text_color="#ffffff")
        label_1.pack(pady=5)

        # cria uma lista que vai guardar os nomes das classes que vamos criar ainda
        self.frames = {}

        # Esse loop vai criar um frame em cima do outro
        for f in (TelaMenu, TelaJogo,TelaFim):
                frame = f(parent=frame_principal, controller=self)
                self.frames[f] = frame

                frame.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

        self.mostrar_frame(TelaMenu)

        # função que puxa um frame pra frente    
    def mostrar_frame(self, nome_do_frame):
        frame = self.frames[nome_do_frame]
        frame.tkraise()
                
class TelaMenu(ctk.CTkFrame):
        # função de inicialização
        def __init__(self, parent, controller):
            super().__init__(parent, fg_color="transparent") # Mantém transparente para herdar o fundo
            self.controller = controller
                     
        # Card central branco onde ficam as opções
            frame_menu = ctk.CTkFrame(self, fg_color='#ffffff', corner_radius=30)
            frame_menu.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

            # criando as labels (text_color adicionado para preto, já que o fundo do frame é branco)
            label_1 = ctk.CTkLabel(frame_menu, text='Quem serão os jogadores', font=('Cinzel', 30, 'bold'), text_color="#000000")
            label_1.place(relx=0.2, rely=0.2)

            label_2 = ctk.CTkLabel(frame_menu, text='De 2 a 15 jogadores', font=('Cinzel', 14, 'bold'), text_color="#343a40")
            label_2.place(relx=0.2, rely=0.3)
                
            # Container para a caixa de entrada e botão de adicionar
            frame_nomes = ctk.CTkFrame(frame_menu, fg_color='#fefefe', corner_radius=30, border_width=1, border_color="#bfbfbf")
            frame_nomes.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.12)

            # Caixa de entrada de texto arredondada
            self.entry_nomes = ctk.CTkEntry(
                    frame_nomes, 
                    font=('Cinzel', 14,'bold'), 
                    fg_color='#948d9c', 
                    text_color='#000000', 
                    placeholder_text="Nome do jogador...",
                    corner_radius=30,
                    border_width=0 # Deixa sem borda interna pois o frame externo já tem borda
            )
            self.entry_nomes.place(relx=0.01, rely=0.1, relwidth=0.68, relheight=0.8)

            label_rodadas = ctk.CTkLabel(frame_menu,
                                   text='Quantas rodadas?',
                                   font=('Cinzel', 14, 'bold'),
                                   text_color="#343a40"
                                   )
            label_rodadas.place(relx=0.2, rely=0.55,relheight=0.05)
            
            self.entry_rodadas = ctk.CTkEntry(
                     frame_menu,
                     font=('Cinzel', 14,'bold'),
                     fg_color='#948d9c',
                     text_color='#000000',
                     placeholder_text="Numero de rodadas",
                     corner_radius=30
                    )
            self.entry_rodadas.place(relx=0.2,rely=0.65,relwidth=0.3,relheight=0.1)
            
            # Botão "+ Adicionar" customizado com as cores do seu tema
            botao_add = ctk.CTkButton(
                    frame_nomes, 
                    text='+ Adicionar', 
                    font=('Cinzel', 12, 'bold'),
                    text_color='#000000',
                    fg_color='#948d9c', 
                    hover_color='#290b0b',
                    corner_radius=30,
                    command=self.clicar_adicionar
            )
            botao_add.place(relx=0.7, rely=0.1, relwidth=0.28, relheight=0.8)

            # Botão principal arredondado (estilo cápsula)
            botao_iniciar = ctk.CTkButton(
                    frame_menu, 
                    text='Iniciar o CAOS', 
                    font=('CinzelDecorate', 12, 'bold'),
                    corner_radius=30, 
                    fg_color='#948d9c', 
                    hover_color='#290b0b',
                    text_color='#000000',
                    command=self.clicar_iniciar
            )
            botao_iniciar.place(relx=0.55, rely=0.65,relwidth=0.2,relheight=0.1)

        def clicar_adicionar(self):

                nome = self.entry_nomes.get()
                
                resultado = ct.validar_jogador(nome)

                print(model.jogadores)
                
                if resultado['error']:
                    tk.messagebox.showwarning('erro',resultado['mensagem'])

                else:
                    #tk.messagebox.showinfo('secesso',resultado['mensagem'])

                    self.entry_nomes.delete(0,'end')
                    
        def clicar_iniciar(self):
                
                nmr_rodadas = self.entry_rodadas.get()
                
                resultado = ct.validar_numeros(nmr_rodadas)
               
                if resultado['error']:
                        tk.messagebox.showwarning('Atenção',resultado['mensagem'])
                else:
                        tela_jogo = self.controller.frames[TelaJogo]
            
                        # Inicializa a TelaJogo com o primeiro jogador e a primeira pergunta
                        tela_jogo.label_vez_jogador.configure(text=f"Vez de: {ct.jogador_atual()}")
                        tela_jogo.label_perguntas.configure(text=ct.sortear_pergunta())
                        
                        self.controller.mostrar_frame(TelaJogo)
                
class TelaJogo(ctk.CTkFrame):
        # função de inicialização
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        
        self.pergunta = ct.sortear_pergunta()
        
        self.jogadores = model.jogadores

        self.controller = controller
        
        # CTkFrame simulando o Labelframe (Cards modernos não usam texto cortando a borda)
        frame_jogo = ctk.CTkFrame(self,
                                  fg_color='#948d9c',
                                  corner_radius=15

                                  )
        frame_jogo.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # Título interno do painel
        #text='TESTE DE FRAMELABEL', font=('Cinzel', 12, 'bold'), text_color="#343a40"
        
        
        # criando as labels
        self.label_perguntas = ctk.CTkLabel(frame_jogo,
                                           text='',
                                           font=('Cinzel', 14, 'bold'),
                                           text_color="#000000",
                                           fg_color='#ffffff',
                                           corner_radius=30

                                           )
        self.label_perguntas.place(relx=0.02,rely=0.05,relwidth=0.96,relheight=0.7)
        self.label_perguntas.configure(text=self.pergunta)

        self.label_vez_jogador = ctk.CTkLabel(self.label_perguntas,
                                        text=f'È as vez de {ct.jogador_atual()}',
                                        font=('Cinzel', 14, 'bold'),
                                        text_color='#000000',
                                        fg_color='#ffffff',
                                        corner_radius=30
                                         )
        
        self.label_vez_jogador.place(relx=0.45,rely=0.1)
        
        self.ent_justificativa = ctk.CTkEntry(
                frame_jogo,
                font=('Cinzel', 14,'bold'), 
                fg_color='#ffffff', 
                text_color='#000000', 
                placeholder_text="Justifique...",
                corner_radius=30,
                border_width=0 

                )
        self.ent_justificativa.place(relx=0.55,rely=0.8,relwidth=0.4,relheight=0.05)

        self.ent_alvo = ctk.CTkEntry(
                frame_jogo,
                font=('Cinzel', 14,'bold'), 
                fg_color='#ffffff', 
                text_color='#000000', 
                placeholder_text="Quem...?",
                corner_radius=30,
                border_width=0 

                )
        self.ent_alvo.place(relx=0.05,rely=0.8,relwidth=0.4,relheight=0.05)

        # Botão para voltar à tela anterior também no padrão arredondado
        self.bt_justificar = ctk.CTkButton(
                frame_jogo, 
                text='Justificar Resposta', 
                font=('Cinzel', 12, 'bold'),
                fg_color='#382947', 
                hover_color='#290b0b',
                corner_radius=30,
                command=self.justificar
        )
        self.bt_justificar.place(relx=0.4,rely=0.9,relwidth=0.2,relheight=0.1)

    def justificar(self):

        #jogador = ct.jogador_atual()

        alvo = self.ent_alvo.get()
        
        justificativa = self.ent_justificativa.get()
        
        if alvo in list(model.jogadores.keys()):
                model.jogadores[alvo] += 1
                print(model.jogadores[alvo])
        else:
                
                return tk.messagebox.showwarning('atenção','Escolha um jogador válido')
        
        
        
        if justificativa.strip() == '':
                return tk.messagebox.showwarning('atenção','Justifique sua resposta')
        else:
                
                nova_pergunta = ct.proxima_pergunta()

                turno = ct.proximo_turno()
                
                if not turno['fim']:
                        novo_jogador = turno['jogador']

                        self.label_perguntas.configure(text=nova_pergunta)

                        self.label_vez_jogador.configure(text=f'È a vez do {novo_jogador}')

                        self.ent_justificativa.delete(0,'end')
                        self.ent_alvo.delete(0,'end')
                else:
                        tela_final = self.controller.frames[TelaFim]

                        tela_final.atualizar_resultado()
                        
                        self.controller.mostrar_frame(TelaFim)

                        self.ent_justificativa.delete(0,'end')
                        
class TelaFim(ctk.CTkFrame):
                        # função de inicialização
        def __init__(self, parent, controller):
                super().__init__(parent, fg_color="transparent")
                self.imagem = Image.open("dark_crown.png")
                
                self.controller = controller

                self.frame_fim = ctk.CTkFrame(self,
                                         fg_color='#eac43b',
                                         corner_radius = 15
                                         )
                self.frame_fim.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.7)

                self.img_vencedor = ctk.CTkImage(
                    light_image=self.imagem,
                    dark_image=self.imagem,
                    size=(128,128)
                    )

                self.icon_vencedor = ctk.CTkLabel(
                    self.frame_fim,
                    fg_color='#eac43b',
                    text='',
                    image=self.img_vencedor
                    )
                self.icon_vencedor.pack(pady=20)
                
                self.label_vencedor = ctk.CTkLabel(
                        self.frame_fim,
                        fg_color='#eac43b',
                        font=('Cinzel', 24,'bold')
                        )
                self.label_vencedor.pack(pady=40)


                self.label_descricao = ctk.CTkLabel(
                        self.frame_fim,
                        fg_color='#eac43b',
                        font=('Cinzel', 20,'bold')
                        )
                self.label_descricao.pack(pady=30)

                self.botao_reiniciar = ctk.CTkButton(
                        self.frame_fim,
                        text='Reiniciar',
                        fg_color='#948d9c',
                        text_color='#ffffff',
                        corner_radius = 30,
                        command=self.reiniciar_jogo
                        )
                self.botao_reiniciar.place(relx=0.4,rely=0.9,relwidth=0.2,relheight=0.1)
	
        def atualizar_resultado(self):

                resultado = ct.obter_vencedor()

                if resultado['sucesso']:
                        nome = resultado['jogador']
                        pontos = resultado['votos']
                        self.label_vencedor.configure(text=f'PARABÉNS {nome}')
                        self.label_descricao.configure(text=f'Você é a pessoa mais odiada do grupo com {pontos} votos')

                else:
                        self.label_vencedor.configure(text="Nenhum jogador foi registrado.")

        def reiniciar_jogo(self):

                model.jogadores.clear()
                model.rodada_atual = 1
                model.indice_jogador_atual = 0

                self.controller.mostrar_frame(TelaMenu)
                
if __name__ == '__main__':
	app = App()
	app.mainloop()
