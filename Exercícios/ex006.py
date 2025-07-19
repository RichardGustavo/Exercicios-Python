# Como fatiar strings

nome = 'Richard Gustavo Gonçalves'
print(nome[1]) # - Aqui voce consegue identificar um index dentro de uma string
print(nome[1:4]) # - Aqui voce consegue identificar quais index estão dentro desse range (lembre-se: o index termina em i-1)
print(nome[0:10:2]) # - Aqui voce consegue 'pular' os index, dessa forma ele vai mostrar de 2 em 2 (Pula 1, mostra 1)
print(nome[:8]) # - Aqui voce faz com que ele inicie a contagem do 0, voce omitiu o inicio da contagem, entao ele vai comecar a contar do 0, e o proximo número de identificação é o fim (i-1)
print(nome[5:])# - Aqui é a mesma ideia da de cima, só que ao contrário, ele começa onde voce indica e vai até o final da string.
print(nome[1::3]) # - Aqui voce mostra onde começa, o programa lê até o final da string e pula de 3 em 3 (i-1)


print("""O céu alaranjado anunciava o fim de mais um dia tranquilo.
As folhas dançavam com o vento leve, espalhando memórias pelo chão.
Em silêncio, ele sorriu, grato pelas pequenas coisas.""") # - Aqui voce usa áspas 3 vezes para selecionar um texto que está em mais de uma linha.
