print("*********************************")
print("Bem vindo ao jogo de Adivinhação")
print("*********************************")

numerosecreto = 40

chute = input("Digite o seu número:")
print("Você digitou: ", chute )

chuteNumerico = int(chute)

acertou = chuteNumerico == numerosecreto
maior = chuteNumerico == numerosecreto
menor = chuteNumerico == numerosecreto

if(numerosecreto == chuteNumerico):
    print("você acertou!")
else:
    print("você errou!")

print("fim do jogo")