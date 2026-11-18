from AgenteDuvidas import AgenteDuvidas

if __name__=='__main__':
    agente = AgenteDuvidas("Tutor IA")
    pergunta = input("Digite sua dúvida: ")
    #print(agente.responder(pergunta)) # resposta não encontrada
    print(agente.responder(pergunta))


