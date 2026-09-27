from pathlib import Path

dados = [
    ["Ana", 19, "ADS"],
    ["Bruno", 21, "Geografia"],
    ["Carla", 20, "TI"],
    ["Diego", 22, "Engenharia"]
]

with open(Path(__file__).with_name("alunos.txt"), "w") as arquivo:
    for aluno in dados:
        arquivo.write(f"{aluno[0]}, {aluno[1]}, {aluno[2]}\n")
if arquivo.closed:
    print("Arquivo gravado com sucesso!")


