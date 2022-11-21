print('hoola mundo')
if 5>3:
    print('5 es mayor a 3') 
# Python depende de la identación, no funciona el codigo si está pegado al borde de la columna
if 3>5:
    print('No cumple')
    
x= 99
y= 'chupalo mellanzky'

print(x,y)

email = 'mellaherrera91@gmail.com'
print(email)

a,b,c= 'lala', 'lele','lili'
print(a,b,c)

valor1=valor2=valor3='pico en el ojo'
print(valor1,valor2,valor3)

inicio='Hola'
final='mellanzky'
print(inicio+final)
#tipo de datos
string= 'son palabras'
string2 = "son palabras"

integer = 20
float= 20.2
complejo=1j
print(integer,float,complejo,string)

lista=[1,2,2,3,4,5,6,7]
lista2=lista.copy()
lista.append(8)
print(lista,lista2)
print(lista.count(2)) #conteo de datos de la lista
print(len(lista),len(lista2)) #Largo de las listas

largolista= len(lista)
largolista2= len(lista2)

print (largolista)

print(lista[0]) #accediento a los datos de una lista, el primero es el 0 siempre.

lista.pop() # eliminar el ultimo dato o elemento de la lista
lista.pop() 
print(lista)

# para remover el que nosotros queremos
lista.remove(2)
print(lista)

lista.reverse() #da vuelta el orden
print(lista)

lista.sort() #ordena la lista pero solo cuando son el mismo tipo de dato, si hay strings, integer y float no funcionará

print(lista)

#Si hacemos una lista con () no se puede manipular, se llaman tuplas.
tupla=(1,2,2,3,4,5,6,7)
#Ejemplo
print(tupla)
#tupla.pop()
#tupla.remove(1)
#Para esto se tiene que convertir en una lista con [], entonces:
listadetupla=list(tupla)
listadetupla.append('pico') #modificando
print(listadetupla)

#crear rango
rango=range(3)
print(rango)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
diccionario={
"nombre": "Benito",
"raza":"Poodel",
"edad": 5    
}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['raza'])
print(diccionario.get('nombre')) #the same shit
#cambiar algun dato de un diccionario
diccionario['nombre']= 'Sheraton Shester Shesterton'
print(diccionario)

#agregar un item al diccionario
diccionario['ronronea']='No'
print(diccionario)

#diccionario.pop('ronronea') borrar item
#print(diccionario)
#diccionario.popitem()#eliminar el ultimo item
#print(diccionario)
del diccionario['ronronea']#otra forma de borrar item
print(diccionario)

# copiar diccionario
#copiaperrito=diccionario.copy()
copiaperrito=dict(diccionario)
print(copiaperrito)
print(diccionario,copiaperrito)
#limpiar o borrar diccionario
diccionario.clear()
print(diccionario,copiaperrito)


perritos={
    'Luffy':{
        'nombre':'Luffy',
        'edad':4
    },
    'Zoro':{
        'nombre':'zoro',
        'edad':'10'
    }
}
print(perritos)

#Indexar diccionarios

Luffy = {
        'nombre':'Luffy',
        'edad':4,
        'sexo': 'macho'
    }
Zoro={'nombre':'zoro',
        'edad':'10',
        'sexo': 'macho'
    }

perritos={
    'Luffy':Luffy,
    'Zoro':Zoro
}
print(perritos)
#de otra forma
muestraluffy = dict(Luffy)
print(muestraluffy)

#variables booleanas
verdadero=True
falso=False
print(verdadero,falso)
#-------------------------------------------------------------------
#control de flujo
# evaludar si dos variables son iguales (==), distintas (!=), menor, mayor o igual, etc...

if 2 > 5:
    print('dos es menor a 5 en if')
elif 2 > 5:
    print('2 menor a 5 en elif')
elif 2 < 5:
    print('2 menor a 5 en segundo elif')
else:
    print('yo me imprimo solo si todo lo anterior evalua en falso')


if 2 > 5:
    print('dos es menor a 5 en if')
else:
    print('yo me imprimo solo si todo lo anterior evalua en falso 2')

if 2 < 5: print('if de una linea')

print('cuando devuelve true') if 5 > 2 else print('cuando devuelve false')

if 2 < 5 and 3 > 2:
    print('ambas devuelven true')

if 2 < 5 and 3 < 2:
    print('hay una falsa, esto no se mostrará')

if 1 < 0 or 1 > 0: # si una condición evalua en true se ejecuta la instrucción
    print('una de las dos condiciones devolvió true')

if 1 < 0 or 1 < 0: # si ambas condiciones son falsas entonces no se ejecuta
    print('si ambas condiciones evaluan en true no se ejecuta esto')
#----------------------------------------------------------
#EJERCICIOS sigue con el archivo de calculadora y while

dato= input ('Ingrese dato:  ')

lista= ['hola','mundo','chancho','feliz','drogas']

if lista.count(dato)>0:
    print('El dato existe', dato)
else:
    print('El dato no existe', dato)

first=input ('Ingresa primer numero')
second=input ('Ingresa segundo numero')

first_number= int(first)
second_number= int(second)
print(first_number+second_number)
