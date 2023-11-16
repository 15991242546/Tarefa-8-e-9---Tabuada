1# Programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um valor qualquer = '))
print('_'*30)
print ('A Tabuada do Número {} é'.format(n))
print('{} * {:2} = {}'. format (n, 1, n * 1))
print('{} * {:2} = {}'. format (n, 2, n * 2))
print('{} * {:2} = {}'. format (n, 3, n * 3))
print('{} * {:2} = {}'. format (n, 4, n * 4))
print('{} * {:2} = {}'. format (n, 5, n * 5))
print('{} * {:2} = {}'. format (n, 6, n * 6))
print('{} * {:2} = {}'. format (n, 7, n * 7))
print('{} * {:2} = {}'. format (n, 8, n * 8))
print('{} * {:2} = {}'. format (n, 9, n * 9))
print('{} * {:2} = {}'. format (n, 10, n * 10))

print('.'*30)
print("Tabuada novo metodo")
for c in range (1,11):
    print('{} x {:2} = {}'.format (n, c, n*c))



