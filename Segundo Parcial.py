import os
import webbrowser
clear = lambda: os.system('cls')

print ("_______________MENU_______________")
print ("Presiona [ 1 ] para digitar datos de estudiantes")
print ("Presione [ 2 ] para modificar notas")
print ("Presione [ 3 ] para mostrar Listado de estudiantes de la sección")
print ("Presione [ 4 ] para consultar estudiente por nombre o matricula")
print ("Presione [ 5 ] para generar tabla HTML")
print ("Presione [ 6 ] para salir")


nombres = []
matriculas = []
edades = []
notaFinal = []


while True:
    
    menu = int(input("Escoja su seleccion: "))

    if menu == 1:
        while True:
            print ("Ingrese el nombre, matricula, edad y nota final de los estudiantes")
            nombres.append(input("nombre: "))
            matriculas.append(input("Matriculas: "))
            edades.append(input("Edad: "))
            notaFinal.append(input("Nota: "))
            if input ("Desea continuar? S/N: ") == "N".casefold(): break
        n1 = int(input("cuantos estudiantes introdujo?  "))
        
    elif menu == 2:
        nota = str(input("Ingrese la nota que desea modificar: "))
        for i in range(n1):
            if nota == notaFinal[i]:
                notaFinal[i] = int(input("ingrese la nueva nota: "))

    elif menu == 3:
        print("{:<15}{:>15}{:>15}{:>15}".format("nombres","matriculas","edades","nota"))
        for i in range(n1):
           print("{:<15}{:>15}{:>13}{:>16}".format(nombres[i],matriculas[i],edades[i],notaFinal[i]))

    elif menu == 4:
        bus=int(input("Desea buscar un estudiante por el nombre [1] o por la matricula[2]: "))
        if bus == 1:
            bus1 = str(input("Intruduzca el nombre del estudiante que desea consultar: "))
            for i in range(n1):
                if bus1 == nombres[i]:
                    print("{:<15}{:>15}{:>15}{:>15}".format("nombre","matricula","edad","nota final"))
                    print("{:<15}{:>15}{:>13}{:>16}".format(nombres[i],matriculas[i],edades[i],notaFinal[i]))
                else:
                    print("El nombre que introdujo no se encuentra en la lista")
        if bus == 2:
            busm = str(input("Intruduzca la matricula del estudiante que desea consultar: "))
            for i in range(n1):
                if busm == matriculas[i]:
                    print("{:<15}{:>15}{:>15}{:>15}".format("nombre","matricula","edad","nota final"))
                    print("{:<15}{:>15}{:>13}{:>16}".format(nombres[i],matriculas[i],edades[i],notaFinal[i]))
                else:
                    print("La matricula que introdujo no se encuentra en la lista")
        
    elif menu == 5:
        Registro = open('tablaAlumnos.html', 'w')
        estrutura = """<!DOCTYPE html>
        <html lang="es" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title>Keury Lendof</title>
          </head>
          <style type="text/css">
              table, th, td {
              border: 1px solid black;
              border-collapse: collapse;;
              }
              
              th, td {
              padding: 10px;
              }
          </style>
          <body style="background-color: #FFFFFF;">
            <div align = "center" style= "font 100% times calibri;">
            <h1> Tabla de Alumnos <h1>
            <hr/>
            <br/>
            </div>
            <table style="width: 100%">
            <tr>
                <th>
                    Nombres
                </th>
                <th>
                    Matriculas
                </th>
                <th>
                    Edades
                </th>
                <th>
                    Nota Final
                </th>
            </tr>"""
        Registro.write(estrutura)
        
        for i in range(n1):
            estrutura1= """
                      <tr>
                            <td>{0}""".format(nombres[i]) + """</td>
                            <td>{0}""".format(matriculas[i]) + """</td>
                            <td>{0}""".format(edades[i]) + """</td>
                            <td>{0}""".format(notaFinal[i]) + """</td>
                      </tr>"""
            Registro.write(estrutura1)

            estructura2= """
                </table>
                </body>
                </html> """
        Registro.write(estructura2)
        Registro.close()
        
      
    else:
        print("Numero fuera de rango, revise nuevamente el menu de opciones")

