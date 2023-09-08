#Agregar personas al diccionario
personas = {
"Diego": 30,
"Daniela": 25,
"Sebastian": 28,
"Alfonso":55,
"Tatiana":40
}
#Lamar diccionario
#print(personas)

#consultar nombre y edad 
while True:
    nombre_consultar = input("Ingresa el nombre de la persona que quiere consultar-->")
    if nombre_consultar in personas:
        edad = personas[nombre_consultar]
        print(f"Nombre: {nombre_consultar}")
        print(f"Edad: {edad} años")

        eliminado = input("Que nombre desea eliminar? (eliminar):").lower()
        if eliminado =="eliminar":
            del personas[nombre_consultar]
            print(f"{nombre_consultar} Ha sido eliminado")
    else:
        print(f"{nombre_consultar} no se escuentra este diccionario")    





 