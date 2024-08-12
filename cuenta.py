class Cuenta:
	def __init__(self, id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo):
		self.__id_titular = id_titular
		self.__nombre_titular = nombre_titular
		self.__numero_cuenta = num_cuenta
		self.__saldo = saldo
		self.__fecha = fecha
		self.__tipo_cuenta = tipo_cuenta
		self.__cupo = cupo
		self.__cupo_original = cupo

	def get_num_cuenta(self): #Entrega informacion
		return self.__numero_cuenta
	def get_id_titular(self):
		return self.__id_titular

	def visualizar(self):
		if self.__tipo_cuenta == 'Ahorro':
			print("El id del titular es: ", self.__id_titular)
			print("El nombre del titular es: ", self.__nombre_titular)
			print("El numer de la cuenta es: ", self.__numero_cuenta)
			print("La fecha de la creacion de la cuenta es: ", self.__fecha)
			print("El tipo de cuenta es: ", self.__tipo_cuenta)
			print("El saldo de la cuenta es: $", self.__saldo)
			print("El cupo de la cuenta es de: $", self.__cupo)
			print("El total disponible es de: $", self.__saldo + self.__cupo)
		else:
			print("El id del titular es: ", self.__id_titular)
			print("El nombre del titular es: ", self.__nombre_titular)
			print("El numer de la cuenta es: ", self.__numero_cuenta)
			print("La fecha de la creacion de la cuenta es: ", self.__fecha)
			print("El tipo de cuenta es: ", self.__tipo_cuenta)
			print("El saldo de la cuenta es: $", self.__saldo)
			if self.__saldo > 0:
				print("El cupo de la cuenta es de: $", self.__cupo)
				print("El total disponible es de: $", self.__saldo + self.__cupo)
			else:
				print("El cupo de la cuenta es de: $", self.__cupo)
				print("El total disponible es de: $", self.__cupo)              


	def retirar(self, monto):
		if self.__saldo - monto >= 0:
			self.__saldo -= monto
			return True
		else:
			return False

	def retirar_corriente(self, monto):
		if self.__saldo > 0:
			if self.__saldo - monto >= 0:
				self.__saldo -= monto
				return True
			elif (self.__saldo +  self.__cupo )  -monto >= 0:
				self.__saldo -= monto
				if self .__saldo < 0:
					self.__cupo += self.__saldo
					return True
			
			return False
		else:
			if  (self.__cupo- monto ) > 0 :
				
				self.__cupo -= monto
				return True
			else:
				return False

	def depositar(self, monto):
		if monto > 0:
			self.__saldo += monto
			return True
		return False

	def depositar_corriente(self, monto):
		if monto > 0:
			if self.__saldo > 0:
				self.__saldo += monto
				return True
			else:
				self.__saldo += monto
				if self.__cupo < self.__cupo_original:
					aux = self.__cupo_original - self.__cupo
					if monto < aux:
						self.__cupo += monto
						return True
					else:
						self.__cupo = self.__cupo_original
				return True
		return False

	def get_saldo(self):    
		return self.__saldo

	def saldo_corriente(self):
		if self.__saldo > 0:
			print("El saldo de la cuenta es: $", self.__saldo)
			print("El cupo de la cuenta es de: $", self.__cupo)
			print("El total disponible es de: $", self.__saldo + self.__cupo)

		else:
			print("El saldo de la cuenta es: $", self.__saldo)
			print("El cupo de la cuenta es de: $", self.__cupo)
			print("El total disponible es de: $", self.__cupo)     

	def get_nombre(self):
		return self.__nombre_titular

	def get_tipo_cuenta(self):
		return self.__tipo_cuenta
