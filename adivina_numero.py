import os
from random import randint

def clear():
	""" Limpia la pantalla  """
	if os.name == 'nt':
		os.system("cls") # sistema operativo windows
	else:
		os.system("clear") # sistema operativo linux

def generar_numero(inferior: int, superior: int) -> int:
	""" Genera un número aleatorio dentro de un intervalo
	
	Parámetros:
		inferior(int): Representa valor inferior del intervalo
		superior(int): Representa valor superior del intervalo

	Returts:
		numero(int): Numero que el usuario deberá adivinar
	"""
	numero = randint(inferior, superior + 1)
	return numero

def mensaje_bienvenida(inferior: int, superior: int, intentos_maximos: int):
	"""  da la bienvenida al usuario mostrando al usuario el objetivo del juego """
	clear()
	print('¡Bienvenido! al juego Adivina el número')
	print('Tu objetivo es adivinar un número entre el {0} y el {1}'.format(inferior, superior))
	print('Dispones de solo {} intentos para conseguirlo'.format(intentos_maximos))
	print('¡Buena suerte!')

def leer_entero():
	""" solicita un valor entero al usuario

	Raises:
		ValueError: entrada no entera
	
	Returns:
		valor(int): El entero ingresado por el usuario
	"""
	while True:
		valor = input()

		try:
			valor = int(valor) 
			return valor       

		except ValueError:
			print('Atencion: Debe ingresar un entero')

def obtener_intento(inferior: int, superior: int) -> int:
	"""Pide al usuario que ingrese un intento
		
	Parameters:
		inferior (int): Representa valor inferior del intervalo
		superior (int): Representa valor superior del intervalo

	Returns:
		valor(int): El intento del usuario
	"""
	while True:
		print('\nIngrese su intento', end=': ')
		valor = leer_entero()

		if valor >= inferior and valor <= superior:
			return valor
		else: 
			print('Atencion: El intento debe estar entre {} y {}'.format(inferior, superior))

def jugarde_nuevo():
	""" Pregunta la usuario si desea jugar de nuevo 
		
	Returns:
		True si la repuesta por el usuario comienza con 's', False en caso contrario
	"""
	repuesta = input('\n¿Desea jugar de nuevo?(si/no): ')
	return repuesta.lower().startswith('s') 

def main():
	""" Función principal del programa """

	INFERIOR = 1          # rango inferior del intervalo en el cual estará el número ha adivinar
	SUPERIOR = 20         # rango superior del intervalo en el cual estará el número ha adivinar
	INTENTOS_MAXIMOS = 5  # número de intentos maximos que tiene el usuario apara adivinar el número secreto

	while True: 

	# --- Fase de inicialización ---

		intentos = 0          # representa el intento actual del usuario
		hecho = False         # determina si la partida debe o no continuar
		usuario_gano = False  # determina si el jugador ha ganado la partida

		numero_secreto = generar_numero(INFERIOR, SUPERIOR)
		mensaje_bienvenida(INFERIOR, SUPERIOR, INTENTOS_MAXIMOS)

	# --- Fase de ejecución ---

		while not hecho and not usuario_gano: 

			print('\nIntentos restantes:', INTENTOS_MAXIMOS - intentos)
			opcion = obtener_intento(INFERIOR, SUPERIOR)

			if opcion > numero_secreto:
				print('\nEl número que ingresaste es alto')
			elif opcion < numero_secreto:
				print('\nEl número que ingresaste es bajo')
			else: 
				usuario_gano = True # El usuario adivinó el número

			intentos += 1 
			hecho = usuario_gano or INTENTOS_MAXIMOS == intentos;

	# --- Fase de finalizacion ---

		if not usuario_gano: 
			print('\nLastima te quedaste sin intentos, el número era:', numero_secreto)
		else:
			print('\nFelicidades adivinaste el número en {} intentos'.format(intentos))

		if not jugarde_nuevo():
			break

	clear()
	print('Gracias por Jugar') 

if __name__ == '__main__':
	main()