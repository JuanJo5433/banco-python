from os import system
from cuenta import Cuenta
from banco import Banco
from datetime import datetime

class Menu:
	def __init__(self): #Constructor donde se inicializa los objetos de las clases
		self.banco = Banco() 
	def pedir_datos_cuenta(self):
		try:
			system("cls")
			print("**************************")
			print("*****  CREAR CUENTA  *****")
			print("**************************")
			id_titular = input("Digite el numero de docuemento del titular: ")
			nombre_titular = input("Digite el nombre del titular: ")
			num_cuenta = self.banco.generar_numeros_cuentas()
			saldo = int(input("Digite el saldo inicial de la cuenta: "))
			fecha = datetime.now()

			while True:
				print("**************************")
				print("***   TIPO DE CUENTA   ***")
				print("**************************")
				print("1: Ahorros")
				print("2: Corriente")
				print("**************************")

				try:
					op_tipo_cuenta = int(input("Seleccione el tipo de cuenta: "))

					if op_tipo_cuenta == 1:
						tipo_cuenta = "Ahorro"
						cupo = 0
						break

					elif op_tipo_cuenta == 2:
						tipo_cuenta = "Corriente"

						try:
							cupo = float(input("Digite el cupo asignado a la cuenta: "))
							break

						except ValueError:
							print("**************************")
							print("Error - El cupo debe ser numerico")
							print("**************************")
							input()

					else:
						print("**************************")
						print("Error - Opcion no valida debe ser 1 o 2.")
						print("**************************")
						input()

				except ValueError:
					print("**************************")
					print("Error - El dato debe ser entero")
					print("**************************")
					input()

			cuenta = Cuenta(id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo)

			if self.banco.adicionar_cuenta(cuenta):
				print("**************************")
				print("Info - La cuenta se creo correctamente")
				print("El numero de cuenta es: ", num_cuenta)
				print("**************************")
				input()

			else:
				print("**************************")
				print("Error - La cuenta no se puede crear el id del cliente ya existe en el sistema")
				print("**************************")
				input()
		except ValueError:
			print("**************************")
			print("Error -Faltan datos por rellenar")
			print("**************************")
			input()

	def pedir_datos_visualizar_cuenta(self):
		system("cls")
		print("**************************************")
		print("*****      VISUALIZAR CUENTA     *****")
		print("**************************************")
		num_cuenta = int(input("Digite el numero de cuenta: "))
		pos = self.banco.buscar_cuenta(num_cuenta)

		if pos != -1:
			self.banco.visualizar_cuenta(num_cuenta)
			input()

		else:
			print("**************************")
			print("Error - El numero de cuenta no existe")
			print("**************************")
			input()

	def pedir_datos_retiro_cuenta(self):
		system("cls")
		print("*********************************")
		print("*****     RETIROS CUENTA    *****")
		print("*********************************")
		num_cuenta = int(input("Digite el numero de cuenta: "))

		pos = self.banco.buscar_cuenta(num_cuenta)

		if pos != -1:
			if self.banco.tipo_cuenta_cliente(num_cuenta) == 'Ahorro':
				monto = float(input("Digite el monto de retiro: "))
				if self.banco.retirar_monto_cuenta(num_cuenta, monto):
					print("******************************")
					print("Info - El retiro de la cuenta ahorro fue realizado")
					print("******************************")
					input()

				else:
					print("**************************")
					print("Error - El retiro no se puede realizar")
					print("**************************")
					input()
			if pos != -1: 
				if self.banco.tipo_cuenta_cliente(num_cuenta) == 'Corriente':
					monto = float(input("Digite el monto de retiro: "))
					if self.banco.retirar_monto_cuenta_corriente(num_cuenta, monto):
						print("******************************")
						print("Info - El retiro de la cuenta corriente fue realizado")
						print("******************************")
						input()

					else:
						print("**************************")
						print("Error - El retiro no se puede realizar")
						print("**************************")
						input()

		else:
			print("**************************")
			print("Error - El numero de cuenta no existe")
			print("**************************")
			input()

	def pedir_datos_deposito_cuenta(self):
		system("cls")
		print("****************************")
		print("*****     DEPOSITOS    *****")
		print("****************************")
		num_cuenta = int(input("Digite el numero de cuenta: "))
		pos = self.banco.buscar_cuenta(num_cuenta)
		if pos != -1:
			monto = float(input("Digite el monto del deposito: "))
			if self.banco.tipo_cuenta_cliente(num_cuenta) == 'Ahorro':
				if self.banco.deposito_monto_cuenta(monto, num_cuenta):
					print("*********************************")
					print("Info - El deposito fue realizado")
					print("*********************************")
					input()
				else:
					print("****************************************")
					print("Error - El deposito no se puede realizar")
					print("****************************************")
					input()
			if self.banco.tipo_cuenta_cliente(num_cuenta) == 'Corriente':
				if self.banco.deposito_monto_cuenta_corriente(monto, num_cuenta):
					print("*********************************")
					print("Info - El deposito fue realizado")
					print("*********************************")
					input()
				else:
					print("****************************************")
					print("Error - El deposito no se puede realizar")
					print("****************************************")
					input()
		else:
			print("***************************")
			print("Error - La cuenta no existe")
			print("***************************")
			input()

	def mostrar_saldo_cuenta(self):
		system("cls")
		print("********************************")
		print("*****     Mostrar Saldo    *****")
		print("********************************")
	
		num_cuenta = int(input("Digite el numero de cuenta: "))
		pos = self.banco.buscar_cuenta(num_cuenta)
		if pos != -1 and self.banco.tipo_cuenta_cliente(num_cuenta) == 'Ahorro':
			print("*********************************")
			print("Info - El saldo de la cuenta es: $", (self.banco.consultar_saldo_cuenta_ahorro(num_cuenta)))
			print("*********************************")
			input()

		elif pos != -1 and self.banco.tipo_cuenta_cliente(num_cuenta) == 'Corriente':
			print("*********************************")
			self.banco.consultar_saldo_cuenta_corriente(num_cuenta)
			print("*********************************")
			input()

		else:
			print("***************************")
			print("Error - La cuenta no existe")
			print("***************************")
			input()

	def pedir_datos_visualizar_cliente(self):
		system("cls")
		print("************************************")
		print("*****     CONSULTAR CLIENTE    *****")
		print("************************************")
		num_cuenta = int(input("Digite el numero de cuenta: "))
		pos = self.banco.buscar_cuenta(num_cuenta)
		if pos != -1:
			print("*********************************")
			print("Info - El titular de la cuenta es: ", (self.banco.visualizar_cliente(num_cuenta)))
			print("*********************************")
			input()
		else:
			print("***************************")
			print("Error - La cuenta no existe")
			print("***************************")
			input()



	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("**************************")
			print("**************************")
			print("*****      BANCO     *****")
			print("**************************")
			print("1: Crear Cuenta")
			print("2: Visualizar Cuenta")
			print("3: Retiro")
			print("4: Deposito")
			print("5: Consultar saldo")
			print("6: Consultar cliente")
			print("0: Salir")
			print("**************************")

			try:
				opcion = int(input("Digite la opcion: "))
				print("**************************")

				if opcion == 1:
					self.pedir_datos_cuenta()

				elif opcion == 2:
					self.pedir_datos_visualizar_cuenta()
				elif opcion == 3:
					self.pedir_datos_retiro_cuenta()
				elif opcion == 4:
					self.pedir_datos_deposito_cuenta()
				elif opcion == 5:
					self.mostrar_saldo_cuenta()
				elif opcion == 6:
					self.pedir_datos_visualizar_cliente()

				elif opcion == 0:
					print("**************************")
					print("HAZ SALIDO DEL SISTEMA :)")
					print("**************************")
					input()
					break

				else:
					print("**************************")
					print("Error - Opcion no valida")
					print("**************************")
					input()

			except ValueError:
				print("**************************")
				print("Error - El dato debe ser entero")
				print("**************************")
				input()

if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu_principal()
