#Jogo da forca
print("*********************************)
print ("Bem vindo ao jogo da Foca")
print(**********************************)

palavrasecreta = "Abacaxi".upper
letrasacertadas - ["_"] * len(palavrasecreta)

print(letrasacertadas)

 enforcou = False
 acertou = False

while(not enforcou and not acertou and tentativas < 5) :
    chute = input( "Digite uma letra? ") 
    chute = chute.strip()

if(chute in palavrasecreta):
    index = 0
    for letra in palavrasecreta:
     if(chute.upper() == letra.upper()) :
        print( "Encontrei a letra {} na posição {}".format(letra, index))
    index = index + 1
else:
     tentativas += 1
     
     # controle de tentativas 
     enforcou = tentativas == total_tentativas 
     acertou = "_" not in letrasacertadas                                                                                                                                                                    tentativas += 1
     print("letras acertadas: {}".format(letrasacertadas))
     print("tentativas restantes: {}".format(total_tentativas - tentativas))

     if(arcertou):
        print("parabéns, você ganhou!")
     elif(enforcou):
        print("você perdeu! A palavra era {}".format(palavrasecreta))  

 print( "Fim do Jogo")