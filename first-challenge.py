# Palíndromo em python

print('Digite a palavra ou frase e descubra se ela é palíndromo!')
print()

word = input('Palavra ou frase: ')

if word.strip() == word.strip()[::-1]:
    print('A palavra é palíndromo. 😁')
else:
    print('A palavra não é palíndromo. 😢')