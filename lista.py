#Agregar personas al diccionario
personas = [
("Diego", 30),
("Daniela", 25),
("Sebastian", 28),
("Alfonso",55),
("Tatiana",40)
]
#Lamar lista
#print(personas)

#consultar nombre y edad 
while True:
    nombre_consultar = input("Ingresa el nombre de la persona que quiere consultar-->")
    encontrar = False
    for i, (nombre, edad) in enumerate(personas):
        if nombre == nombre_consultar:
            encontrar = True
            print(f"Nombre: {nombre}")
            print(f"Edad: {edad} años")

            eliminado =input("Que nombre desea eliminar? (eliminar)-->").lower()
            if eliminado == "eliminar":
                personas.pop(i)
                print(f"{nombre_consultar} Ha sido eiminado")
    if not encontrar:
        print(f"{nombre_consultar} no se encuentra en la lista")