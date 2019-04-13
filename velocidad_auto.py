velocidad_min = 40
velocidad_med = 80
velocidad_may = 81
velocidad_usuario = "velocidad"
velocidad_usuario = (int(input("ingrese su velocidad  ")))
if velocidad_usuario <= velocidad_min:
    print("su velocidad es minima ")
    print("conduzca por su carril de baja velocidad")
elif velocidad_usuario <= velocidad_med:
    print("su velocidad es media ")
    print("localize su carril de velocidad media")
else:
    print("CUIDADO SU VELOCIDAD ES DEMACSIADO ALTA")
    print("utilize su cinturon de seguridad ")