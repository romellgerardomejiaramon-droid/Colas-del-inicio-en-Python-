import time

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

def crear_lista_ejemplo():
    print("\n--- Cargando lista de ejemplo ---")
    p = Nodo("García")
    p.liga = Nodo("Pérez")
    p.liga.liga = Nodo("López")
    p.liga.liga.liga = Nodo("Santos")
    p.liga.liga.liga.liga = Nodo("Martínez")
    return p

def inserta_inicio(p, dato):
    q = Nodo(dato)
    q.liga = p
    return q

def inserta_final(p, dato):
    if p is None:
        return Nodo(dato)
    t = p
    while t.liga is not None:
        t = t.liga
    q = Nodo(dato)
    q.liga = None
    t.liga = q
    return p

def inserta_por_posicion(p, pos, dato):
    if pos < 1:
        print("Posición inválida.")
        return p

    actual = p
    longitud = 0
    while actual is not None:
        longitud += 1
        actual = actual.liga

    while longitud < pos - 1:
        p = inserta_final(p, "VACÍO")
        longitud += 1

    if pos == 1:
        return inserta_inicio(p, dato)
    
    if pos == longitud + 1:
        return inserta_final(p, dato)

    actual = p
    for _ in range(1, pos - 1):
        actual = actual.liga

    nuevo = Nodo(dato)
    nuevo.liga = actual.liga
    actual.liga = nuevo
    return p

def apuntar_dos_a_uno(p, val1, val2, val_objetivo):
    nodo1 = None
    nodo2 = None
    nodo_obj = None
    
    actual = p
    while actual is not None:
        if actual.info == val1 and nodo1 is None:
            nodo1 = actual
        if actual.info == val2 and nodo2 is None and actual != nodo1:
            nodo2 = actual
        if actual.info == val_objetivo and nodo_obj is None:
            nodo_obj = actual
        actual = actual.liga
        
    if nodo1 and nodo2 and nodo_obj:
        nodo1.liga = nodo_obj
        nodo2.liga = nodo_obj
        print(f"¡Listo! Los nodos '{val1}' y '{val2}' ahora apuntan al nodo '{val_objetivo}'.")
    else:
        print("No se encontraron todos los nodos especificados en la lista.")
    return p

def elimina_inicio(p):
    if p is None:
        print("La lista está vacía.")
        return None
    q = p
    p = q.liga
    return p

def elimina_ultimo(p):
    if p is None:
        print("La lista está vacía.")
        return None
    if p.liga is None:
        return None
    q = p
    t = None
    while q.liga is not None:
        t = q
        q = q.liga
    t.liga = None
    return p

def elimina_x(p, x):
    if p is None:
        print("La lista está vacía.")
        return p
    q = p
    band = 1
    t = None
    while (q.info != x) and (band == 1):
        if q.liga is not None:
            t = q
            q = q.liga
        else:
            band = 0
            
    if band == 0:
        print("El elemento no se encuentra en la lista.")
    else:
        if p == q:
            p = q.liga
        else:
            t.liga = q.liga
    return p

def busqueda_desordenada(p, x):
    q = p
    pos = 1
    encontrado = False
    while q is not None:
        if q.info == x:
            print(f"¡Elemento encontrado en la fila/posición {pos}!")
            encontrado = True
        q = q.liga
        pos += 1
    if not encontrado:
        print("El elemento no se encuentra en la lista.")

def imprimir_lista(p):
    actual = p
    print("Lista actual: ", end="")
    while actual is not None:
        print(f"[{actual.info}]", end=" -> ")
        actual = actual.liga
    print("FIN")

if __name__ == "__main__":
    print("¿Cómo desea inicializar el programa?")
    print("1. Cargar lista de ejemplo (García -> Pérez -> López -> Santos -> Martínez)")
    print("2. Crear lista desde cero")
    op_creacion = int(input("Seleccione una opción: "))
    
    if op_creacion == 1:
        p = crear_lista_ejemplo()
    else:
        print("1. Creación al inicio")
        print("2. Creación al final")
        sub_op = int(input("Seleccione forma de creación: "))
        if sub_op == 1:
            info_inicial = input("Ingrese el valor para el primer nodo: ")
            p = Nodo(info_inicial)
            p.liga = None
            res = int(input("¿Desea ingresar más nodos al inicio? Sí: 1, No: 0: "))
            while res == 1:
                q = Nodo(input("Ingrese el valor: "))
                q.liga = p
                p = q
                res = int(input("¿Desea ingresar más nodos? Sí: 1, No: 0: "))
        else:
            info_inicial = input("Ingrese el valor para el primer nodo: ")
            p = Nodo(info_inicial)
            p.liga = None
            res = int(input("¿Desea ingresar más nodos al final? Sí: 1, No: 0: "))
            while res == 1:
                q = Nodo(input("Ingrese el valor: "))
                q.liga = None
                t = p
                while t.liga is not None:
                    t = t.liga
                t.liga = q
                res = int(input("¿Desea ingresar más nodos? Sí: 1, No: 0: "))
                
    imprimir_lista(p)
    
    while True:
        print("\n--- Menú Principal de Operaciones ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Insertar en una fila específica (rellena con VACÍO los huecos)")
        print("4. Hacer que dos nodos apunten a un nodo común")
        print("5. Eliminar el primer nodo")
        print("6. Eliminar el último nodo")
        print("7. Eliminar un nodo con información X")
        print("8. Buscar un elemento")
        print("9. Mostrar lista")
        print("10. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        # Medir tiempo de inicio de la operación
        inicio_tiempo = time.perf_counter()
        
        if opcion == 1:
            dato = input("Ingrese el valor a insertar: ")
            p = inserta_inicio(p, dato)
            imprimir_lista(p)
        elif opcion == 2:
            dato = input("Ingrese el valor a insertar: ")
            p = inserta_final(p, dato)
            imprimir_lista(p)
        elif opcion == 3:
            pos = int(input("Ingrese el número de fila donde desea insertar: "))
            dato = input("Ingrese el valor del nuevo nodo: ")
            p = inserta_por_posicion(p, pos, dato)
            imprimir_lista(p)
        elif opcion == 4:
            v1 = input("Ingrese el valor del primer nodo origen: ")
            v2 = input("Ingrese el valor del segundo nodo origen: ")
            v_obj = input("Ingrese el valor del nodo destino común: ")
            p = apuntar_dos_a_uno(p, v1, v2, v_obj)
            imprimir_lista(p)
        elif opcion == 5:
            p = elimina_inicio(p)
            imprimir_lista(p)
        elif opcion == 6:
            p = elimina_ultimo(p)
            imprimir_lista(p)
        elif opcion == 7:
            x = input("Ingrese el valor (X) del nodo que desea eliminar: ")
            p = elimina_x(p, x)
            imprimir_lista(p)
        elif opcion == 8:
            x = input("Ingrese el valor que desea buscar: ")
            busqueda_desordenada(p, x)
        elif opcion == 9:
            imprimir_lista(p)
        elif opcion == 10:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
            
        # Medir tiempo final y calcular la diferencia
        fin_tiempo = time.perf_counter()
        tiempo_total = (fin_tiempo - inicio_tiempo) * 1000 # Convertir a milisegundos
        
        if opcion != 10:
            print(f" [Tiempo de ejecución: {tiempo_total:.4f} ms]")
