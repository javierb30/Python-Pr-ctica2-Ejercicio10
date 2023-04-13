import functools

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

"""A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
notas. Utilizar esta estructura para la resolución de los siguientes items."""

def crear_estructura_estudiantes():
    return (zip(lista_nombres,notas_1,notas_2))

def promedio_notas_estudiantes(estudiantes):
    promedio_estudiantes = {}
    for estudiante,nota1,nota2 in estudiantes: 
        promedio_estudiantes[estudiante] = ((nota1 + nota2) / 2)
    return promedio_estudiantes
        
def promedio_general_del_curso(promedio):
    return functools.reduce(lambda x,y: x + y, promedio.values()) / len(promedio)

def estudiante_nota_promedio_mas_alta(promedio):  #inciso_d -->  Identificar al estudiante con la nota promedio más alta
    #Ordeno por mayor a menor promedio y me quedo con el primero
    return sorted(promedio.items(), key = lambda item:item[1], reverse=True)[0][0]

def estudiante_nota_mas_baja(estudiantes):
    estudiantes_dic = {}
    for estudiante,nota1,nota2 in estudiantes:
        estudiantes_dic[estudiante]= nota1 if (nota1<nota2) else nota2
    return sorted(estudiantes_dic.items(), key = lambda item:item[1])[0][0]


#Probando
if __name__ == "__main__":

    nombres = nombres.strip().split(",")
    lista_nombres = [ nombre.replace("'","").replace("\n","").strip() for nombre in nombres ]

    estudiantes = list(crear_estructura_estudiantes())  #inciso_a

    promedio_estudiantes = promedio_notas_estudiantes(estudiantes) #inciso_b
    print(f"Promedio de notas de los estudiantes: \nNombre: {'':<3} Promedio:")
    for nombre,promedio in promedio_estudiantes.items():
        print(f"{nombre:<12}{promedio}")
    
    print(f"Promedio general del curso: {promedio_general_del_curso(promedio_estudiantes):.2f}") #inciso_c

    print(f"Estudiante con la nota promedio mas alta: {estudiante_nota_promedio_mas_alta(promedio_estudiantes)}") #inciso_d
    
    print(f"Estudiante con la nota mas baja: {estudiante_nota_mas_baja(estudiantes)}") #inciso_e
