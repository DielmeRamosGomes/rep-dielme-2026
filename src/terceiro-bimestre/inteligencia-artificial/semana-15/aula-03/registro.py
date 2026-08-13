def triagem_simbolica(queixa):
    queixa = queixa.lower()
    
    # Tentativa de cobrir casos de emergência via regras manuais
    if ("sangue" in queixa) or ("desmaio" in queixa) or ("respirar" in queixa):
        return "ALTA: Vá ao hospital imediatamente."
    
    # Tentativa de cobrir casos médios
    elif ("febre" in queixa) or ("dor forte" in queixa):
        return "MÉDIA: Agende uma consulta para hoje."
        
    # Caso padrão
    elif ("dor" in queixa) or ("incômodo" in queixa):
        return "BAIXA: Observe os sintomas."
    
    else:
        return "ERRO: Não compreendi a queixa. Seja mais específico."

# Área de Testes (Execute o código com estas frases)
#print(triagem_simbolica("Minha cabeça dói um pouco."))
#print(triagem_simbolica("Sinto uma pressão no peito e falta de ar."))
#print(triagem_simbolica("Não consigo puxar o ar e minha visão escureceu."))
#print(triagem_simbolica("Estou com dor de garganta."))
print(triagem_simbolica("Não estou com febre, na verdade estou gelado e tremendo muito, sentindo uma pontada fina no braço esquerdo."))