# Instalando as ferramentas do nosso Robô Analista 
import xml.etree.ElementTree as ET 
import json 
import pandas as pd 
from datetime import datetime 
import matplotlib.pyplot as plt 
 
print("Robô Analista inicializado com sucesso!") 
print("Ferramentas de análise carregadas!") 

# Simulando dados de cobertura XML (como JaCoCo geraria)
xml_cobertura = """<?xml version="1.0" encoding="UTF-8"?>
<coverage>
    <module name="login" lines-covered="450" lines-total="500" coverage="90.0"/>
    <module name="pagamento" lines-covered="720" lines-total="1200" coverage="60.0"/>
    <module name="relatorios" lines-covered="1600" lines-total="2000" coverage="80.0"/>
    <module name="forum" lines-covered="540" lines-total="600" coverage="90.0"/>
    <module name="cadastro" lines-covered="760" lines-total="800" coverage="95.0"/>
</coverage>"""

print("Arquivo XML de cobertura simulado criado!") 
print("Dados prontos para análise pelo Robô Analista")

# Função para o robô processar XML de cobertura 
def processar_cobertura_xml(xml_data): 
    print("Robô Analista processando dados de cobertura...") 
    # Parseando o XML 
    root = ET.fromstring(xml_data) 
 
    # Extraindo dados de cada módulo 
    modulos_data = [] 
    for module in root.findall('module'): 
        nome = module.get('name') 
        linhas_cobertas = int(module.get('lines-covered')) 
        linhas_totais = int(module.get('lines-total')) 
        cobertura = float(module.get('coverage')) 
             
        modulos_data.append({ 
            'modulo': nome, 
            'linhas_cobertas': linhas_cobertas, 
            'linhas_totais': linhas_totais, 
            'cobertura_pct': cobertura, 
            'linhas_descobertas': linhas_totais - linhas_cobertas 
        }) 
 
    return modulos_data 
 
# Executando o processamento 
dados_processados = processar_cobertura_xml(xml_cobertura) 
print("Processamento concluído!") 
 
# Mostrando os dados processados 
for modulo in dados_processados: 
    print(f"{modulo['modulo']}: {modulo['cobertura_pct']}% de cobertura") 

# Convertendo para DataFrame (como ferramentas profissionais fazem) 
df_cobertura = pd.DataFrame(dados_processados) 
 
print("\nRELATÓRIO AUTOMATIZADO DE COBERTURA") 
print("=" * 50) 
print(df_cobertura.to_string(index=False)) 
 
# Calculando estatísticas gerais 
cobertura_media = df_cobertura['cobertura_pct'].mean() 
cobertura_total = (df_cobertura['linhas_cobertas'].sum() / df_cobertura['linhas_totais'].sum()) * 100 
 
print(f"\n RESUMO EXECUTIVO:") 
print(f"Cobertura Média: {cobertura_media:.1f}%") 
print(f"Cobertura Total: {cobertura_total:.1f}%") 

# Robô identificando módulos que precisam de atenção 
def analisar_qualidade_modulos(df): 
    print("\nANÁLISE AUTOMÁTICA DE QUALIDADE") 
    print("=" * 40) 
     
    # Módulos com baixa cobertura (< 70%) 
    baixa_cobertura = df[df['cobertura_pct'] < 70] 
    if not baixa_cobertura.empty: 
        print("MÓDULOS COM BAIXA COBERTURA:") 
        for _, modulo in baixa_cobertura.iterrows(): 
            print(f"   {modulo['modulo']}: {modulo['cobertura_pct']}%") 
     
    # Módulos com boa cobertura (> 90%) 
    boa_cobertura = df[df['cobertura_pct'] > 90] 
    if not boa_cobertura.empty: 
        print("MÓDULOS COM BOA COBERTURA:") 
        for _, modulo in boa_cobertura.iterrows(): 
            print(f"   {modulo['modulo']}: {modulo['cobertura_pct']}%") 
 
    # Recomendações automáticas 
    print("\n RECOMENDAÇÕES AUTOMÁTICAS:") 
    if not baixa_cobertura.empty: 
        print("   Priorizar testes nos módulos com baixa cobertura") 
        print("   Meta: Elevar cobertura para pelo menos 80%") 
    else: 
        print("    Todos os módulos atendem aos critérios mínimos!") 
 
# Executando a análise 
analisar_qualidade_modulos(df_cobertura) 

# Função para gerar badges baseados na cobertura 
def gerar_badge_cobertura(cobertura_pct): 
    if cobertura_pct >= 90: 
        return f"[coverage | {cobertura_pct:.0f}% | brightgreen]" 
    elif cobertura_pct >= 80: 
        return f"[coverage | {cobertura_pct:.0f}% | green]" 
    elif cobertura_pct >= 70: 
        return f"[coverage | {cobertura_pct:.0f}% | yellow]" 
    else: 
        return f"[coverage | {cobertura_pct:.0f}% | red]" 
 
print("\nBADGES GERADOS AUTOMATICAMENTE:") 
print("=" * 40) 
 
# Gerando badge para cobertura total 
badge_total = gerar_badge_cobertura(cobertura_total) 
print(f" Badge do Projeto: {badge_total}") 
 
# Gerando badges por módulo 
print("\n Badges por Módulo:") 
for _, modulo in df_cobertura.iterrows(): 
    badge = gerar_badge_cobertura(modulo['cobertura_pct']) 
    print(f"   {modulo['modulo']}: {badge}") 

# Simulando um relatório como GitHub Actions geraria 
def gerar_relatorio_ci(): 
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
 
    relatorio = f""" 
RELATÓRIO AUTOMÁTICO DE CI/CD 
 
Gerado em: {timestamp} 
 
Build: SUCESSO 
 Cobertura Total: {cobertura_total:.1f}% 
 Testes Executados: 150 
 Testes Passaram: 147 
 Testes Falharam: 3 
 
TENDÊNCIA DE COBERTURA: 
   Commit anterior: 78.2% 
   Commit atual: {cobertura_total:.1f}% 
   Variação: +{cobertura_total - 78.2:.1f}% 
STATUS: {"APROVADO" if cobertura_total >= 75 else "REPROVADO"} 
"""     
    return relatorio 

# Gerando e exibindo o relatório 
relatorio_ci = gerar_relatorio_ci() 
print(relatorio_ci) 

# Criando visualização automática (como Jenkins faz) 
plt.figure(figsize=(10, 6)) 
 
# Gráfico de barras da cobertura por módulo 
cores = ['red' if x < 70 else 'yellow' if x < 80 else 'green' for x in df_cobertura['cobertura_pct']] 
 
plt.subplot(1, 2, 1) 
plt.bar(df_cobertura['modulo'], df_cobertura['cobertura_pct'], color=cores) 
plt.title(' Cobertura por Módulo\n(Gerado Automaticamente)') 
plt.ylabel('Cobertura (%)') 
plt.xticks(rotation=45) 
plt.axhline(y=80, color='orange', linestyle='--', label='Meta (80%)') 
plt.legend() 
 
# Gráfico de pizza das linhas cobertas vs descobertas 
plt.subplot(1, 2, 2) 
total_cobertas = df_cobertura['linhas_cobertas'].sum() 
total_descobertas = df_cobertura['linhas_descobertas'].sum() 

plt.pie([total_cobertas, total_descobertas],  
        labels=['Linhas Cobertas', 'Linhas Descobertas'], 
        colors=['lightgreen', 'lightcoral'], 
        autopct='%1.1f%%') 
 
plt.title('Distribuição Geral\nde Cobertura') 
plt.tight_layout() 
plt.show() 
 
print("Gráficos gerados automaticamente pelo Robô Analista!")