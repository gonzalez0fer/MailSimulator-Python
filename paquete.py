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


class Paquete:
#Clase Paquete, la cual se utilizara como info asociada al nodo de la lista
#enlazada generica

	def __init__(self, destinatario, prioridad, capacidad, duracion, subpaquetes, \
		tiempo_inicial = 0):
		self.destinatario = destinatario
		self.prioridad = prioridad
		self.capacidad = capacidad
		self.duracion = duracion
		self.subpaquetes = subpaquetes
		self.tiempo_inicial = tiempo_inicial

###############################################################################
#FUNCION PARA LA IMPRESION DE LOS PAQUETES DENTRO DE LA LISTA
	def show(self, archivo, de_cola, de_pila):
		b = de_cola
		if b == -1:
			arch = open(archivo,'a')
			arch.write(str(self.destinatario) + ' '  + str(self.prioridad) \
			+' ' + str(self.capacidad) + ' '+ str(self.duracion) +' '+ str(de_pila) \
			+ '\n')
			
			arch.close()
		else:
			pass
		if b != -1:
			arch = open(archivo,'a')
			arch.write(str(self.destinatario) + ' '  + str(self.prioridad) \
			+' ' + str(self.capacidad) + ' '+ str(self.duracion) +' '+ str(de_cola)\
			 + '\n')

			arch.close()
		else:
			pass

