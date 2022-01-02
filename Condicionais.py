nome=input("Digite o nome do paciente: ")
idade=int(input("Digite a idade do paciente: "))
prioridade="Não"
if idade>=65:
    prioridade="Sim"
print(f"O paciente {nome} possui atendimento prioritário? {prioridade}")

#condicional composta

nome=input("Digite o nome do paciente: ")
idade=int(input("Digite a idade do paciente: "))
doencaInfectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()
if idade>=65:
    print(f"O paciente {nome} possui atendimento prioritário!")
elif doencaInfectocontagiosa == "SIM":
    print(f"O paciente {nome} deve ser encaminhado para sala de espera reservada!")
else:
    print(f"O paciente {nome} não tem atendimento prioritário e deve aguardar na sala comum")