# conexaoBD.py
import mysql.connector as mysql

class ConexaoBD:

	def __init__(self, host='localhost', db='banco_pooii', user='root', passwd='password', auth_plugin='mysql_native_password'):
		self.host = host 
		self.user = user
		self.pwd = passwd
		self.db = db
		self.plug = auth_plugin
	
	def conecta(self):
		self.conexao = mysql.connect(host = self.host, db=self.db, user=self.user, passwd=self.pwd, auth_plugin=self.plug)
		self.cursor = self.conexao.cursor()

	def desconecta(self):
		self.conexao.close()

	def executaSELECT(self, sql):
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
		self.cursor.execute(f"SELECT max(numero) FROM conta")
		aux = self.cursor.fetchall()
		if( aux[0][0] != None ):
			resultado = int(aux[0][0]) + 1
		else:
			resultado = 0
		self.desconecta()
		return resultado