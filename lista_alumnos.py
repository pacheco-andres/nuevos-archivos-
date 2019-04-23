print("INGRESO A ESCUELA ")

ALUMNOS = {"Edurdo":1,"Ismael":2,"Jesus":3,"memo":4, "Ivan":5}
def alumnos():
    counter = 1
    print("ALUNOS DE LA ESCUELA")
    for alumno in ALUMNOS.keys():
        print('%s.- %s') %(counter,alumno)
        counter+=1

alumnos()