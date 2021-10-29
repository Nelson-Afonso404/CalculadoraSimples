import termcolor
from termcolor import colored
#instruções
print(colored('BEM VINDO A MINHA CALCULADORA!' , 'red'))
print(colored('Essas são as operações possiveis:' , 'green'))
print('#'*35)
print('somar=       +')
print('subtrair=    -')
print('multiplicar= *')
print('dividir=     /')
print('potenciar=  **')
print('#'*35)
#pedindo pra digitar os valores
while True:
	num1=input(colored('digite um numero: ' , 'yellow'))
	num2=input(colored('digite outro numero: ' , 'yellow'))
	operador=input(colored('digite um operador: ' , 'yellow'))
	
#aplicando condições
	exit=input('Deseja sair? [s]im ou [n]ão: ')
	if exit == 's':
		break
    
	if not num1.isnumeric() or not num2.isnumeric():
		print('Digite apenas números')
		continue
	num1=int(num1)
	num2=int(num2)
#resolvendo valores
	if operador == "+":
   	 print(num1 + num2)
	elif operador == "-":
		print(num1 - num2)
	elif operador == '*':
 	   print(num1 * num2)
	elif operador == '/':
		print(num1/num2)
	elif operador == '**':
		print(num1**num2)
	else:
 	   print('Digite um operador válido')
    
print('ACABOU A CALCULADORA')