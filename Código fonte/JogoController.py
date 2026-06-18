import JogoModel as model
import random as rd

def validar_jogador(nome):

    if nome.strip() == '':
        return {'error':True,'mensagem':'Insira o nome de um jogador'}

    model.jogadores[nome] = 0
    return {'error':False,'mensagem':'Jogador adicionado'}

def validar_numeros(rodadas):

    if len(model.jogadores) < 2:
        return{'error':True,'mensagem':'são necessários pelo menos 2 jogadores'}

    elif (rodadas == 0) or not rodadas.isdigit():
        return{'error':True,'mensagem':'Insira um NUMERO de rodadas valido'}
    else:
        model.nmr_rodadas = rodadas
        
    return {'error':False,'mensagem':'O jogo já vai começar...'}

def sortear_pergunta():
    pergunta = rd.choice(model.perguntas)
    
    return pergunta

def proxima_pergunta():
    nova_pergunta = rd.choice(model.perguntas)

    return nova_pergunta

def jogador_atual():
    lista_nomes = list(model.jogadores.keys())

    if model.indice_jogador_atual < len(lista_nomes):
        return lista_nomes[model.indice_jogador_atual]
    return 'nenhum jogador'

def proximo_turno():
    lista_nomes = list(model.jogadores.keys())
    nmr_max_jogadores = len(lista_nomes)
    proximo_jogador = ''
    model.indice_jogador_atual += 1

    if model.indice_jogador_atual >= nmr_max_jogadores:
        model.indice_jogador_atual = 0
        model.rodada_atual += 1

    if model.rodada_atual > int(model.nmr_rodadas):
        return{'fim':True,'mensagem':'O jogo acabou'}

    nova_pergunta = rd.choice(model.perguntas)

    proximo_jogador = lista_nomes[model.indice_jogador_atual]
    
    return {
        "fim": False,
        "pergunta": nova_pergunta,
        "jogador": proximo_jogador,
        "rodada": model.rodada_atual
    }
def obter_vencedor():

    if not model.jogadores:
        return {'sucesso':False,'mensagem':'Nenhum jogador encontrado'}

    mais_votado = max(model.jogadores, key=model.jogadores.get)
    votos = model.jogadores[mais_votado]

    return {'sucesso':True,'jogador':mais_votado,'votos':votos}
    
    
