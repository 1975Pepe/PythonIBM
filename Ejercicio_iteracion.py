#Este código no funciona
zen = '''\
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
'''
f = open('short.zen.txt', 'w') 
f.writelines(zen) #Escribe el fichero
f.close() #Cierra elfichero
f = open('short.zen.txt', 'r') 
f.readline()
print(f)

