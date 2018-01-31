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

class _ListNode(object):

	def __init__(self,item):
		self.item=item
		self.next=None

	def getNode(self):
		return self.item

	def getNext(self):
		return self.next


class Linkedlist:

	#CONSTRUCTORES
	def __init__(self):
		self.primero=None
		self.ultimo=None
		self.size = 0



	#OPERACIONES
############################################################
#OPERACIONES RELATIVAS A LA ENTREGA DE PAQUETES AL MENSAJERO



	def agregar_ordenado(self, item):
		actual = self.primero

		if actual == None:
			nodo = _ListNode(object)
			nodo.item = item
			self.primero = nodo
			self.size +=1
			return

		if actual.item.prioridad > item.prioridad:
			nodo = _ListNode(object)
			nodo.item = item
			self.primero = nodo
			self.size +=1
			return

		while actual.next is not None:
			if actual.next.item.prioridad > item.prioridad:
				break
			actual = actual.next

		nodo = _ListNode(object)
		nodo.item = item
		nodo.next = actual.next
		actual.next = nodo
		self.size +=1
		return


	def quitar_inicio(self):
		aux=_ListNode(object)
		aux=self.primero.item		
		if (self.primero==self.ultimo):
			self.ultimo=None

		self.primero = self.primero.next
		self.size -= 1
		return aux


	def buscar_posicion(self, propiedad):
		i = 1
		aux = self.primero

		if aux != None:
			while aux.next != None:
				if (int(aux.item.capacidad) <= propiedad):

					return i
				aux = aux.next
				i += 1
			if (int(aux.item.capacidad) <= propiedad):

				return i 
		return -1


	def quitar_posicion(self, indice):

		prev = None
		node = self.primero
		i = 0
		while (node != None) and (i < indice-1):
			prev = node
			node = node.next
			i += 1
		if prev == None:
			self.primero = node.next
			self.size -= 1

		else:
			self.size -= 1
			prev.next = node.next



	def obtener_en_posicion(self, indice):
		aux = self.primero

		if indice == 1:


			return self.primero
		elif self.primero.next:
			while (self.primero.next != None) and (indice-1 != 0):
				aux = aux.next
				indice -= 1

			return aux
		else:
			pass



#########################################################################
# OPERACIONES RELATIVAS A LA PILA DE CADA MENSAJERO (ENTREGA DEL PAQUETE)

	def agregar(self,node):
		aux=_ListNode(object)
		aux.item=node
		aux.next=None

		if (self.primero==None):
			self.primero=aux
			self.ultimo=aux

		elif(self.primero!=None):
			self.ultimo.next=aux

		self.ultimo = aux
		self.size += 1


	def quitar_final(self):
		aux =_ListNode(object)
		aux = self.primero
		res = self.ultimo.item
		self.size -= 1
		if (self.ultimo != self.primero):
			while (aux.next != self.ultimo):
					aux= aux.next

			self.ultimo = aux
			self.ultimo.next = None

		elif (self.ultimo == self.primero):
			self.ultimo = None
			self.primero = None
		return res

	def quitar_final2(self):
		aux =_ListNode(object)
		aux = self.primero
		res = self.ultimo
		self.size -= 1
		if (self.ultimo != self.primero):
			while (aux.next != self.ultimo):
					aux= aux.next

			self.ultimo = aux
			self.ultimo.next = None

		elif (self.ultimo == self.primero):
			self.ultimo = None
			self.primero = None
		return res


#########################################################################
# OPERACIONES LIGADAS A LA LISTA "TO DO" IMPRESION DE PAQUETES PENDIENTES 

	def agregar_ordenado_Lista(self, item):
		actual = self.primero

		if actual == None:
			nodo = _ListNode(object)
			nodo.item = item
			self.primero = nodo
			self.size +=1
			return

		if actual.item.destinatario > item.destinatario:
			nodo = _ListNode(object)
			nodo.item = item
			self.primero = nodo
			self.size +=1
			return

		while actual.next is not None:
			if actual.next.item.destinatario > item.destinatario:
				break
			actual = actual.next

		nodo = _ListNode(object)
		nodo.item = item
		nodo.next = actual.next
		actual.next = nodo
		self.size +=1
		return

	def mostrar (self,archivo,info1, info2):
		nodoActual = self.primero
		while nodoActual != None:
			nodoActual.item.show(archivo,info1, info2)
			nodoActual = nodoActual.next

##################################################################
#OPERACIONES VARIAS DE LISTA APLICABLES A LA PILA Y A LA COLA


	def top(self):
		u=self.ultimo
		return(u)


	def first(self):
		p=self.primero.item
		return(p)


	def esVacia(self):
		if (self.tam() ==0):
			ev=True
		else:
			ev=False
		return (ev)


	def tam(self):
		return (self.size)







#casos de prueba previos

"""
lista = Linkedlist()
one = Paquete('p','0','3','5','5')
noe = Paquete('p2','0','5','4','g')
nre= Paquete('p3','0','3','4d','5')
noe2 = Paquete('p2','0','5','4','g')
nre2= Paquete('p3','0','10','4d','5')

lista.agregar(one)
lista.agregar(noe)
lista.agregar(nre)
lista.agregar(noe2)
lista.agregar(nre2)

lista.mostrar()
print(lista.primero.item.capacidad)

print('----',lista.obtener_posicion(3).item.destinatario)
print('>',lista.buscar_posicion(10))

#lista.eliminar_posicion(1)
print('------')
lista.mostrar()
"""