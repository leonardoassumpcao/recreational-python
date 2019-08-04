# Neste programa vamos exercitar:
# abs, max, input, operadores ternários, str.format, str.repr
# definição de funções, valor padrão em funções, como documentar uma função.

def obter_idade(texto=None):
	"""
	Solicitamos a idade do usuário com a função input.
	A propósito, isso daqui é a docstring da função, cuja finalidade em geral
	é explicar o que ela faz! Para consultar a documentação de qualquer função,
	use help(nome_da_função) no interpretador, ou faça print(nome_da_função.__doc__)
	Pra sair do help, em geral é a tecla "q".
	"""
	print("# Função obter_idade() acaba de ser chamada!")

	if texto is None:
		texto = "Favor informar sua idade: "

	# Em Python 3, input() retorna uma string; então convertemos pra int:
	idade = int(input(texto))
	print()  # (dando um Enter pra ficar bonito e tal)
	return idade


def comparar_duas_idades():
	"""
	O usuário deve informar a idade de duas pessoas muito específicas;
	Retorna-se uma string informando o nome e idade da pessoa mais velha.
	"""
	kleber_wilson = obter_idade("Idade de Kleber Wilson: ")
	maria_josefina = obter_idade("Idade de Maria Josefina: ")

	# Operador ternário (valor_se_verdadeiro if condição else valor_se_falso):
	mais_velho = ("Kleber" if maria_josefina < kleber_wilson else "Maria")

	dd = abs(maria_josefina - kleber_wilson)  # (módulo da diferença)

	if kleber_wilson < maria_josefina:
		print("Maria é mais velha por {} anos!\n".format(dd))

	elif kleber_wilson > maria_josefina:
		print("Kleber é mais velho por {} anos!\n".format(dd))

	else:
		print("Maria e Kleber têm a mesma idade!\n")
		return "Maria e Kleber têm {} anos".format(maria_josefina)
		# Ao retornar um valor, a execução da função termina!
		# Ou seja, se entrarmos nesse else, as linhas abaixo não executam.

	maior_idade = max(maria_josefina, kleber_wilson)
	return "{} tem {} anos".format(mais_velho, maior_idade)


# Sempre que um script Python é executado diretamente ao invés de ser importado,
#   uma variável __name__ recebe o valor "__main__".
# Assim, o if abaixo não será executado quando fizerem "import functions_01"!
# A ideia é que quem for importar não gostaria de ficar testando o módulo,
#   mas tão somente usar os objetos aqui definidos (funções, constantes etc).

if __name__ == "__main__":
	resultado = comparar_duas_idades()

	print("Chamamos comparar_duas_idades() e o valor de retorno foi este:")
	print(repr(resultado))  # repr dá uma representação printável de um objeto.
	# Confira sobre repr(x) em https://docs.python.org/3/library/functions.html

