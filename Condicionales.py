# Declaramos una variable
calificacion = input("Introduce tu calificación de la AZ-900: ")

calificacion = int(calificacion)

#Preguntamos si la calificación es menos a 700
if calificacion < 700 :
    print("Veees, por no estudiar")  # si es menos a 700, muestra esto
elif calificacion > 1000 :
    print("MIENTES!!!! no puede sacar mas de mil")
else : #si no se cumple el if anterior pasa a esta linea.
    print("Felicidades pasa por tu certificado") #Se ejecuta y ninguno de los if se ejecuta
    
#Verficador de mayoria de edad
edad = input("Introduce tu edad")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Eres mayor de edad")
elif edad > 100 :
    print("si vienes a compañad@ de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")

# EN PYTHON NO HAY SWITCH CASE
