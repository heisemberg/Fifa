import os
def addEquipo(equipos):
    teamName = input('Ingrese el nombre del equipo: ').upper()
    myTeam = [teamName,[],[],[],[]]
    equipos.append(myTeam)

def addPlayer(equipos):
    isAddPlayer=True
    equipo = input('Ingrese el nombre del Equipo: ').upper()
    for item in equipos:
        if equipo in item:            
            while isAddPlayer:
                namePlayer = input('Ingrese el nombre del jugador: ')
                agePlayer = input('Ingrese la edad del jugador:')
                dorsalPlayer = input('Ingrese el numero del dorsal del jugador:')
                positions = ["Arquero","Defensa","Delantero","Medio Central"]
                print('Seleccione la posicion del jugador: ')
                for i, position in enumerate(positions):
                    print (f'{i+1}. {position}')
                positionPlayer = positions[int(input())-1]
                myPlayer = [namePlayer,agePlayer,dorsalPlayer,positionPlayer]
                item[1].append(myPlayer)
                isAddPlayer = bool(input("Desea agregar otro Jugador S(Si) Enter(No)"))

def addTecnico(equipos):
    isAddTecnico=True
    equipo = input('Ingrese el nombre del Equipo: ').upper()
    for item in equipos:
        if equipo in item:
            while isAddTecnico:
                nameTecnico = input('Ingrese el nombre del tecnico: ')
                ageTecnico = input('Ingrese la edad del tecnico:')
                titles = ["Director tecnico","Asistente Tecnico","Entrenador De Arquero","Entrenador"]
                print('Seleccione el cargo del tecnico: ')
                for i, job in enumerate(titles):
                    print(f'{i+1}. {job}')
                titleTecnico = titles[int(input())-1]
                tecnico = [nameTecnico,ageTecnico,titleTecnico]
                item[2].append(tecnico)
                isAddTecnico=bool(input("Desea agregar otro Tecnico S(Si) Enter(No)"))

def addMedico(equipos):
    isAddMedico=True
    equipo = input('Ingrese el nombre del Equipo: ').upper()
    for item in equipos:
        if equipo in item:
            while isAddMedico:
                nameMedico = input('Ingrese el nombre del medico: ')
                ageMedico = input('Ingrese la edad del medico:')
                titles = ["Fisioterpeuta","Camillero","Masajista","Psicologo"]
                print('Seleccione el cargo del medico: ')
                for i, job in enumerate(titles):
                    print(f'{i+1}. {job}')
                titleMedico = titles[int(input())-1]
                medico = [nameMedico,ageMedico,titleMedico]
                item[3].append(medico)
                isAddMedico=bool(input("Desea agregar otro Medico S(Si) Enter(No)"))

def showEntrenador(equipos):
    for item in equipos:
        for j in item[2]:
            if 'entrenador' in j:
                print(f'{item[0]} -- {j[0]}')
    

def scoreEquipo(equipos):
    isScoreEquipo=True
    pj = 0
    pg = 0
    pe = 0
    pp = 0
    gf = 0
    gc = 0
    tp = 0
    equipo = input('Ingrese el nombre del Equipo: ').upper()
    for item in equipos:
        if equipo in item:
            while isScoreEquipo:
                pj += 1
                print('Gano o perdio el partido?')
                result = input('Marque G si ganó, P si perdio y E si quedo empatado: ').upper()
                if result == 'G':
                    pg += 1
                    pe += 0
                    pp += 0
                    tp += 3
                elif result == 'P':
                    pg += 0
                    pe += 0
                    pp += 1 
                    tp += 0   
                else:
                    pg += 0
                    pe += 1
                    pp += 0
                    tp += 1  
                gf += int(input('Ingrese goles marcados: '))
                gc += int(input('Ingrese goles en contra: '))

                results = [pj, pg, pp, pe, gf, gc, tp]
                item[4]=(results)
                os.system("cls")
                print('+','-'*55,'+')
                print("|{:^18}{}{:^18}|".format(' ','PUNTAJE DEL EQUIPO ',' '))
                print('+','-'*55,'+')
                print("| {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} |".format('PJ','PG','PE','PP','GF','GC','TP'))
                print('+','-'*55,'+')
                print("| {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} |".format(item[4][0],item[4][1],item[4][2],item[4][3],item[4][4],item[4][5],item[4][6]))
                print('+','-'*55,'+')

                isScoreEquipo=bool(input("Desea agregar otro Puntaje S(Si) Enter(No)"))

