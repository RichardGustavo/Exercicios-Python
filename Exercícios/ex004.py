#Escreva uma variável, mostre seu tipo primitivo e use método

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace())
print('Só tem letras?', algo.isalpha())
print('Só tem letras maiúsculas?', algo.isupper())
print('Só tem números?', algo.isnumeric())
print('É alphanumerico?', algo.isalnum(), '\nParabéns, voce aprendeu a concatenar com virgula')
