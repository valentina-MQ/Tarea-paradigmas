Solución de la tarea solicitada en clase haciendo uso de la función sucesora y antecesora.

def sucesora(n):
    #s(n)=n+1

    return n+1

def antecesora(n):
    #a(n)=n-1

    return n-1

Implementacion de operaciones:

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
        return sucesora(divi(resta(g, h), h)) 

Al momento de crear la división, no se puede implementar la función antecesora ya que si esta se implementa el resultado seria un numero negativo, lo cual se 
contradice con los parametros expuestos en clase.

