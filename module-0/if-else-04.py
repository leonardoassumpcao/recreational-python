
# (Code below was automatically generated using if-else-03.py)

def wat():
	N = int(input('Escolha um número de 0 a 7: '))
	print('  # Intervalo inicial [0 <= N <= 7].')

	if N <= 3:
		print('  # Descobrimos  que  [0 <= N <= 3]...')
		if N <= 1:
			print('  # Descobrimos  que  [0 <= N <= 1]...')
			if N <= 0:
				print('# Achamos N = 0!')
			else:
				print('# Achamos N = 1!')
		else:
			print('  # Descobrimos  que  [2 <= N <= 3]...')
			if N <= 2:
				print('# Achamos N = 2!')
			else:
				print('# Achamos N = 3!')
	else:
		print('  # Descobrimos  que  [4 <= N <= 7]...')
		if N <= 5:
			print('  # Descobrimos  que  [4 <= N <= 5]...')
			if N <= 4:
				print('# Achamos N = 4!')
			else:
				print('# Achamos N = 5!')
		else:
			print('  # Descobrimos  que  [6 <= N <= 7]...')
			if N <= 6:
				print('# Achamos N = 6!')
			else:
				print('# Achamos N = 7!')


# Por enquanto, entenda o if abaixo como "se estiver rodando este arquivo diretamente..."
if __name__ == "__main__":
	wat()
