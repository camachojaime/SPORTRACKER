import requests
import json
from requests import *

#   ```
#   🔜 🔙   📆🕓


def helpCommandStart():
    return "/help\n/command\n/start\n\n/ultimaCarrera\n/proximaCarrera\n/verClasificacionPilotos\n/verClasificacionConstructores"


def lastRace():

    anterior= requests.get("http://ergast.com/api/f1/current/last/results.json")
    anteriorTEXT = anterior.text
    anteriorJSON = json.loads(anteriorTEXT)

    datosAnterior = "🏁``` " + anteriorJSON["MRData"]["RaceTable"]["Races"][0]["raceName"] + "\n"
    datosAnterior += "🏟 " + anteriorJSON["MRData"]["RaceTable"]["Races"][0]["Circuit"]["circuitName"] + "\n"
    datosAnterior += "📍 " + anteriorJSON["MRData"]["RaceTable"]["Races"][0]["Circuit"]["Location"]["locality"] + " (" + anteriorJSON["MRData"]["RaceTable"]["Races"][0]["Circuit"]["Location"]["country"] +")\n"
    datosAnterior += "🔙 Round: " + anteriorJSON["MRData"]["RaceTable"]["Races"][0]["round"] + "\n\n"

    for x in range(20):
        posicionAnterior = anteriorJSON["MRData"]["RaceTable"]["Races"][0]["Results"][x]["position"]
        if int(posicionAnterior) < 10:
            if int(posicionAnterior) < 4:
                if int(posicionAnterior) == 1:
                    posicionAnterior = "🥇\t\t\t"
                elif int(posicionAnterior) == 2:
                    posicionAnterior = "🥈\t\t\t"
                elif int(posicionAnterior) == 3:
                    posicionAnterior = "🥉\t\t\t"
            else:
                posicionAnterior += "\t\t\t\t"
        else:
            posicionAnterior += "\t\t\t"
        
        numero = anteriorJSON["MRData"]["RaceTable"]["Races"][0]["Results"][x]["number"]
        if int(numero) < 10:
            numero = " " + numero
        numero += "\t\t\t"

        nombreAnterior = anteriorJSON["MRData"]["RaceTable"]["Races"][0]["Results"][x]["Driver"]["givenName"]+"\t\t"
        apellidoAnterior = anteriorJSON["MRData"]["RaceTable"]["Races"][0]["Results"][x]["Driver"]["familyName"]+"\n"
        datosAnterior += (posicionAnterior + numero +nombreAnterior + apellidoAnterior )
    
    return datosAnterior + "```"


def nextRace():
    datos = ""

    siguiente = requests.get("http://ergast.com/api/f1/current/next.json")
    siguienteTEXT = siguiente.text
    siguienteJSON = json.loads(siguienteTEXT)

    datos += "🏁```" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["raceName"] + "\n"
    datos += "🏟 " + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["Circuit"]["circuitName"] + "\n"
    datos += "📍 " + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["Circuit"]["Location"]["locality"] + " (" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["Circuit"]["Location"]["country"] + ")" + "\n"
    datos += "🔜 Round: " + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["round"] + "\n\n"

    datos += "Practice 1: 📆" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["FirstPractice"]["date"] + "\t🕓" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["FirstPractice"]["time"] + "\n"
    # datos += "Qualifying: 📆" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["Qualifying"]["date"] + "\t🕓" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["Qualifying"]["time"] + "\n\n"
    datos += "Practice 2: 📆" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["SecondPractice"]["date"] + "\t🕓" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["SecondPractice"]["time"] + "\n\n"
    
    datos += "Practice 3: 📆" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["ThirdPractice"]["date"] + "\t🕓" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["ThirdPractice"]["time"] + "\n"
    # datos += "Sprint: 📆" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["Sprint"]["date"] + "\t🕓" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["Sprint"]["time"] + "\n\n"
    datos += "Qualifying: 📆" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["Qualifying"]["date"] + "\t🕓" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["Qualifying"]["time"] + "\n\n"
    
    datos += "Race: 📆" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["date"] + "\t🕓" + siguienteJSON["MRData"]["RaceTable"]["Races"][0]["time"]

    return datos + " ```"


def driversQualy():
    datos = "Pos\t\t\tPts\t\tNum\t\tName\n\n"

    drivers = requests.get("http://ergast.com/api/f1/current/driverStandings.json")
    driversTEXT = drivers.text
    driversJSON = json.loads(driversTEXT)

    for x in range(len(driversJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"])):
        pos = driversJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][x]["position"]
        if int(pos) < 10:
            if int(pos) < 4:
                if int(pos) == 1:
                    pos = "🥇\t\t\t"
                elif int(pos) == 2:
                    pos = "🥈\t\t\t"
                elif int(pos) == 3:
                    pos = "🥉\t\t\t"
            else:
                pos += "\t\t\t\t"
        else:
            pos += "\t\t\t"

        puntos = driversJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][x]["points"]
        if int(puntos) < 10:
            puntos = "  " + puntos
        elif int(puntos) < 100:
            puntos = " " + puntos
        puntos += "\t\t"

        numero = driversJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][x]["Driver"]["permanentNumber"]
        if int(numero) < 10:
            numero = " " + numero
        numero += "\t\t"

        nombreApellido = driversJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][x]["Driver"]["givenName"] + " " + driversJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][x]["Driver"]["familyName"]

        datos += pos + puntos + numero + nombreApellido + "\n"

    return "```" + datos + "```"


def constructorsQualy():
    datosCons = "Pos\t\t\tPts\t\t\tConstructor\n\n"
    
    cons = requests.get("http://ergast.com/api/f1/current/constructorStandings.json")
    consTEXT = cons.text
    consJSON = json.loads(consTEXT)

    for x in range(len(consJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"])):
        posConst = consJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"][x]["position"]
        if int(posConst) < 10:
            if int(posConst) < 4:
                if int(posConst) == 1:
                    posConst = "🥇\t\t\t"
                elif int(posConst) == 2:
                    posConst = "🥈\t\t\t"
                elif int(posConst) == 3:
                    posConst = "🥉\t\t\t"
            else:
                posConst += "\t\t\t\t"
        else:
            posConst += "\t\t\t"

        puntos = consJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"][x]["points"]
        if int(puntos) < 10:
            puntos = "  " + puntos
        elif int(puntos) < 100:
            puntos = " " + puntos
        puntos += "\t\t\t"

        nombreCons = consJSON["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"][x]["Constructor"]["name"]

        datosCons += posConst + puntos + nombreCons + "\n"
    
    return "``` Pos" + datosCons + "```"