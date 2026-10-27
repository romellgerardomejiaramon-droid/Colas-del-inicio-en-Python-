import time
import tkinter as tk
from tkinter import messagebox, simpledialog

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class MyLinkedList:
    def __init__(self):
        self.cabeza = None

    def crear_lista_ejemplo(self):
        self.cabeza = Nodo("García")
        self.cabeza.liga = Nodo("Pérez")
        self.cabeza.liga.liga = Nodo("López")
        self.cabeza.liga.liga.liga = Nodo("Santos")
        self.cabeza.liga.liga.liga.liga = Nodo("Martínez")
        return self.cabeza

    def inserta_inicio(self, dato):
        q = Nodo(dato)
        q.liga = self.cabeza
        self.cabeza = q
        return self.cabeza

    def inserta_final(self, dato):
        if self.cabeza is None:
            self.cabeza = Nodo(dato)
            return self.cabeza
        t = self.cabeza
        while t.liga is not None:
            t = t.liga
        q = Nodo(dato)
        q.liga = None
        t.liga = q
        return self.cabeza

    def inserta_por_posicion(self, pos, dato):
        if pos < 1:
            return False, "Posición inválida."

        actual = self.cabeza
        longitud = 0
        while actual is not None:
            longitud += 1
            actual = actual.liga

        # Rellenar con "VACÍO" si la posición está más adelante
        while longitud < pos - 1:
            self.inserta_final("VACÍO")
            longitud += 1

        if pos == 1:
            self.inserta_inicio(dato)
            return True, f"Nodo '{dato}' insertado en la posición {pos}."
        
        if pos == longitud + 1:
            self.inserta_final(dato)
            return True, f"Nodo '{dato}' insertado en la posición {pos}."

        actual = self.cabeza
        for _ in range(1, pos - 1):
            actual = actual.liga

        nuevo = Nodo(dato)
        nuevo.liga = actual.liga
        actual.liga = nuevo
        return True, f"Nodo '{dato}' insertado en la posición {pos}."

    def editar_por_posicion(self, pos, nuevo_valor):
        if pos < 1:
            return False, "Posición inválida."
        
        actual = self.cabeza
        actual_pos = 1
        while actual is not None and actual_pos < pos:
            actual = actual.liga
            actual_pos += 1
            
        if actual is not None:
            valor_anterior = actual.info
            actual.info = nuevo_valor
            return True, f"Fila {pos} (antes '{valor_anterior}') actualizada a '{nuevo_valor}'."
        else:
            return False, f"La posición {pos} está fuera del rango de la lista."

    def apuntar_dos_a_uno(self, val1, val2, val_objetivo):
        nodo1 = None
        nodo2 = None
        nodo_obj = None
        
        actual = self.cabeza
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
            return True, f"Nodos '{val1}' y '{val2}' apuntan a '{val_objetivo}'."
        else:
            return False, "No se encontraron todos los nodos especificados."

    def elimina_inicio(self):
        if self.cabeza is None:
            return False, "La lista está vacía."
        self.cabeza = self.cabeza.liga
        return True, "Primer nodo eliminado."

    def elimina_ultimo(self):
        if self.cabeza is None:
            return False, "La lista está vacía."
        if self.cabeza.liga is None:
            self.cabeza = None
            return True, "Último nodo eliminado."
        q = self.cabeza
        t = None
        while q.liga is not None:
            t = q
            q = q.liga
        t.liga = None
        return True, "Último nodo eliminado."

    def elimina_x(self, x):
        if self.cabeza is None:
            return False, "La lista está vacía."
        q = self.cabeza
        band = 1
        t = None
        while (q.info != x) and (band == 1):
            if q.liga is not None:
                t = q
                q = q.liga
            else:
                band = 0
                
        if band == 0:
            return False, "El elemento no se encuentra en la lista."
        else:
            if self.cabeza == q:
                self.cabeza = q.liga
            else:
                t.liga = q.liga
            return True, f"Nodo '{x}' eliminado."

    def busqueda_desordenada(self, x):
        q = self.cabeza
        pos = 1
        while q is not None:
            if q.info == x:
                return True, f"Elemento encontrado en la posición {pos}."
            q = q.liga
            pos += 1
        return False, "El elemento no se encuentra en la lista."

# --- INTERFAZ GRÁFICA (GUI) ---
class AppMyLinkedList:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca MyLinkedList - Entorno Gráfico")
        self.root.geometry("950x720")
        self.root.config(bg="#f0f2f5")

        self.lista = MyLinkedList()
        self.pedir_inicio_seguro()

        self.crear_widgets()
        self.dibujar_lista()

    def pedir_inicio_seguro(self):
        top = tk.Toplevel(self.root)
        top.title("Inicialización de MyLinkedList")
        top.geometry("400x220")
        top.config(bg="#1e293b")
        top.transient(self.root)
        top.grab_set()

        top.update_idletasks()
        x = (top.winfo_screenwidth() - top.winfo_reqwidth()) / 2
        y = (top.winfo_screenheight() - top.winfo_reqheight()) / 2
        top.geometry(f"+{int(x)}+{int(y)}")

        lbl = tk.Label(top, text="¿Cómo desea iniciar el programa?", font=("Arial", 12, "bold"), bg="#1e293b", fg="white", pady=15)
        lbl.pack()

        def elegir(tipo):
            if tipo == 1:
                self.lista.crear_lista_ejemplo()
            else:
                self.lista.cabeza = None
            top.destroy()

        btn_ejemplo = tk.Button(top, text="1. Cargar Lista de Ejemplo", command=lambda: elegir(1), bg="#3b82f6", fg="white", font=("Arial", 10, "bold"), width=30, pady=8)
        btn_ejemplo.pack(pady=5)

        btn_vacia = tk.Button(top, text="2. Iniciar Lista Vacía (Crear desde cero)", command=lambda: elegir(2), bg="#10b981", fg="white", font=("Arial", 10, "bold"), width=30, pady=8)
        btn_vacia.pack(pady=5)

        top.protocol("WM_DELETE_WINDOW", lambda: elegir(2))
        self.root.wait_window(top)

    def crear_widgets(self):
        titulo = tk.Label(self.root, text="Gestor Gráfico de Listas Ligadas (MyLinkedList)", font=("Arial", 16, "bold"), bg="#1e293b", fg="white", pady=12)
        titulo.pack(fill=tk.X)

        canvas_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.GROOVE)
        canvas_frame.pack(pady=15, padx=20, fill=tk.X)

        lbl_canvas = tk.Label(canvas_frame, text="Representación Gráfica de la Estructura:", font=("Arial", 10, "bold"), bg="white", anchor="w")
        lbl_canvas.pack(fill=tk.X, padx=10, pady=5)

        self.canvas = tk.Canvas(canvas_frame, height=120, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill=tk.X, padx=10, pady=5)

        panel_control = tk.LabelFrame(self.root, text=" Funciones de la Biblioteca MyLinkedList ", font=("Arial", 11, "bold"), bg="#f0f2f5", fg="#1e293b", padx=15, pady=15)
        panel_control.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

        btn_ini = tk.Button(panel_control, text="Insertar al Inicio", command=self.cmd_insertar_inicio, bg="#3b82f6", fg="white", font=("Arial", 10, "bold"), width=25)
        btn_ini.grid(row=0, column=0, padx=8, pady=8)

        btn_fin = tk.Button(panel_control, text="Insertar al Final", command=self.cmd_insertar_final, bg="#3b82f6", fg="white", font=("Arial", 10, "bold"), width=25)
        btn_fin.grid(row=0, column=1, padx=8, pady=8)

        btn_pos = tk.Button(panel_control, text="Insertar en Posición / Fila", command=self.cmd_insertar_pos, bg="#2563eb", fg="white", font=("Arial", 10, "bold"), width=28)
        btn_pos.grid(row=0, column=2, padx=8, pady=8)

        # BOTÓN DE EDITAR POR POSICIÓN (IDEAL PARA RELLENAR VACÍOS)
        btn_editar = tk.Button(panel_control, text="Editar Nodo por Fila", command=self.cmd_editar, bg="#d97706", fg="white", font=("Arial", 10, "bold"), width=25)
        btn_editar.grid(row=1, column=0, padx=8, pady=8)

        btn_apuntar = tk.Button(panel_control, text="Apuntar Dos a Uno (Op. 4)", command=self.cmd_apuntar, bg="#8b5cf6", fg="white", font=("Arial", 10, "bold"), width=25)
        btn_apuntar.grid(row=1, column=1, padx=8, pady=8)

        btn_buscar = tk.Button(panel_control, text="Buscar Elemento", command=self.cmd_buscar, bg="#10b981", fg="white", font=("Arial", 10, "bold"), width=28)
        btn_buscar.grid(row=1, column=2, padx=8, pady=8)

        btn_reset = tk.Button(panel_control, text="Reiniciar / Limpiar Lista", command=self.cmd_reiniciar, bg="#64748b", fg="white", font=("Arial", 10, "bold"), width=25)
        btn_reset.grid(row=2, column=0, padx=8, pady=8)

        btn_del_ini = tk.Button(panel_control, text="Eliminar Primer Nodo", command=self.cmd_eliminar_inicio, bg="#ef4444", fg="white", font=("Arial", 10, "bold"), width=25)
        btn_del_ini.grid(row=2, column=1, padx=8, pady=8)

        btn_del_fin = tk.Button(panel_control, text="Eliminar Último Nodo", command=self.cmd_eliminar_fin, bg="#ef4444", fg="white", font=("Arial", 10, "bold"), width=28)
        btn_del_fin.grid(row=2, column=2, padx=8, pady=8)

        btn_del_x = tk.Button(panel_control, text="Eliminar por Valor (X)", command=self.cmd_eliminar_x, bg="#dc2626", fg="white", font=("Arial", 10, "bold"), width=25)
        btn_del_x.grid(row=3, column=1, padx=8, pady=8)

        self.log_text = tk.Text(self.root, height=5, font=("Consolas", 9), bg="#0f172a", fg="#38ef7d", padx=10, pady=10)
        self.log_text.pack(fill=tk.X, padx=20, pady=15)
        self.log_text.insert(tk.END, ">>> Sistema MyLinkedList Gráfico inicializado correctamente.\n")

    def dibujar_lista(self):
        self.canvas.delete("all")
        actual = self.lista.cabeza
        x, y = 40, 35
        ancho_nodo, alto_nodo = 85, 45

        if actual is None:
            self.canvas.create_text(450, 60, text="[ LISTA VACÍA ] - Ingrese nodos usando el menú de botones", font=("Arial", 11, "bold"), fill="#64748b")
            return

        while actual is not None:
            color_bg = "#fef08a" if actual.info == "VACÍO" else "#38bdf8"
            
            self.canvas.create_rectangle(x, y, x + ancho_nodo, y + alto_nodo, fill=color_bg, outline="#0f172a", width=2)
            self.canvas.create_text(x + ancho_nodo/2, y + alto_nodo/2, text=str(actual.info), font=("Arial", 9, "bold"), fill="#0f172a")

            if actual.liga is not None:
                self.canvas.create_line(x + ancho_nodo, y + alto_nodo/2, x + ancho_nodo + 35, y + alto_nodo/2, arrow=tk.LAST, width=2, fill="#475569")
            
            x += ancho_nodo + 35
            actual = actual.liga

        self.canvas.create_text(x + 15, y + alto_nodo/2, text="FIN", font=("Arial", 11, "bold"), fill="#ef4444")

    def registrar_log(self, mensaje, tiempo):
        log_msg = f"[{time.strftime('%H:%M:%S')}] {mensaje}  ➔  ⏱️ Tiempo: {tiempo:.4f} ms\n"
        self.log_text.insert(tk.END, log_msg)
        self.log_text.see(tk.END)

    def cmd_insertar_inicio(self):
        dato = simpledialog.askstring("Insertar al inicio", "Ingrese el valor del nuevo nodo:", parent=self.root)
        if not dato:
            return
        inicio = time.perf_counter()
        self.lista.inserta_inicio(dato)
        fin = time.perf_counter()
        self.dibujar_lista()
        self.registrar_log(f"Insertado '{dato}' al inicio.", (fin - inicio) * 1000)

    def cmd_insertar_final(self):
        dato = simpledialog.askstring("Insertar al final", "Ingrese el valor del nuevo nodo:", parent=self.root)
        if not dato:
            return
        inicio = time.perf_counter()
        self.lista.inserta_final(dato)
        fin = time.perf_counter()
        self.dibujar_lista()
        self.registrar_log(f"Insertado '{dato}' al final.", (fin - inicio) * 1000)

    def cmd_insertar_pos(self):
        dato = simpledialog.askstring("Insertar por posición", "Ingrese el valor del nodo:", parent=self.root)
        if dato is None:
            return
        
        pos_str = simpledialog.askstring("Insertar por posición", "Ingrese el número de fila/posición:", parent=self.root)
        if pos_str is None or not pos_str.isdigit():
            return
        
        pos = int(pos_str)
        inicio = time.perf_counter()
        _, msg = self.lista.inserta_por_posicion(pos, dato)
        fin = time.perf_counter()
        self.dibujar_lista()
        self.registrar_log(msg, (fin - inicio) * 1000)

    def cmd_editar(self):
        # Primero pide la fila/posición del nodo a editar (sea VACÍO u otro valor)
        pos_str = simpledialog.askstring("Editar por Fila", "Ingrese el número de fila/posición del nodo que desea editar:", parent=self.root)
        if pos_str is None or not pos_str.isdigit():
            return
        
        # Después pide el nuevo valor
        nuevo_valor = simpledialog.askstring("Editar por Fila", "Ingrese el nuevo valor para este nodo:", parent=self.root)
        if nuevo_valor is None:
            return
        
        pos = int(pos_str)
        inicio = time.perf_counter()
        _, msg = self.lista.editar_por_posicion(pos, nuevo_valor)
        fin = time.perf_counter()
        self.dibujar_lista()
        self.registrar_log(msg, (fin - inicio) * 1000)

    def cmd_apuntar(self):
        v1 = simpledialog.askstring("Apuntar 2 a 1", "Valor del primer nodo origen:", parent=self.root)
        if v1 is None: return
        v2 = simpledialog.askstring("Apuntar 2 a 1", "Valor del segundo nodo origen:", parent=self.root)
        if v2 is None: return
        v_obj = simpledialog.askstring("Apuntar 2 a 1", "Valor del nodo destino común:", parent=self.root)
        if v_obj is None: return

        inicio = time.perf_counter()
        _, msg = self.lista.apuntar_dos_a_uno(v1, v2, v_obj)
        fin = time.perf_counter()
        self.dibujar_lista()
        self.registrar_log(msg, (fin - inicio) * 1000)

    def cmd_buscar(self):
        x = simpledialog.askstring("Buscar", "Ingrese el valor que desea buscar:", parent=self.root)
        if x is None: 
            return
        inicio = time.perf_counter()
        _, msg = self.lista.busqueda_desordenada(x)
        fin = time.perf_counter()
        self.registrar_log(msg, (fin - inicio) * 1000)
        messagebox.showinfo("Resultado de Búsqueda", msg, parent=self.root)

    def cmd_reiniciar(self):
        self.pedir_inicio_seguro()
        inicio = time.perf_counter()
        fin = time.perf_counter()
        self.dibujar_lista()
        self.registrar_log("Lista reiniciada / actualizada.", (fin - inicio) * 1000)

    def cmd_eliminar_inicio(self):
        inicio = time.perf_counter()
        _, msg = self.lista.elimina_inicio()
        fin = time.perf_counter()
        self.dibujar_lista()
        self.registrar_log(msg, (fin - inicio) * 1000)

    def cmd_eliminar_fin(self):
        inicio = time.perf_counter()
        _, msg = self.lista.elimina_ultimo()
        fin = time.perf_counter()
        self.dibujar_lista()
        self.registrar_log(msg, (fin - inicio) * 1000)

    def cmd_eliminar_x(self):
        x = simpledialog.askstring("Eliminar por valor", "Ingrese el valor (X) a eliminar:", parent=self.root)
        if x is None: 
            return
        inicio = time.perf_counter()
        _, msg = self.lista.elimina_x(x)
        fin = time.perf_counter()
        self.dibujar_lista()
        self.registrar_log(msg, (fin - inicio) * 1000)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMyLinkedList(root)
    root.mainloop()
