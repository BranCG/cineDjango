from django.shortcuts import render
from django.http import HttpResponse





boletos_reservados = []
def asiento_disponible(asiento, pelicula, horario):
    for boleto in boletos_reservados:
        if boleto["asiento"] == asiento and boleto["pelicula"] == pelicula and boleto["horario"] == horario:
            return False
    return True

HORARIOS = ["12:00", "16:00", "20:00", "00:00"]

PELICULAS = [
    {"titulo": "Alien Romulus 1", "sala": "Sala 1", "horarios": HORARIOS},
    {"titulo": "Intensamente 2", "sala": "Sala 2", "horarios": HORARIOS},
    {"titulo": "DeadPool & Wolverine", "sala": "Sala 3", "horarios": HORARIOS},
]

ASIENTOS = []
filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for fila in filas:
    for columna in range(1, 11):
        ASIENTOS.append(f"{fila}{columna}")
print(ASIENTOS)

#FUNCION PARA VALIDAR QUE ESTE EL ASIENTO DISPONIBBLE
def validar_asiento(asiento):
    return asiento in ASIENTOS

def crear_boleto(request):
    try:
        nombre = str(input("Nombre: "))
        rut = int(input("RUT: "))

        print("Películas disponibles:")
        for idx, pelicula in enumerate(PELICULAS):
            print(f"{idx + 1}: {pelicula['titulo']} - {pelicula['sala']}")

        pelicula_idx = int(input("Seleccione la película (número): ")) - 1
        pelicula_seleccionada = PELICULAS[pelicula_idx]

        print("Horarios disponibles:")
        for idx, horario in enumerate(HORARIOS):
            print(f"{idx + 1}: {horario}")

        horario_idx = int(input("Seleccione el horario (número): ")) - 1
        horario_seleccionado = HORARIOS[horario_idx]
            
        asientos_disponibles = []
        for asiento in ASIENTOS:
            if asiento_disponible(asiento, pelicula_seleccionada, horario_seleccionado):
                asientos_disponibles.append(asiento)
        
        print("Asientos disponibles:")
        for asiento in asientos_disponibles:
            print(asiento , end=" ")
        print()

        asiento = str(input("Seleccione el asiento: ").upper())
        if not validar_asiento(asiento):
            return HttpResponse("Asiento no válido.", status=400)
        if asiento not in asientos_disponibles:
            return HttpResponse("Asiento no disponible.", status=400)
       
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    else:
        print("Boleto generado con exito, vaya a la web!")
        boleto = {
            "nombre": nombre,
            "rut": rut,
            "asiento": asiento,
            "pelicula": pelicula_seleccionada,
            "horario": horario_seleccionado
        }
        boletos_reservados.append(boleto)
            

    respuesta = f"""
    <html>
    <body>
        <h1>Boleto generado</h1>
        <p>Nombre: {nombre}</p>
        <p>RUT: {rut}</p>
        <p>Asiento: {asiento}</p>
        <p>Película: {pelicula_seleccionada['titulo']} - {pelicula_seleccionada['sala']} - Horario: {horario_seleccionado}</p>
    </body>
    </html>
    """
    
    return HttpResponse(respuesta)

