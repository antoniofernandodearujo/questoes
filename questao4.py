"""
    @author: Antonio Fernando
    data: 14/06/2022
"""
vSP = 63836.43
vRJ = 36678.66
vMG = 29229.88
vES = 27165.48
outros = 19849.53

somaTotal = (vSP + vRJ + vMG + vES + outros)

print('Distribuidora de SP:   {}%'.format((vSP / somaTotal) * 100))
print('Distribuidora do RJ:   {}%'.format((vRJ / somaTotal) * 100))
print('Distribuidora de MG:   {}%'.format((vMG / somaTotal) * 100))
print('Distribuidora do ES:   {}%'.format((vES / somaTotal) * 100))
print('Outras Distribuidoras: {}%'.format((outros / somaTotal) * 100))