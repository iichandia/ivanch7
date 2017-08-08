def promedio_notas(I1,I2,I3,Ex):
    lista_notas.append(I1)
    lista_notas.append(I2)
    lista_notas.append(I3)
    lista_notas.append(Ex*2)

        #print(lista_notas)
    a=min(lista_notas)
    lista_notas.remove(a)
        #print(lista_notas)
    suma=0
    for i in lista_notas:
        suma+=i
        
   
    promedio=(suma/len(lista_notas))
    
        #print ("Tu promedio es:", promedio)
    return promedio

def promedio_tareas(notas_tareas):
     suma2=0
     for i in notas_tareas:
        suma2+=i
        #print(suma2)

     promedio_t=(suma2/len(notas_tareas))
        #print ("Tu promedio de tareas es:", promedio_t)
     return promedio_t

def promedio_proyecto(E1,E2,E3,E4):
    #lista_proyecto.append(E1)
    #lista_proyecto.append(E2)
    #lista_proyecto.append(E3)
    #lista_proyecto.append(E4)
    nota_proyecto=(E1*0.15+0.25*E2+0.3*E3+0.3*E4)
    #print(nota_proyecto)
    return nota_proyecto





opcion=int(input("Escoja la opcion de su ramo siendo 1 Catedra, 2 Catedra y tareas, 3 Catedra, tareas, proyecto:"))

if opcion ==1:
    lista_notas=[]
    I1= float(input("Digite su nota de la I1:"))
    I2= float(input("Digite su nota de la I2:"))
    I3= float(input("Digite su nota de la I3:"))
    Ex= float(input("Digite su nota del Examen:"))
    #CATEDRA
    a=promedio_notas(I1,I2,I3,Ex)
    #print(a)    
    print("Tu promedio final es:",a)
elif opcion==2:
    lista_notas=[]
    I1= float(input("Digite su nota de la I1:"))
    I2= float(input("Digite su nota de la I2:"))
    I3= float(input("Digite su nota de la I3:"))
    Ex= float(input("Digite su nota del Examen:"))
    #CATEDRA
    a=promedio_notas(I1,I2,I3,Ex)
    #print(a)
    notas_tareas=[]
    NumeroT= int(input("Digite la cantidad de tareas:"))

    for i in range(NumeroT):
        notas_tareas.append(float(input("Ingrese su nota de tarea:")))
        #print(notas_tareas)
    b=promedio_tareas(notas_tareas)
    NCT= (0.7*a + 0.3*b)
    print("Tu promedio  final es:",NCT)
elif opcion==3:
    lista_notas=[]
    I1= float(input("Digite su nota de la I1:"))
    I2= float(input("Digite su nota de la I2:"))
    I3= float(input("Digite su nota de la I3:"))
    Ex= float(input("Digite su nota del Examen:"))
    #CATEDRA
    a=promedio_notas(I1,I2,I3,Ex)
    #print(a)
    notas_tareas=[]
    NumeroT= int(input("Digite la cantidad de tareas:"))

    for i in range(NumeroT):
        notas_tareas.append(float(input("Ingrese su nota de tarea:")))
        #print(notas_tareas)

    E1= float(input("Digite su nota de la E1:"))
    E2= float(input("Digite su nota de la E2:"))
    E3= float(input("Digite su nota de la E3:"))
    E4= float(input("Digite su nota de la E4:"))
    lista_proyecto=[]
    
    a=promedio_notas(I1,I2,I3,Ex)
    b=promedio_tareas(notas_tareas)
    c=promedio_proyecto(E1,E2,E3,E4)
    NCT= (0.5*a + 0.2*b + 0.3*c)
    print("Tu promedio final es:",NCT)






  

