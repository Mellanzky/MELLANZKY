i=0
while i< 90:
    i+=5
    if i==50:
        continue
    print(i)
    
#break sirve para detener el loop, continue sirve para seguir pero se salta el numero en el if
print("de otra forma")
i=0
while i< 90:
    print(i)
    i+=5

print("otro forma, al fin al cabo el orde de los codigos altera el resultado")
i=0
while i< 90:
    print(i)
    if i==50:
        break
    i+=5