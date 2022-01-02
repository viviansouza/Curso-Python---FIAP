nome=input("Digite o nome do paciente: ")
idade=int(input("Digite a idade do paciente: "))
doencaInfectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()
if idade>=65 and doencaInfectocontagiosa=="SIM":
    print(f"O paciente {nome} possui atendimento prioritário. Ele deve ser encaminhado para sala de espera reservada!")
elif idade<65 and doencaInfectocontagiosa=="SIM":
    print(f"O paciente {nome} não possui atendimento prioritário. Ele deve ser encaminhado para sala de espera reservada!")
elif idade >= 65 and doencaInfectocontagiosa == "NÂO":
    print(f"O paciente {nome} possui atendimento prioritário. Ele deve aguardar na sala de espera comum!")
else:
    print(f"O paciente {nome} não tem atendimento prioritário e deve aguardar na sala comum")