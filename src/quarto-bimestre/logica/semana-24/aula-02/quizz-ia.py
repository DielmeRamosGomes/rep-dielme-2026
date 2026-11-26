class AgenteIA:
    def __init__(self, agente):
        self.agente = agente

    def responder(self, pergunta):
        if pergunta == "O que é python?":
            return "Python é uma linguagem de programação"
        elif pergunta == "Gere uma imagem de gta VI":
            return "Imagem gerada com os personagens"
        else:
            return "Pergunta não encontrada"

agente = AgenteIA("TiraDuvídas")
pergunta = input("Qual a duvida?: ")
resposta = agente.responder(pergunta)
print(resposta)
