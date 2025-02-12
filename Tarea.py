def sucesora(n):
    #s(n)=n+1

    return n+1

def antecesora(n):
    #a(n)=n-1

    return n-1

def suma(a, b):
    if b==0:
        return a
    else:
        return sucesora(suma(a, b-1))
    

def resta(c, d):
    if d==0:
        return c
    else:
        return antecesora(resta(c, d-1))
    

def multi(e, f):
    if f==0:
        return 0
    else:
        return suma(e, multi(e, f-1))

def divi(g, h):
    if h==0:
        return "error"
    elif g < h:
        return 0  
    else:
        return sucesora(divi(resta(g, h), h)) #contar cuantas veces se puede restar g de h
    

print("suma")
    
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

print("El resultado de la suma es: ", suma(a, b))

print("resta")

c=int(input("Ingrese el primer numero: "))
d=int(input("Ingrese el segundo numero: "))

print("El resultado de la resta es: ", resta(c, d))

print("multiplicación")

e=int(input("Ingrese el primer numero: "))
f=int(input("Ingrese el segundo numero: "))

print("El resultado de la multiplicación es: ", multi(e, f))

print("división")

g=int(input("Ingrese el primer numero: "))
h=int(input("Ingrese el segundo numero: "))

print("El resultado de la división es: ", divi(g, h))




#recursión: llamar a si misma una funcion 







