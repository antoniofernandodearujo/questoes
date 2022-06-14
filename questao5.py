"""
    @author: Antonio Fernando
    data: 14/06/2022
"""

str = "Eu consegui!"
string_reversed=[]
i = len(str)
while i > 0: 
    string_reversed += str[i-1]
    i -= 1 

print('Frase no sentido original')
print(str)

print('-'*20)

print('Frase ao contrario')
for frase in string_reversed:
    print('{}'.format(frase), end='')