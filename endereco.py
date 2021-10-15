class Endereco:
	__slots__ = ['_pais', '_estado', '_cidade', '_cep', '_bairro', '_rua', '_numero']

	def __init__(self, pais='Brasil', estado=None, cidade=None, cep=None, bairro=None, rua=None, numero=None):
		self._pais = pais
		self._estado = estado
		self._cidade = cidade
		self._bairro = bairro
		self._cep = cep
		self._bairro = bairro
		self._rua = rua
		self._numero = numero

	@property
	def pais(self):
		return self._pais

	@property
	def estado(self):
		return self._estado

	@property
	def cidade(self):
		return self._cidade

	@property
	def cep(self):
		return self._cep

	@property
	def bairro(self):
		return self._bairro

	@property
	def rua(self):
		return self._rua

	@property
	def numero(self):
		return self._numero

	# ---------------------------- #

	@pais.setter
	def pais(self, pais):
		self._pais = pais

	@estado.setter
	def estado(self, estado):
		self._estado = estado

	@cidade.setter
	def cidade(self, cidade):
		self._cidade = cidade
		
	@cep.setter
	def cep(self, cep):
		self._cep = cep

	@bairro.setter
	def bairro(self, bairro):
		self._bairro = bairro
		
	@rua.setter
	def rua(self, rua):
		self._rua = rua

	@numero.setter
	def numero(self, numero):
		self._numero = numero