# Code below was intended to be shared at http://foruns.rf.gd/ufrj/viewtopic.php?f=12&t=8 ;
# The idea is to recreationally produce a brute force "binary search".
# The output is a python program (?) with the sole purpose of guessing an integer.
# This is intended as an if-else exercise for novices.

def bisect(i_min=0, i_max=15, tabs=1):
	if tabs == 1:
		print("def wat():")
		print("\tN = int(input('Escolha um número de {} a {}: '))".format(i_min, i_max))
		print("\tprint('  # Intervalo inicial [{} <= N <= {}].')\n".format(i_min, i_max))

	if i_min == i_max:
		print("\t" * tabs + "print('# Achamos N = {}!')".format(i_min))
		return None

	else:
		midpoint = (i_min + i_max) // 2
		print("\t" * tabs + "if N <= {}:".format(midpoint))
		if i_min >= midpoint:
			print("\t" * (tabs+1) + "print('# Achamos N = {}!')".format(i_min))
		else:
			print("\t" * (tabs+1) + "print('  # Descobrimos  que  [{} <= N <= {}]...')".format(i_min, midpoint))
			bisect(i_min, midpoint, tabs+1)

		midpoint += 1
		print("\t" * tabs + "else:")
		if i_max <= midpoint:
			return print("\t" * (tabs+1) + "print('# Achamos N = {}!')".format(i_max))
		else:
			print("\t" * (tabs+1) + "print('  # Descobrimos  que  [{} <= N <= {}]...')".format(midpoint, i_max))
			bisect(midpoint, i_max, tabs+1)


if __name__ == "__main__":
	bisect(i_max=7)
