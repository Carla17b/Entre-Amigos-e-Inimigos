rodada_atual = 1

indice_jogador_atual = 0

jogadores = {}

rodadas = 0

perguntas = [
        "Quem do grupo você considera mais falso? ", "Quem você menos confiariaria para guardar um segredo ",
        "Se tivesse que excluir uma pessoa do grupo, quem seria? ",
        "Quem mais se acha melhor do que realmente é? ",
        "Quem tem a personalidade mais difícil de lidar? ",
        "Quem você acha que fala mal dos outros pelas costas?",
        "Qual pessoa do grupo mais te decepcionou até hoje? ",
        "Quem você acha que seria o primeiro a abandonar uma situação difícil? ",
        "Quem é mais hipócrita? ",
        "Qual é a opinião sobre alguém aqui que você nunca teve coragem de dizer? ",
        "Quem tem o maior ego? ", "Quem merece ouvir algumas verdades hoje? ",
        "Quem você acha que não seria seu amigo se vocês não estivessem no mesmo grupo?  ",
        "Quem mais força uma personalidade que não é a verdadeira? ",
        "Quem é mais invejoso? ",
        "Quem tem mais dificuldade em admitir que está errado? ",
        "Quem você acha que é mais interesseiro? ",
        "Qual amizade do grupo parece mais falsa? ",
        "Quem mais gosta de aparecer? ",
        "Se pudesse trocar uma pessoa do grupo por outra, quem seria? ",
        "Quem aqui é a pessoa mais influenciável do grupo? ",
        "Se você tivesse que apontar alguém aqui que finge ser o que não é nas redes sociais, quem seria? ",
        "Quem é a pessoa mais mão de vaca da roda? ",
        "Quem nesta roda você acha que é o mais duas caras, que fala bem na frente e fala mal pelas costas? ",
        "Quem aqui você acha que se acha o mais superior aos outros, mas não tem motivo nenhum para isso? ",
        "Quem aqui você acha que é a pessoa mais tóxica ou que suga a energia do ambiente quando chega? ",
        "Quem tem a energia mais chata da roda? ",
        "Quem aqui só te procura por interesse? ",
        "Quem aqui você menos confia? ",
        "Quem tem o ego mais insuportável da roda? ",
        "Quem aqui força simpatia que não tem? ",
        "Se você pudesse dar um choque de realidade em alguém aqui, em quem seria? ",
        "De quem você cortaria amizade sem dar explicações? ",
        "De quem aqui você tem mais preguiça de conversar? ",
        "Quem é a pessoa mais egocêtrica daqui? ",
        "Se alguém tivesse que ser cancelado aqui, quem mereceria mais? ",
        "Quem aqui você deletaria da sua memória se pudesse? ",
        "Quem se acha o centro das atenções, mas passa vergonha? ",
        "Quem tem o temperamento mais infantil do grupo? ",
        "Quem é a pessoa mais ingrata com os amigos? ",
        "Quem é mais provável de engravidar alguém do curso/trabalho? "
        ]
def registrar(jogador,pergunta,alvo):
    jogadores[jogador] = 0

    print(jogadores)
