# Playing with Fibonacci
# http://foruns.rf.gd/ufrj/viewtopic.php?f=13&t=10

def fibonacci(N):
	"""
	Calcula o termo N da sequência de Fibonacci usando um laço de repetição.
	F(1) = F(2) = 1; F(3) = F(2) + F(1); F(4) = F(3) + F(2), e assim por diante!
	"""
	if N <= 2:
		return 1 if (N > 0) else 0  # Convenção: F(0) = 0. Costumam começar do F(1)

	# Para avançar na sequência, só precisamos lembrar de dois consecutivos:
	a, b = 1, 1  # (isso é uma dupla atribuição)
	for i in range(N-2):
		anterior = a
		a = b
		b += anterior  # ("a, b = b, a+b" também funcionaria)

	return b


def fibonacci_lenta(N):
	"""Calcula recursivamente o termo N da sequência de Fibonacci."""
	# Essa função funciona, porém, é mais lenta (imagina o porquê?).
	# Lançaremos um erro se tentarem calcular com N > 33:
	assert N <= 33, "Essa função é muito lenta, testar apenas com N <= 33!"

	if N <= 2:
		# Para uma função recursiva não executar infinitamente,
		# precisamos cuidar dos casos iniciais manualmente, geralmente com um if:
		return 1 if (N > 0) else 0

	else:
		# A própria definição da sequência é recursiva:
		return fibonacci_lenta(N-1) + fibonacci_lenta(N-2)


def demo_function(func):
	"""Dada a função func fornecida, exibimos func(k) para cada k em range(7)."""
	# Funções são objetos: podemos passar uma função como parâmetro sem problemas
	nome = func.__name__  # (func.__name__ é o nome da função; ex: "fibonacci")
	print("Primeiros valores da função {}:".format(nome))

	for k in range(7):
		print("| {}({}) == {}".format(nome, k, func(k)))
	print()


if __name__ == "__main__":
	from time import time  # vamos cronometrar algumas coisas :>

	demo_function(fibonacci)
	demo_function(fibonacci_lenta)

	print("Comparação do tempo de execução (tempos em ms):")
	N = 25

	# Calculamos a diferença dos tempos do sistema antes e depois da execução:
	t1 = -1 * time()
	print("[fibonacci normal] resultado:", fibonacci(N), end=";  ")
	t1 += time()
	t1 *= 1000
	print("tempo: {:.6f}".format(t1))  # "{:.6f}" é pra exibir 6 casas decimais!

	t2 = -1 * time()
	print("[fibonacci lenta ] resultado:", fibonacci_lenta(N), end=";  ")
	t2 += time()
	t2 *= 1000
	print("tempo: {:.6f}".format(t2))

	print("\nfibonacci({}) é {:.2f} vezes mais rápida!".format(N, t2 / t1))

