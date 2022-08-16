import random 

class SimuladorDeDado:
#def init para passar o comportamento inicial do programa
    def __init__(self):
        self.valormin=1
        self.valormax=6
        self.mensagem="Posso jogar o dado ? (responda com 's' para sim ou 'n' para não: "
        
#função para gerar um valor aleatório entre o valor mínimo até o valor máximo
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

#loop para caso o usuário queira rodar o código outras vezes
while True:
    nov = input("Deseja rolar o dado novamente ? ")
    if nov == "s":
        simulador.Iniciar()
    else:
        break
print("Obrigado pela participação!")
