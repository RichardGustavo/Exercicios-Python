# Analisar uma string

nome = 'Richard Gustavo Gonçalves'


print(len(nome)) # - Aqui voce lê quantos indexadores tem uma string (ISSO É DE EXTREMA IMPORTÂNCIA)
print(nome.count('a')) # - Aqui voce consegue contar quantas vezes determinada str aparece dentro da sua frase ou texto, lembre-se que o python diferencia letrar maiúsculas das minúsculas
print(nome.count('a', 0, 25)) # - Aqui voce determina quantas letras quer procurar na sua frase em um determinado range (lembre-se: i-1)
print(nome.find('Ric')) # - Aqui ele vai ter mostrar onde começa determinado 'texto' que voce escreve para procurar na sua string.
print(nome.find('Qualquer coisa')) # - Aqui ele vai retornar -1, porque o valor que voce pediu para ser encontrado não existe.
