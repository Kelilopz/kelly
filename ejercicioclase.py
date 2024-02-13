#1.Registro de los participantes
Participantes=[]
Eventos=[]
cont=0
def registroParticipantes(documentoIdentidad, nombre,edad,cargo):
    for x in Participantes:
        if x["Documento"]==documentoIdentidad:
            print("El usuario ya existe")
            return
    pago=False
    nuevoParticipante={'Documento':documentoIdentidad, 'Nombre':nombre,'Edad':edad,'Cargo':cargo,'Pago':pago}
    Participantes.append(nuevoParticipante)
    print("Participante agregado exitosamente")

#2.Registro de eventos

def registroEventos(nombreEvento,locacion,diadelmes):
    for y in Eventos:
        if y["NombredelEvento"]==nombreEvento:
            print("El evento y0a ")
            return
    realizado=False
    nuevoEvento={'NombredelEvento':nombreEvento,'Ubicacion':locacion,'DiaMes':diadelmes,'Realizacion':realizado}
    Eventos.append(nuevoEvento)
    print("Evento Registrado correctamente")

#3.Funcion para eliminar participantes

def eliminarParticipantes(documentoIdentidad):
    for j in Participantes:
        if j['Documento']==documentoIdentidad :
            if j['Pago']==False :
                Participantes.remove(j)
                print("el participante ha sido eliminado")
                return
            else:
                print("El participante ya cancelo, por tanto no puede ser quitado del registro ")
    print("Este participante no se encuentra registrado") 

#4.Cambiar el estado de la inscripción

def pagarInscripcion(documentoIdentidad):
    for k in Participantes:
        if k['Documento']==documentoIdentidad:
            if k['Pago']==False:
                pagonuevo=bool(int(input("El usuario ya canceló los 50k? escriba un numero diferente de cero y si no ha pagado escriba cero(0)")))
                k['Pago']=pagonuevo
            else:
                print("El usuario ya canceló su inscripción")
        else:
            print('el usuario no se encuentra registrado o lo escribiste mal')

#5.Saber cuantos empleados no han pagado su aporte

def usuariosnopagos(Participantes):
    for x in Participantes:
        if x['Pago']==False:
            print(x['Nombre'])
            print("No se han pagado los 50k")
            cont+=1
    print("las personas que deben son", " = ", cont)
    print("Falta por recibir ", (cont*50000))
            
    
#6. Modificar eventos

def modificarEventos(nombreEvento,locacion,diadelmes):
  for y in Eventos:
    if y['Realizacion']==False:
        opcion=1
        while opcion!=0:
            opcion=int(input("1.Modificar nombre del evento\n2.Modificar ubicacion\n3.Modificar dia del mes\n4.Eliminar Evento\n5.Cambiar Estado del Evento\n0.Salir\n"))
            if opcion==1:
                nombre=input("Ingrese el nuevo nombre del evento")
                for z in Eventos:
                    if z['NombredelEvento']==nombreEvento:
                        z['NombredelEvento']=nombre
                        print("El evento ha sido modificado")
            elif opcion==2:
                locacion=input("Ingrese la nueva ubicacion del evento")
                for z in Eventos:
                    if z['NombredelEvento']==nombreEvento:
                        z['Ubicacion']=locacion
                        print("La ubicacion ha sido modificada")
            elif opcion==3:
                diadelmes=int(input("Ingrese el nuevo dia del mes"))
                for z in Eventos:
                    if z['NombredelEvento']==nombreEvento:
                        z['DiaMes']=diadelmes
                        print("El día evento ha sido modificada")
            elif opcion==4:
                if Eventos['Realizacion']==False:
                    for z in Eventos:
                        if z['NombredelEvento']==nombreEvento:
                            Eventos.remove(z)
                            print("El evento ha sido eliminado")
                else:
                    print("El evento ya ha sido realizado")
            elif opcion==5:
                 for y in Eventos:
                    if y['NombredelEvento']==nombreEvento:
                        realizado=True
                        print("El evento ya ha sido realizado")
                    return realizado
            else:
                print("Opcion incorrecta")
    else:
        print("El evento ya ha sido realizado")
    

#Inicio de Algoritmo 

while True:
    opcion=int(input("1.Registro de participantes\n2.Registro de eventos\n3.Eliminar participantes\n4.Pagar inscripcion\n5.Usuarios que no han pagado su aporte\n6.Modificar eventos\n7.Salir\n"))
    if opcion==1:
        documentoIdentidad=int(input("Ingrese su documento de identidad"))
        nombre=input("Ingrese su nombre")
        edad=int(input("Ingrese su edad"))
        cargo=input("Ingrese su cargo")
        registroParticipantes(documentoIdentidad,nombre,edad,cargo)
    elif opcion==2:
        nombreEvento=input("Ingrese el nombre del evento")
        locacion=input("Ingrese la ubicación del evento")
        diadelmes=int(input("Ingrese el dia del mes"))
        registroEventos(nombreEvento,locacion,diadelmes)
    elif opcion==3:
        documentocambiar=int(input("Por favor ingresa el documento del usuario que deseas eliminar"))
        eliminarParticipantes(documentocambiar)
    elif opcion==4:
        documentonuevo=int(input("por favor inserta el documento de la persona que va a pagar su inscripción"))
        pagarInscripcion(documentoIdentidad)
    elif opcion==5:
        usuariosnopagos(Participantes)
    elif opcion==6:
        modificarEventos(nombreEvento,locacion,diadelmes)
    elif opcion==7:
        print("Espero tengas un lindo día")
        break
    else:
        print("No pusiste una opción correcta")