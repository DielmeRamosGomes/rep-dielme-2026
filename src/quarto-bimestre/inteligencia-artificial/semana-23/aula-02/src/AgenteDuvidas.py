class AgenteDuvidas:
    def __init__(self, nome):
        self.nome = nome

    def responder(self, pergunta):
        pergunta = pergunta.lower()
        if pergunta == "o que é python?":
            return "Python é uma linguagem de programação."
        elif pergunta == "o que é api?":
            return "API é uma forma de comunicação entre sistemas."
        elif pergunta == "qual é a capital do Brasil?":
            return "Brasília"
        return "Desculpe, ainda não sei responder essa pergunta."

'''
    def responder(self, pergunta):
        return "Resposta não encontrada."
'''
    

