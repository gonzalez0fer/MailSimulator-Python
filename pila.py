##############################################################################
#         ..--""|															 #
#         |     |                 _____ _                 __  __       _ _   #
#         | .---'                / ____(_)               |  \/  |     (_) |  #
#   (\-.--| |---------.         | (___  _ _ __ ___ ______| \  / | __ _ _| |  #
#  / \) \ | |          \         \___ \| | '_ ` _ \______| |\/| |/ _` | | |  #
#  |:.  | | |           |        ____) | | | | | | |     | |  | | (_| | | |  #
#  |:.  | |o|           |       |_____/|_|_| |_| |_|     |_|  |_|\__,_|_|_|  #
#  |:.  | `"`           |													 #
#  |:.  |_ __  __ _  __ /		Integrantes: Fernando Gonzalez 08-10464		 #
#  `""""`""|=`|"""""""`						 Bruno Colmenares 12-10551       #
#          |=_|					Laboratorios de Algoritmos II Grupo 9		 #
#          |= |																 #
##############################################################################


from paquete import Paquete
from listagen import Linkedlist
from listagen import _ListNode

class _Pila:

	def __init__(self):
		self._Pila = Linkedlist()


###############################################################################
#FUNCION QUE TIENE COMO PARAMETRO DE ENTRADA EL PAQUETE Y LO EMPILA EN 
#EL MENSAJERO
	def empilar(self, paquete):
		self._Pila.agregar(paquete)



###############################################################################
#FUNCION QUE SE ENCARGA DE DESEMPILAR (ENTREGAR) EL PAQUETE Y ES LA QUE
#DEFINE EL FINAL DEL PROGRAMA AL ENTREGAR TODOS LOS PAQUETES DEL SIMULADOR		
	def desempilar(self):
		self._Pila.quitar_final()


###############################################################################
#FUNCION QUE RETORNA EL ULTIMO (TOPE) PAQUETE EMPILADO EN EL MENSAJERO SE
#UTILIZA PARA CONDICIONALES EN EL SIMULADOR
	def ultimo(self):
		return self._Pila.top()


###############################################################################
#FUNCION QUE RETORNA EL NUMERO DE PAQUETES EMPILADOS SE USA EN EL MENSAJERO
#PARA SABER SI TIENE SUBPAQUETES, YA QUE SOLO PUEDE LLEVAR UN PAQUETE
	def tamanio(self):
		return self._Pila.tam()


###############################################################################
#SIRVE PARA IMPRIMIR EN EL ARCHIVO DE SALIDA TODOS LOS PAQUETES PENDIENTES DE
#ENTREGAR
	def ver_pila(self,archivo,info1,info2):
		self._Pila.mostrar(archivo,info1,info2)


###############################################################################
#RETORNA UN BOOLEAN SI EL MENSAJERO TIENE O NO TIENE PAQUETES
	def vacia(self):
		return self._Pila.esVacia()


	def obten_paquete(self,valor):
		return self._Pila.obtener_en_posicion(valor)



		


