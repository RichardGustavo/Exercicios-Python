# Como dividir strings

nome = 'Richard Gustavo Gonçalves'

print(nome.split()) # - Aqui você consegue dividir os espaços e tornar cada palavra em uma string diferente uma da outra.
new_name = nome.split() # - Aqui você criou uma nova variável onde voce quer encontrar o primeiro índice da variavel nome splitado.
print(nome.split()[0]) # - Esse print e o debaixo resultam na mesma coisa, a diferença é que eu mandei printar sem usar a variável new_name.
print(new_name)

# Como usar o join

new_nome = nome.split()
print('-'.join(nome)) # - Aqui você colocar uma string qualquer dentro da sua frase sem estar splitado (veja no RUN).
print('-'.join(new_nome)) # - Aqui você colocar uma string qualquer dentro da sua frase, depois de splitado (veja no RUN).