
# class Tarea:
#     def __init__(self, descripcion, prioridad):
#         self.descripcion = descripcion
#         self.prioridad = prioridad
#         self.completada = False
#         self.siguiente = None


# class ListaTareas:
#     def __init__(self):
#         self.cabeza = None


#     def esta_vacia(self):
#         return self.cabeza is None


#     def agregar(self, descripcion, prioridad):
#         nueva = Tarea(descripcion, prioridad)
#         self.cabeza = self._agregar_rec(self.cabeza, nueva)


#     def _agregar_rec(self, actual, nueva):

#         # insertar al inicio
#         if actual is None or nueva.prioridad > actual.prioridad:
#             nueva.siguiente = actual
#             return nueva

#         actual.siguiente = self._agregar_rec(
#             actual.siguiente, nueva
#         )

#         return actual




#     def mostrar(self):
#         actual = self.cabeza

#         while actual:
#             estado = "✓" if actual.completada else "○"
#             print(f"[{estado}] {actual.descripcion} (P{actual.prioridad})")
#             actual = actual.siguiente



#     def completar(self, descripcion):
#         actual = self.cabeza

#         while actual:
#             if actual.descripcion == descripcion:
#                 actual.completada = True
#                 print("Tarea completada")
#                 return
#             actual = actual.siguiente

#         print("Tarea no encontrada")



#     def contar_pendientes(self, prioridad):
#         return self._contar_rec(self.cabeza, prioridad)


#     def _contar_rec(self, nodo, prioridad):

#         if nodo is None:
#             return 0

#         contador = 0

#         if nodo.prioridad == prioridad and not nodo.completada:
#             contador = 1

#         return contador + self._contar_rec(
#             nodo.siguiente, prioridad
#         )



#     def obtener_urgentes(self):
#         nueva_lista = ListaTareas()
#         self._urgentes_rec(self.cabeza, nueva_lista)
#         return nueva_lista


#     def _urgentes_rec(self, nodo, nueva_lista):

#         if nodo is None:
#             return

#         if nodo.prioridad >= 4 and not nodo.completada:
#             nueva_lista.agregar(
#                 nodo.descripcion,
#                 nodo.prioridad
#             )

#         self._urgentes_rec(
#             nodo.siguiente,
#             nueva_lista
#         )




#     def limpiar_completadas(self):
#         self.cabeza = self._limpiar_rec(self.cabeza)


#     def _limpiar_rec(self, nodo):

#         if nodo is None:
#             return None

#         nodo.siguiente = self._limpiar_rec(
#             nodo.siguiente
#         )

#         if nodo.completada:
#             return nodo.siguiente

#         return nodo
    


# if __name__ == "__main__":
#     lista = ListaTareas()
#     lista.agregar("Comprar leche", 3)
#     lista.agregar("Pagar facturas", 5)
#     lista.agregar("Llamar a mamá", 4)
#     lista.agregar("Hacer ejercicio", 2)

#     print("Lista de tareas:")
#     lista.mostrar()

#     print("\nContar pendientes de prioridad 4:", lista.contar_pendientes(4))

#     urgentes = lista.obtener_urgentes()
#     print("\nTareas urgentes:")
#     urgentes.mostrar()

#     lista.completar("Pagar facturas")
#     print("\nLista después de completar 'Pagar facturas':")
#     lista.mostrar()

#     lista.limpiar_completadas()
#     print("\nLista después de limpiar completadas:")
#     lista.mostrar()

""""------------------------------------------------------------------------"""

"""
══════════════════════════════════════════════════════
        SISTEMA HISTORIAL DE NAVEGADOR
══════════════════════════════════════════════════════
"""

# ═════════════════════════════════════
# PUNTO 1a: Clase Nodo (Pagina)
# ═════════════════════════════════════

class Pagina:
    def __init__(self, url, titulo, tiempo):
        self.url = url
        self.titulo = titulo
        self.tiempo = tiempo
        self.siguiente = None


# ═════════════════════════════════════
# PUNTO 1b: Clase Lista (Historial)
# ═════════════════════════════════════

class Historial:
    def __init__(self):
        self.cabeza = None


    def esta_vacia(self):
        return self.cabeza is None


# ═════════════════════════════════════
# PUNTO 2: AGREGAR PÁGINA O(1)
# ═════════════════════════════════════

    def visitar(self, url, titulo, tiempo):
        nueva = Pagina(url, titulo, tiempo)

        # insertar al inicio
        nueva.siguiente = self.cabeza
        self.cabeza = nueva


# ═════════════════════════════════════
# MOSTRAR HISTORIAL
# ═════════════════════════════════════

    def mostrar(self):
        actual = self.cabeza

        while actual:
            print(f"{actual.titulo} | {actual.url} | {actual.tiempo}s")
            actual = actual.siguiente


# ═════════════════════════════════════
# PUNTO 3: TIEMPO TOTAL (RECURSIVO)
# ═════════════════════════════════════

    def tiempo_total(self):
        return self._tiempo_total_rec(self.cabeza)


    def _tiempo_total_rec(self, nodo):

        if nodo is None:
            return 0

        return nodo.tiempo + self._tiempo_total_rec(
            nodo.siguiente
        )


# ═════════════════════════════════════
# PUNTO 4: BUSCAR POR DOMINIO (RECURSIVO)
# ═════════════════════════════════════

    def buscar_por_dominio(self, texto):
        nueva_lista = Historial()
        self._buscar_rec(self.cabeza, texto, nueva_lista)
        return nueva_lista


    def _buscar_rec(self, nodo, texto, nueva_lista):

        if nodo is None:
            return

        if texto in nodo.url:
            nueva_lista.visitar(
                nodo.url,
                nodo.titulo,
                nodo.tiempo
            )

        self._buscar_rec(
            nodo.siguiente,
            texto,
            nueva_lista
        )


# ═════════════════════════════════════
# PUNTO 5: ELIMINAR PÁGINAS RÁPIDAS
# ═════════════════════════════════════

    def eliminar_rapidas(self, tiempo_min):
        self.cabeza = self._eliminar_rec(
            self.cabeza,
            tiempo_min
        )


    def _eliminar_rec(self, nodo, tiempo_min):

        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_rec(
            nodo.siguiente,
            tiempo_min
        )

        if nodo.tiempo < tiempo_min:
            return nodo.siguiente

        return nodo
    
if __name__ == "__main__":
    historial = Historial()
    historial.visitar("https://www.google.com", "Google", 5)
    historial.visitar("https://www.facebook.com", "Facebook", 10)
    historial.visitar("https://www.youtube.com", "YouTube", 3)
    historial.visitar("https://www.twitter.com", "Twitter", 8)

    print("Historial completo:")
    historial.mostrar()

    print("\nTiempo total de navegación:", historial.tiempo_total(), "s")

    dominio = "google"
    print(f"\nPáginas que contienen '{dominio}':")
    resultado = historial.buscar_por_dominio(dominio)
    resultado.mostrar()

    tiempo_min = 6
    historial.eliminar_rapidas(tiempo_min)
    print(f"\nHistorial después de eliminar páginas con tiempo < {tiempo_min}s:")
    historial.mostrar()