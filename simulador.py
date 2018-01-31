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
from mensajero import Mensajero
from pila import _Pila
from cola import _Cola 
import sys
import os
import copy

class Simulador:

	def __init__(self):
		self.cola_de_prioridades = _Cola()
		self._mensajero1 = Mensajero(1, archivo_salida)
		self._mensajero2 = Mensajero(2, archivo_salida)
		self._mensajero3 = Mensajero(3, archivo_salida)
		self._mensajero4 = Mensajero(4, archivo_salida)
		self._Tiempo = 1
		self._capacidad = 1024

###############################################################################
#ESTA FUNCION SE ENCARGA DE LLAMAR AL PROCEDIMIENTO DE LECTURA UBICADO EN EL
#ARCHIVO COLA, LEE EL ARCHIVO, CREA PAQUETES Y LAS CARGA ORDENADAS EN LA COLA
	def Leer(self, archivo_entrada):
		self.cola_de_prioridades.LECTURA(archivo_entrada)



###############################################################################
#ESTA FUNCION ES EL CICLO DE LLAMADOS EN EL CUAL SE EJECUTARAN TODAS LAS ACCIONES
#DEL SIMULADOR
	def Tiempo(self):

#dadas las condiciones de que la cola y los mensajeros no son vacios
		cond0 = self._mensajero1.No_Tiene_paquetes()
		cond1 = self._mensajero2.No_Tiene_paquetes()
		cond2 = self._mensajero3.No_Tiene_paquetes()
		cond3 = self._mensajero4.No_Tiene_paquetes()
		cond4 = self.cola_de_prioridades.No_Tiene_paquetes()

	#el contador de Tiempo continua hasta que Pilas y colas vacias esten
		while (not cond0 or not cond1 or not cond2  \
			or not cond3 or not cond4):

		#mientras los mensajeros esten ociosos 
			while cond0 or cond1 or cond2 or cond3:

				if cond0 and self.cola_de_prioridades.Cola_prioridades.buscar_posicion(self._capacidad) >= 0:

					disponibilidad = self._capacidad
					paquetes = self.cola_de_prioridades.desencolar(disponibilidad)
					self._mensajero1.tomar_carga(paquetes,self._Tiempo)
					valor = int(self._mensajero1.paquetesEmpilados.ultimo().item.capacidad)
					self.disponibilidad_(valor)



				elif cond1 and self.cola_de_prioridades.Cola_prioridades.buscar_posicion(self._capacidad) >= 0:

					disponibilidad = self._capacidad
					paquetes = self.cola_de_prioridades.desencolar(disponibilidad)
					self._mensajero2.tomar_carga(paquetes,self._Tiempo)
					valor = int(self._mensajero2.paquetesEmpilados.ultimo().item.capacidad)
					self.disponibilidad_(valor)


				elif cond2 and self.cola_de_prioridades.Cola_prioridades.buscar_posicion(self._capacidad) >= 0:
					disponibilidad = self._capacidad
					paquetes = self.cola_de_prioridades.desencolar(disponibilidad)
					self._mensajero3.tomar_carga(paquetes,self._Tiempo)
					valor = int(self._mensajero3.paquetesEmpilados.ultimo().item.capacidad)
					self.disponibilidad_(valor)



				elif cond3 and self.cola_de_prioridades.Cola_prioridades.buscar_posicion(self._capacidad) >= 0:

					disponibilidad = self._capacidad
					paquetes = self.cola_de_prioridades.desencolar(disponibilidad)
					self._mensajero4.tomar_carga(paquetes,self._Tiempo)
					valor = int(self._mensajero4.paquetesEmpilados.ultimo().item.capacidad)
					self.disponibilidad_(valor)


				else:
					break


				cond0 = self._mensajero1.No_Tiene_paquetes()
				cond1 = self._mensajero2.No_Tiene_paquetes()
				cond2 = self._mensajero3.No_Tiene_paquetes()
				cond3 = self._mensajero4.No_Tiene_paquetes()
				cond4 = self.cola_de_prioridades.No_Tiene_paquetes()

			#aqui llamo a la funcion Lista para realizar la escritura del archivo
			#cada 100 unidades de tiempo
			self.Lista(self._Tiempo)


		#aqui inicia el proceso de entrega, dentro de la clase Paquete asigne una variable para almacenar
		#los tiempos iniciales de cada paquete y sub paquetes, y el proceso de entrega inicia cuando
		#el tiempo del simulador menos el tiempo inicio corresponde al campo duracion del paquete.
		#cada mensajero recibe las ordenes por separado
			if  not cond0:

				if self._mensajero1.paquetesEmpilados.ultimo().item.tiempo_inicial!= -1:
					if int(self._Tiempo) - int(self._mensajero1.paquetesEmpilados.ultimo().item.tiempo_inicial) == \
							int(self._mensajero1.paquetesEmpilados.ultimo().item.duracion)-1:
						n = self._mensajero1.entrega_fin(self._Tiempo)
						self._capacidad = self._capacidad + int(n)
						cond0 = self._mensajero1.No_Tiene_paquetes()
					else:
						pass
				elif self._mensajero1.paquetesEmpilados.ultimo().item.tiempo_inicial == -1:
					nombre = self._mensajero1.paquetesEmpilados.ultimo().item.destinatario
					self._mensajero1.ESCRIBIR_INICIANDO(archivo_salida,self._Tiempo, nombre, 1)
					self._mensajero1.paquetesEmpilados.ultimo().item.tiempo_inicial = self._Tiempo
				else:
					pass
			else:
				pass


			if not cond1:

				if self._mensajero2.paquetesEmpilados.ultimo().item.tiempo_inicial!= -1:
					if int(self._Tiempo) - int(self._mensajero2.paquetesEmpilados.ultimo().item.tiempo_inicial) == \
							int(self._mensajero2.paquetesEmpilados.ultimo().item.duracion)-1:
		
						n = self._mensajero2.entrega_fin(self._Tiempo)
						self._capacidad = self._capacidad + int(n)
						cond1 = self._mensajero2.No_Tiene_paquetes()

					else:
						pass
				elif self._mensajero2.paquetesEmpilados.ultimo().item.tiempo_inicial == -1:
					self._mensajero2.paquetesEmpilados.ultimo().item.tiempo_inicial = self._Tiempo
				else:
					pass
			else:
				pass

			if not cond2:

				if self._mensajero3.paquetesEmpilados.ultimo().item.tiempo_inicial!= -1:
					if int(self._Tiempo) - int(self._mensajero3.paquetesEmpilados.ultimo().item.tiempo_inicial) == \
							int(self._mensajero3.paquetesEmpilados.ultimo().item.duracion)-1:
		
						n = self._mensajero3.entrega_fin(self._Tiempo)
						self._capacidad = self._capacidad + int(n)
						cond2 = self._mensajero3.No_Tiene_paquetes()
					else:
						pass
				elif self._mensajero3.paquetesEmpilados.ultimo().item.tiempo_inicial == -1:
					self._mensajero3.paquetesEmpilados.ultimo().item.tiempo_inicial = self._Tiempo
				else:
					pass
			else:
				pass

			if not cond3:
				if self._mensajero4.paquetesEmpilados.ultimo().item.tiempo_inicial!= -1:
					if int(self._Tiempo) - int(self._mensajero4.paquetesEmpilados.ultimo().item.tiempo_inicial) == \
							int(self._mensajero4.paquetesEmpilados.ultimo().item.duracion)-1 :
		
						n = self._mensajero4.entrega_fin(self._Tiempo)
						self._capacidad = self._capacidad + int(n)
						cond3 = self._mensajero4.No_Tiene_paquetes()
					else:
						pass
				elif self._mensajero4.paquetesEmpilados.ultimo().item.tiempo_inicial == -1:
					self._mensajero4.paquetesEmpilados.ultimo().item.tiempo_inicial = self._Tiempo
				else:
					pass
			else:
				pass

		#actualizo las capacidades de mis 5 listas enlazadas
			cond0 = self._mensajero1.No_Tiene_paquetes()
			cond1 = self._mensajero2.No_Tiene_paquetes()
			cond2 = self._mensajero3.No_Tiene_paquetes()
			cond3 = self._mensajero4.No_Tiene_paquetes()
			cond4 = self.cola_de_prioridades.No_Tiene_paquetes()

			#si todas las listas del simulador estan vacias, se imprime
			#Fin y termina el programa
			if (cond0 and cond1 and cond2 and cond3 and cond4):
				arch = open(archivo_salida,'a')
				arch.write(str(self._Tiempo+1) + ' ' + 'Fin')
			else:
				pass


			self._Tiempo += 1

###############################################################################
#FUNCION QUE ES UTILIZADA PARA RESTAR LA CAPACIDAD AL SIMULADOR CADA VEZ QUE
#UN PAQUETE PASA A LAS MANOS DE UN MENSAJERO
	def disponibilidad_(self, valor=0):
		self._capacidad = self._capacidad - valor


###############################################################################
#FUNCION QUE SE ENCARGA DE IMPRIMIR EL LISTADO DE PAQUETES PENDIENTES CADA
#100 UNIDADES DE TIEMPO, COLECTA CADA PAQUETE EN LAS 5 LISTAS ENLAZADAS, Y LAS
#COLOCA EN UNA LISTA PARA LUEGO DE ORDENARLAS ALFABETICAMENTE, SEAN ESCRITAS EN
#EL ARCHIVO DE SALIDA
	def Lista(self, tiempo):

		if (tiempo % 100 == 0):

			sal_list = open(archivo_salida,'a')
			linea = str(self._Tiempo) + ' Listado'
			sal_list.write(linea+'\n')
			linea = []
		#por cada mensajero hay una pila que por medio de la funcion obten_paquete, retornara el objeto
		#asociado a cada nodo y lo pondra en la lista
			if not self._mensajero1.No_Tiene_paquetes():
				card = self._mensajero1.tam_carga()
				while card != 0:
					linea.append(str(self._mensajero1.paquetesEmpilados.obten_paquete(card).item.destinatario)+' '+\
						str(self._mensajero1.paquetesEmpilados.obten_paquete(card).item.prioridad) + ' ' +\
						str(self._mensajero1.paquetesEmpilados.obten_paquete(card).item.capacidad)+' '+\
						str(self._mensajero1.paquetesEmpilados.obten_paquete(card).item.duracion)+' mensajero '+\
						str(self._mensajero1.identificador))
					card -= 1

			if not self._mensajero2.No_Tiene_paquetes():
				card = self._mensajero2.tam_carga()
				while card != 0:
					linea.append(str(self._mensajero2.paquetesEmpilados.obten_paquete(card).item.destinatario)+' '+\
						str(self._mensajero2.paquetesEmpilados.obten_paquete(card).item.prioridad) + ' ' +\
						str(self._mensajero2.paquetesEmpilados.obten_paquete(card).item.capacidad)+' '+\
						str(self._mensajero2.paquetesEmpilados.obten_paquete(card).item.duracion)+' mensajero '+\
						str(self._mensajero2.identificador))
					card -= 1

			if not self._mensajero3.No_Tiene_paquetes():
				card = self._mensajero3.tam_carga()
				while card != 0:
					linea.append(str(self._mensajero3.paquetesEmpilados.obten_paquete(card).item.destinatario)+' '+\
						str(self._mensajero3.paquetesEmpilados.obten_paquete(card).item.prioridad) + ' ' +\
						str(self._mensajero3.paquetesEmpilados.obten_paquete(card).item.capacidad)+' '+\
						str(self._mensajero3.paquetesEmpilados.obten_paquete(card).item.duracion)+' mensajero '+\
						str(self._mensajero3.identificador))
					card -= 1

			if not self._mensajero4.No_Tiene_paquetes():
				card = self._mensajero4.tam_carga()
				while card != 0:
					linea.append(str(self._mensajero4.paquetesEmpilados.obten_paquete(card).item.destinatario)+' '+\
						str(self._mensajero4.paquetesEmpilados.obten_paquete(card).item.prioridad) + ' ' +\
						str(self._mensajero4.paquetesEmpilados.obten_paquete(card).item.capacidad)+' '+\
						str(self._mensajero4.paquetesEmpilados.obten_paquete(card).item.duracion)+' mensajero '+\
						str(self._mensajero4.identificador))
					card -= 1


		#analogamente con la cola, toma toda la informacion referente a paquetes que contenga
		#el nodo y lo pondra en la lista para luego ser impreso en el archivo de salida

			if not self.cola_de_prioridades.No_Tiene_paquetes():
				card2 = self.cola_de_prioridades.Tamanio_cola()
				while card2 != 0:

					linea.append(str(self.cola_de_prioridades.obten_paquete(card2).item.destinatario)+' '+\
						str(self.cola_de_prioridades.obten_paquete(card2).item.prioridad) + ' ' +\
						str(self.cola_de_prioridades.obten_paquete(card2).item.capacidad)+' '+\
						str(self.cola_de_prioridades.obten_paquete(card2).item.duracion)+' Cola de prioridades')
					card2 -=1
		#llamado a la funcion de ordenamiento por insercion para ordenar alfabeticamente
		#la lista y enviarla a la escritura
			self.insertion_sort(linea)

			for i in range(len(linea)):
				sal_list.write(linea[i]+'\n')
				sal_list.closed
			sal_list.write('Fin listado'+'\n')

###############################################################################
#FUNCION DE ORDENAMIENTO, UTILIZADA PARA ORDENAR DE FORMA ALFABETICA LA LISTA
#EN LA CUAL SE ESCRIBIRAN LOS PAQUETES PENDIENTES
	def insertion_sort(self,lista):
		for i in range(1,len(lista)):
			j = i - 1 
			clave = lista[i]
			while (clave < lista[j]) and (j >= 0):
				lista[j+1] = lista[j]
				j -= 1
			lista[j+1] = clave




########################################################################################
#																					   #
######                            GLOBAL PROGRAM                                  ######
#																					   #
########################################################################################



def parseArgs(args): 
#comprueba si se estan metiendo justamente 2 parametros en el terminal

    msg = "Error en la linea de comando:\nsimulador.py <arch_entrada> <arch_salida>"
    if len(args) != 3:
        print(msg)
        sys.exit(1)

    return str(args[1]), str(args[2])



if __name__=="__main__":

	archivo_entrada,archivo_salida = parseArgs(sys.argv)
	if os.path.exists(archivo_salida):
		os.remove(archivo_salida)

	simulador = Simulador()
	simulador.Leer(archivo_entrada)
	simulador.Tiempo()
