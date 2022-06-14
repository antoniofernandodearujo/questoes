"""
    @author: Antonio Fernando
    data: 14/06/2022
"""

def fibonacci_iter(n):
    a = 1
    b = 1
    if n == 1:
        print('0')
    elif n == 2:
        print('0', '1')
    else:
        print('0')
        print(a)
        print(b)
        cont = 0
        for i in range(n - 3):
            total = a + b
            b = a
            a = total
            print(total)
            
            if n == total:
                cont = 1
        
        if cont == 1:
            print('O numero {} esta na sequencia.'.format(n))
        else:
            print('O numero {} nao esta na sequencia.'.format(n))
         
         
fibonacci_iter(13)