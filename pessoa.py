class Pessoa:
	
	__slots__ = ['_nome', '_sobrenome', '_cpf', '_email', '_telefone', '_endereco']

	def __init__(self, nome, sobrenome, cpf, email, telefone, endereco=None):
		self._nome = nome
		self._sobrenome = sobrenome
		self._cpf = cpf
		self._email = email
		self._telefone = telefone
		self._endereco = endereco

	@property
	def nome(self):
		return self._nome

	@property
	def sobrenome(self):
		return self._sobrenome

	@property
	def cpf(self):
		return self._cpf

	@property
	def email(self):
		return self._email

	@property
	def telefone(self):
		return self._telefone

	@property
	def telefone(self):
		return self._endereco


	# ----------------------- #

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@sobrenome.setter
	def sobrenome(self, sobrenome):
		self._sobrenome = sobrenome

	@cpf.setter
	def cpf(self, cpf):
		self._cpf = cpf

	@email.setter
	def email(self, email):
		self._email = email

	@telefone.setter
	def telefone(self, telefone):
		self._telefone = telefone

