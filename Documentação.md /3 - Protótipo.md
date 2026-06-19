# Protótipo

O protótipo do "Jogo da Discórdia" agora apresenta uma Interface Gráfica de Usuário (GUI) desenvolvida com customtkinter, proporcionando uma experiência visualmente mais rica e interativa em comparação com a versão de linha de comando. A GUI é dividida em telas (Frames) para gerenciar o fluxo do jogo: uma tela de menu para configuração, uma tela de jogo para as rodadas de votação e uma tela final para exibir os resultados.

Estrutura da GUI (Telas)

Tela de Menu (TelaMenu)

Esta é a tela inicial onde os jogadores são configurados e o jogo é iniciado.

•
Título: "Quem serão os jogadores" e "De 2 a 15 jogadores".

•
Campo de Entrada de Nome: Um campo de texto (CTkEntry) para digitar o nome de cada jogador.

•
Botão "+ Adicionar": Adiciona o nome digitado à lista de jogadores. Exibe mensagens de erro (tk.messagebox.showwarning) se o nome for inválido.

•
Campo de Entrada de Rodadas: Um campo de texto (CTkEntry) para definir o número de rodadas.

•
Botão "Iniciar o CAOS": Inicia o jogo, validando o número de jogadores e rodadas. Em caso de sucesso, transiciona para a TelaJogo.

Tela de Jogo (TelaJogo)

Esta tela gerencia o fluxo das rodadas de votação.

•
Área de Pergunta: Um CTkLabel grande que exibe a pergunta atual da discórdia.

•
Indicador de Rodada: Um CTkLabel dentro da área de pergunta que mostra a rodada atual (e.g., "Estamos na rodada 1").

•
Indicador de Jogador: Um CTkLabel que informa de quem é a vez de votar (e.g., "É a vez de [Nome do Jogador]").

•
Campo "Quem...?": Um CTkEntry para o jogador digitar o nome do alvo do voto.

•
Campo "Justifique...": Um CTkEntry para o jogador inserir a justificativa do voto.

•
Botão "Justificar Resposta": Processa o voto e a justificativa. Valida as entradas e, se válidas, atualiza a pontuação, avança para o próximo turno/jogador e atualiza a pergunta. Se o jogo terminar, transiciona para a TelaFim.

Tela Final (TelaFim)

Esta tela exibe o resultado final do jogo.

•
Coroa (Imagem): Uma imagem de coroa (dark_crown.png) exibida no topo, simbolizando o "vencedor" (o mais votado).

•
Label do Vencedor: Um CTkLabel que parabeniza o jogador mais votado (e.g., "PARABÉNS [Nome do Vencedor]").

•
Descrição do Resultado: Um CTkLabel que informa a pontuação do vencedor (e.g., "Você é a pessoa mais odiada do grupo com [X] votos").

•
Botão "Reiniciar": Permite reiniciar o jogo, retornando à TelaMenu e resetando o estado do jogo.

Cores e Estilo

•
Modo de Aparência: Light (claro).

•
Tema de Cores: blue (padrão do customtkinter).

•
Cor de Fundo Principal: Roxo (#674c82).

•
Elementos de UI: Utilizam cantos arredondados (corner_radius=30) para um visual moderno e suave. Cores como #948d9c (cinza/roxo) e #ffffff (branco) são usadas para botões e fundos de campos de entrada, com texto em preto (#000000) para contraste

# TelaMenu
<img width="1031" height="617" alt="image" src="https://github.com/user-attachments/assets/40892685-919a-47e1-b3c5-6c1a8edde6c7" />

# TelaJogo
<img width="1031" height="618" alt="image" src="https://github.com/user-attachments/assets/9a85c2ca-dff3-4934-bfb1-ed22e66f92e6" />

# TelaFim
<img width="1029" height="613" alt="image" src="https://github.com/user-attachments/assets/43704dc2-fa20-476c-8efa-0bd07e79019c" />



