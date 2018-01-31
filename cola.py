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

class _Cola:

	def __init__(self):
		self.Cola_prioridades = Linkedlist()

##############################################################################
#ESTE METODO SE ENCARGA DE LEER EL ARCHIVO DE ENTRADA CON LA CARGA DE PAQUETES
#POR MEDIO DEL SIMULADOR, Y LOS ORDENA EN UNA COLA DE PRIORIDADES INICIALIZADA
#EN EL SIMULADOR

	def LECTURA (self, archivo):

		arch = open(archivo,'r')
		linea = arch.readline()
		lista = linea.split()

		while (linea !=""):

			if lista != []:

				if (lista[0] == 'paquete'):
					objeto = Paquete(lista[1], lista[2], lista[3],\
					 lista[4], lista[5])

					if (self.Cola_prioridades.tam() == 0):

						self.Cola_prioridades.agregar(objeto)

					elif self.Cola_prioridades.tam()!= 0:
						nuevo_nodo = _ListNode(object)
						nuevo_nodo.item  = objeto
						nuevo_nodo.next = None

						primer = self.Cola_prioridades.primero
						self.Cola_prioridades.agregar_ordenado(objeto)

					else:
						pass
				else:

					pass
			else:
				pass
			linea = arch.readline()
			lista = linea.split()


##############################################################################
#ESTA FUNCION SE ENCARGA DE DESENCOLAR Y RETORNAR EL ELEMENTO QUE SEA MENOR
#O IGUAL A LA CAPACIDAD DISPONIBLE EN EL SIMULADOR PARA ASIGNARLO AL MENSAJERO
	def desencolar(self, posicion=1):

		j = (self.Cola_prioridades.buscar_posicion(posicion))
		n = (self.Cola_prioridades.obtener_en_posicion(j).item)
		self.Cola_prioridades.quitar_posicion(j)
		return(n)



###############################################################################
#ESTA FUNCION ES UTILIZADA PARA LA IMPRESION DE LA LISTA QUE ES PUESTA CADA
# T MOD 100 = 0 
	def Ver_cola(self,archivo,info1,info2):
		self.Cola_prioridades.mostrar(archivo, info1, info2)


###############################################################################
#ESTA FUNCION ES UTILIZADA PARA RETORNAR UN BOOLEAN EN CASO DE COLA VACIA
#UTILIZADA PARA CONDICIONALES DE TIEMPO Y MANEJO DE PAQUETES EN SIMULADOR
	def No_Tiene_paquetes(self):
		return self.Cola_prioridades.esVacia()


################################################################################
#REGRESA EL TAMAÑO DE LA COLA, UTILIZADA PARA CONDICIONALES
	def Tamanio_cola(self):
		return self.Cola_prioridades.size


################################################################################
#REGRESA LA CAPACIDAD DEL ELEMENTO QUE ESTA DE PRIMERO EN LA COLA
	def Primer(self):
		return self.Cola_prioridades.first().capacidad

	def obten_paquete(self,valor):
		return self.Cola_prioridades.obtener_en_posicion(valor)




#d= _Cola()
#d.LECTURA('in')
#d.Cola_prioridades.mostrar()
#print(d.Cola_prioridades.tam())