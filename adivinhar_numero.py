# Módulos
from random import randint
from time import sleep

# Gerando O Número Aleatório
numeroAleatorio = randint ( 1 , 100 )

# Input Da Dificuldade Do Jogo
print ( "[ 1 ] -> Modo Easy ( Contém Dica )" )
print ( "[ 2 ] -> Modo Hard ( Sem Dica )" )
dificuldade = int ( input ( "Opção : " ) )
while dificuldade !=1 and dificuldade != 2 : # Caso O Usuário Insira Uma Opção Inexistente
    dificuldade = int ( input ( "Opção Inválida, Tente Novamente : " ) )

# Modo Do Jogo
if dificuldade == 1 :
    modo = "Easy"
else :
    modo = "Hard"

print ( f"Você Escolheu O Modo {modo}, Boa Sorte E Divirta-se !!!" )

# Valor Inicial Do Palpite E Tentativas
palpite = 0
tentativas = 0

# Palpite Do Usuário
while palpite != numeroAleatorio :
    palpite = int ( input ( "Seu Palpite : ( Entre 0 E 100 ) : " ) )
    if palpite < 0 or palpite > 100 : # Caso O Usuário Chute Um Valor Fora Da Range
        print ( "O Número É Entre 1 E 100 !!!" )
    if modo == "Easy" : # Modo Easy
        if palpite > numeroAleatorio : # Caso O Palpite Seja Maior Que O Número
            dica = "Chute Um Número Menor"
        elif palpite < numeroAleatorio : # Caso O Palpite Seja Menor Que O Número
            dica = "Chute Um Número Maior"
    elif modo == "Hard" : # Modo Hard
        dica = ""
    
    # Caso O Usuário Erre
    print ( "Errou !!! Tente Novamente" )
    print ( dica )
    tentativas = tentativas + 1 # Incrementa A Quantidade De Tentativas

# Qunando O Usuário Acertar, Quebrando O Loop While
print ( "Parabéns, Você Acertou !!!" )
print ( f"Quantidade De Tentativas : {tentativas}" )

