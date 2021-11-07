# conexaoBD.py
import mysql.connector as mysql # Trocando para MYSQL.

class ConexaoBD:

	def __init__(self,host = 'localhost',database = 'Banco',user = 'root',passwd = 'Slowking2021#'):
		self.host = host
		self.user = user
		self.pwd = passwd
		self.db = database
		self.conexao = None
		self.cursor = None
		
	def conecta(self):
		self.conexao = mysql.connect(host = self.host, db=self.db, user=self.user, passwd=self.pwd)
		# self.conexao = sqlite3.connect(self.db)
		self.cursor = self.conexao.cursor()

	def desconecta(self):
		self.conexao.commit()
		self.conexao.close()

	def executaSELECT(self,sql):
		self.conecta()
		self.cursor.execute(sql)
		resultado = self.cursor.fetchall()
		self.desconecta()
		return resultado

	def executaALTERACOES(self, sql):
		self.conecta()
		self.cursor.execute(sql)
		self.conexao.commit()
		self.desconecta()

	def gerarID_historico(self):
		self.conecta()
		self.cursor.execute(f"SELECT count(*) FROM historico")
		aux = self.cursor.fetchall()
		if( aux[0][0] != None ):
			resultado = int(aux[0][0]) + 1
		else:
			resultado = 0
		self.desconecta()
		return resultado
