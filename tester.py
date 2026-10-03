import requests

print("---------TEST DE CONEXION CON LA API ERGAST F1---------"+"\n")

print("Codigo de error 1xx: La peticion se esta realizando."+"\n"
+ "Codigo de error 2xx: La peticion ha sido recibida y realiza con exito."+"\n"
+ "Codigo de error 3xx: Se tiene que redireccionar la peticion para que esta se pueda realizar."+"\n"
+ "Codigo de error 4xx: La peticion se ha hecho de forma incorrecta o no se encuentra."+"\n"
+ "Codigo de error 5xx: El servidor no se encuentra disponible."+"\n")

print("---------TEST PARA SABER DATOS DE LA CARRERA ANTERIOR---------"+"\n")
r = requests.get("http://ergast.com/api/f1/current/last/results")
if r.status_code == 200:
    print(str(r.status_code) +" OK\n")
elif r.status_code == 100:
    print(str(r.status_code) +" INFORMATINAL RESPONSE\n")
elif r.status_code == 300:
    print(str(r.status_code) +" REDIRECTION\n")
elif r.status_code == 400:
    print(str(r.status_code) +" NOT FOUND\n")
elif r.status_code == 500:
    print(str(r.status_code) +" SERVER ERROR\n")
    
print("---------TEST PARA SABER DATOS DE LA PROXIMA CARRERA---------"+"\n")
r = requests.get("http://ergast.com/api/f1/current/next")
if r.status_code == 200:
    print(str(r.status_code) +" OK\n")
elif r.status_code == 100:
    print(str(r.status_code) +" INFORMATINAL RESPONSE\n")
elif r.status_code == 300:
    print(str(r.status_code) +" REDIRECTION\n")
elif r.status_code == 400:
    print(str(r.status_code) +" NOT FOUND\n")
elif r.status_code == 500:
    print(str(r.status_code) +" SERVER ERROR\n")
    
print("---------TEST PARA SABER DATOS DE LA CLASIFICACION DE PILOTOS---------"+"\n")
r = requests.get("http://ergast.com/api/f1/current/driverStandings")
if r.status_code == 200:
    print(str(r.status_code) +" OK\n")
elif r.status_code == 100:
    print(str(r.status_code) +" INFORMATINAL RESPONSE\n")
elif r.status_code == 300:
    print(str(r.status_code) +" REDIRECTION\n")
elif r.status_code == 400:
    print(str(r.status_code) +" NOT FOUND\n")
elif r.status_code == 500:
    print(str(r.status_code) +" SERVER ERROR\n")
    
print("---------TEST PARA SABER DATOS DE LA CLASIFICACION DE CONSTRUCTORES---------"+"\n")
r = requests.get("http://ergast.com/api/f1/current/constructorStandings")
if r.status_code == 200:
    print(str(r.status_code) +" OK\n")
elif r.status_code == 100:
    print(str(r.status_code) +" INFORMATINAL RESPONSE\n")
elif r.status_code == 300:
    print(str(r.status_code) +" REDIRECTION\n")
elif r.status_code == 400:
    print(str(r.status_code) +" NOT FOUND\n")
elif r.status_code == 500:
    print(str(r.status_code) +" SERVER ERROR\n")
