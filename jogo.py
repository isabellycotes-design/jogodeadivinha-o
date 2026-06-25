import random
print("*********************************")
print("Bem vindo ao jogo de Adivinhação")
print("*********************************")

numerosecreto = 40
totaldetentativas = 10

chute = input("Digite o seu número:")
print("Você digitou: ", chute)

chutenumerico = int(chute)

while(totaldetentativas > 0):
    print("Você tem ", totaldetentativas,"tentativas")
    totaldetentativas = totaldetentativas - 1
    print("tentativas restantes:", totaldetentativas) 
    
    if(totaldetentativas == 0):
        print("você não tem mais tentativas. Fim do jogo.")
        break



acertou = chuteNumerico == numerosecreto
maior = chuteNumerico == numerosecreto
menor = chuteNumerico == numerosecreto

if(numerosecreto == chuteNumerico):
    print("Parabéns! você acertou! Fim do jogo")
else:
    if(maior): 
        print("você errou! O seu chute foi maior que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("fim do jogo")