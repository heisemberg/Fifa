import equipos
import os

if __name__ == "__main__":
    teams =[]
    isAddTeam = True
    while isAddTeam:
        os.system("cls")
        print("1.Registrar equipo\n2.Mostrar Equipos\n3.Registro de jugadores\n4.Registro de cuerpo tecnico\n5.Registro de medico\n6.Mostrar entrenador de equipos\n7.Registrar puntajes de equipo")
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                equipos.addEquipo(teams)
            elif opcion == 2:
                os.system("cls")
                print(teams)
                input("Presione cualquier tecla para continuar")
            elif opcion == 3:
                equipos.addPlayer(teams)
            elif opcion == 4:
                equipos.addTecnico(teams)
            elif opcion == 5:
                equipos.addMedico(teams)
            elif opcion == 6:
                equipos.showEntrenador(teams)
            else:
                equipos.scoreEquipo(teams)
        except Exception:
            isAddTeam= bool(input("Desea continuar en el programa S(Si) o Enter(No) :"))