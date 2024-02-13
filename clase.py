import json
datos = []

def cargarDatos():
    with open("veterinariaBD.json", "r") as file:
        respuesta = json.load(file)
        return respuesta

def guardarDatos(datos):
    with open("veterinariaBD.json", "w") as file:
        escritura = json.dumps(datos)
        file.write(escritura)

def crearAnimal():
    try:
        animales = list(cargarDatos())
        tipo = input("Ingrese el tipo de animal: ")
        nPatas = int(input("Ingrese el numero de patas del animal: "))
        raza = input("Ingrese la raza del animal: ")
        animal = {"tipo": tipo, "nPatas": nPatas, "Raza": raza}
        animales.append(animal)
        guardarDatos(animales)
        print("Animal creado con éxito!")
    except Exception:
        print("Ocurrió un error al crear animal!")

def eliminarAnimal():
    try:
        animales=list(cargarDatos())
        animal=input("Ingrese el tipo de animal que deseas elminar")
        for x in animales:
            if x['tipo']==animal:
                animales.remove(x)
    except:
        print("El dato ingresado no se encuenta en la lista")         

crearAnimal()
