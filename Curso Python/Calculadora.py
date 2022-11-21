# #CALCULADORA BY MELLANZKY

# primero=input('Ingresa numero')

# try:
#     primero=int(primero)
# except:
#     primero='pico'
# segundo=input('Ingresa segundo numero')

# try:
#     segundo=int(segundo)

# except:
#     segundo='pico'

# if primero=='pico' or segundo=='pico':
#     print('Ingresaste mal los datos scw, pon numeros') 
# else:
#     print(primero+segundo)
#-----------------------------------------------------

# datos= input('meta los datos ')
# lista=['1','2','3','4','5','6','7','8','8','8','8','9','0']

# if lista.count(datos)>0: 
#     print('el dato existe')
# else:
#     print('el dato no existe ctm')

primern= input('Ingresa numero ctm ')
try:
    primern=int(primern)
except:
    primern='string'
# pero aca falta una condición para que diga error por si no se meten numeros entonces:
if primern=='string':
    print('dato invalido sapo ql')
    exit()
segundon= input('mete segundo numero ctm ')
try:
    segundon=int(segundon)
except:
    segundon='string'
if segundon=='string':
    print('dato invalido sapo reql')
    exit()
#if primern=='string' or segundon=='string':
    #print('pao ql pon numeros ERROR ERROR')
#añadiendo más funciones a la calculadora
simbolo=input("Ingrese simbolo: ")

if simbolo=="*":
    print(primern*segundon)
elif simbolo== "/":
    print(primern/segundon)
elif simbolo== "**":
    print(primern**segundon)
elif simbolo=="+": 
    print(primern+segundon)
elif simbolo=="-": 
    print(primern-segundon)
else:
    print("Syntaxx Error DONT PUT THAT, PUT MATHEMATICAL SIMBOLS")












