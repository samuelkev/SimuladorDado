import random 

class SimuladorDeDado:
    def __init__(self):
        self.valormin=1
        self.valormax=6
        self.mensagem="Posso jogar o dado ? (responda com 's' para sim ou 'n' para não: "

    def GerarValorDado(self):
        print(random.randint(self.valormin, self.valormax))

    def Iniciar(self):
        resposta=input(self.mensagem)
        try:
            if resposta == "s":
                self.GerarValorDado()
            elif resposta == "n":
                print("Obrigado pela participação!")
            else:
                print("Por favor, respostas apenas com s ou n")
        except:
            print("Ocorreu um erro!")

simulador = SimuladorDeDado()
simulador.Iniciar()
while True:
    nov = input("Deseja rolar o dado novamente ? ")
    if nov == "s":
        simulador.Iniciar()
    else:
        break
print("Obrigado pela participação!")
