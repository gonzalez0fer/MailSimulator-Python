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
from pila import _Pila

class Mensajero:

	def __init__(self, etiquetador,salida):
		self.identificador = etiquetador
		self.paquetesEmpilados = _Pila()
		self.archivo_sal = salida

###############################################################################
#FUNCION EN LA CUAL EL MENSAJERO TOMA EL PAQUETE DE LA COLA DE PRIORIDADES
#Y SE DISPONE A LA ENTREGA, SI EL PAQUETE TIENE SUBPAQUETES, LOS CREA Y LOS
#EMPILA EN EL MENSAJERO
	def tomar_carga(self,paquete, Tiempo_):
		tiempo_ini = Tiempo_
		aux = int(paquete.subpaquetes)
		aux2 = paquete.destinatario
		aux3 = paquete.prioridad
		aux4 = paquete.duracion
		cartero = self.identificador

		if aux == 0:

			self.ESCRIBIR_INICIANDO (self.archivo_sal,tiempo_ini, aux2, cartero)
			if paquete.tiempo_inicial == 0:
				paquete.tiempo_inicial = tiempo_ini
			else:
				pass
			self.paquetesEmpilados.empilar(paquete)

		else:
			if paquete.tiempo_inicial == 0:
				paquete.tiempo_inicial = tiempo_ini
			else:
				pass
			self.ESCRIBIR_SUBPAQUETE (self.archivo_sal,tiempo_ini, aux2, aux, cartero)
			while aux != 0:
				sub = aux2 + '-' + str(aux-1)
				j = Paquete(sub, aux3, 0, aux4, 0)
				if j.tiempo_inicial == 0:
					j.tiempo_inicial = -1
				else:
					pass
				self.paquetesEmpilados.empilar(j)
				aux -= 1

			self.ESCRIBIR_INICIANDO (self.archivo_sal,tiempo_ini, aux2, cartero)
			self.paquetesEmpilados.empilar(paquete)

###############################################################################
#FUNCION EN LA CUAL EL CARTERO DESEMPILA EL PAQUETE FINALIZANDO LA ENTREGA 
#Y RETORNA EL VALOR DE LA CAPACIDAD DEL PAQUETE PARA LIBERAR CAPACIDAD 
#EN EL SIMULADOR
	def entrega_fin(self, Tiempo_):
		mensajero = self.identificador
		j = self.paquetesEmpilados.ultimo().item.capacidad
		nombre = self.paquetesEmpilados.ultimo().item.destinatario
		tiempo = Tiempo_
		self.paquetesEmpilados.desempilar()
		self.ESCRIBIR_FINALIZANDO (self.archivo_sal, tiempo, nombre, mensajero)
		return j



###############################################################################
#FUNCION QUE RETORNA UN BOOLEAN SI EL MENSAJERO ESTA SIN PAQUETES AL SIMULADOR 
#UTILIZADA PARA PARA CONDICIONALES
	def No_Tiene_paquetes(self):
		return self.paquetesEmpilados.vacia()



###############################################################################
#RETORNA LA CAPACIDAD DEL PAQUETE QUE TIENE EMPILADO AL TOPE  AL MENSAJERO
#PARA CONDICIONALES EN EL SIMULADOR
	def _capacidad_carga(self):
		cond = self.No_Tiene_paquetes()
		if cond:
			a = 0
		else:
			a = self.paquetesEmpilados.ultimo().item.capacidad
		return int(a) 



###############################################################################
#RETORNA EL NUMERO DEL PAQUETE MAS SUBPAQUETES (SI EXISTEN) EMPILADOS
# EN EL MENSAJERO
	def tam_carga(self):
		return self.paquetesEmpilados.tamanio()


###############################################################################
#RETORNA EL OBJETO TIPO PAQUETE EN LA POSICION QUE SE LE SOLICITA SE UTILIZA 
#PARA LA IMPRESION DE LA LISTA
	def obten_paquete(self,valor):
		return self.paquetesEmpilados.obtener_paquete(valor)

###############################################################################
###############################################################################
#PROCEDIMIENTOS RELATIVOS A LA IMPRESION DEL ARCHIVO DE SALIDA


	def ESCRIBIR_INICIANDO (self,archivo_salida,tiempo, nombre, mensajero): 
	#hace la escritura de la inicializacion de la entrega de los paquetes
		arch = open(archivo_salida,'a')
		arch.write(str(tiempo) + ' ' + 'Iniciando paquete' + ' ' + str(nombre) + ' ' + \
			'por el mensajero ' + str(mensajero) + '.'+ '\n')
		arch.close()

	def ESCRIBIR_SUBPAQUETE (self,archivo_salida,tiempo, nombre, numero, mensajero): 
	#hace la escritura de la inicializacion de la entrega de los paquetes
		arch = open(archivo_salida,'a')
		arch.write(str(tiempo) + ' ' + 'Empilando' + ' ' + str(numero)+ ' ' + \
			'subpaquetes del paquete' + ' ' + str(nombre) +' ' +\
			'en el mensajero ' + str(mensajero) +'.'+ '\n')
		arch.close()

	def ESCRIBIR_FINALIZANDO (self,archivo_salida, tiempo, nombre, mensajero):
	#hace la escritura de la finalizacion de los paquetes
		arch = open(archivo_salida,'a')
		arch.write(str(tiempo) + ' ' + 'Finalizando paquete' + ' ' + str(nombre) + ' ' + \
			'por el mensajero ' + str(mensajero) +'.'+ '\n')
		arch.close()



