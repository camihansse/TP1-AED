#datos
patente = input ("Ingrese los caracteres de la patente:")


#procesos 
if len (patente) == 7 :
    if patente[0].isalpha() :
        patente_1ercaract = 'L'

    else:
        patente_1ercaract = 'N'

    if patente[1].isalpha():
        patente_2docaract= 'L'
 
    else:
         patente_2docaract = 'N'

    if patente[2].isalpha():
        patente_3ercaract= 'L'
    else:
        patente_3ercaract = 'N'

    if patente[3].isalpha():
        patente_4tocaract= 'L'
    else:
        patente_4tocaract = 'N'
    
    if patente[4].isalpha():
        patente_5tocaract= 'L'
    else:
        patente_5tocaract = 'N' 


    if patente[5].isalpha():
        patente_6tocaract= 'L'
    else:
        patente_6tocaract = 'N'


    if patente[6].isalpha():
        patente_7timocaract= 'L'
    else:
        patente_7timocaract = 'N'
    patente = patente_1ercaract + patente_2docaract + patente_3ercaract + patente_4tocaract + patente_5tocaract + patente_6tocaract + patente_7timocaract
else: 
    patente = 'Otro'

if patente == 'LLNNNLL':
    origen_patente = 'Argentina'

if patente == 'LLLNLNN':
    origen_patente = 'Brasil'

if patente == ' LLNNNNN':
    origen_patente = 'Bolivia'

if patente == 'LLLLNNN':
    origen_patente = 'Paraguay' 

if patente == 'LLLLNNN':
    origen_patente = 'Uruguay'

if patente == 'Otro':
    origen_patente = 'Otro'
#resultados 

print (patente)
print (origen_patente)