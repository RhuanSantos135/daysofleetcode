STEP =2
qtd_pessoas = int(input())

pessoas = [i for i in range(1, qtd_pessoas + 1)]


atual = 0 
morto = 0

while len(pessoas) >1:
    morto = atual + (STEP - 1)
    while morto >= len(pessoas):
        morto =  morto -len(pessoas)
    pessoas.pop(morto)
    
    atual = morto
    if atual >= len(pessoas):
        atual = atual - len(pessoas)
