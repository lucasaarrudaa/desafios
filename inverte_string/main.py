import re

def inverte(palavra):
    if re.match(r'^\w+$', palavra):
        return palavra[::-1]
    return palavra

frase = input("digite uma palavra: ")
invertida = ''.join(inverte(palavra) for palavra in re.split(r'(\W+)', frase))
print(invertida)
