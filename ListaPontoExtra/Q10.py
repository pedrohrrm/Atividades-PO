# Questão 10
from jellyfish import levenshtein_distance

str1 = input('digite a primeira palavra: ').strip()
str2 = input('digite a segunda palavra: ').strip()
print(levenshtein_distance(str1, str2), 'é a distância de edição')
