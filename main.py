# main -- Apenas para testes.
from pessoa import Pessoa
from cliente import Cliente
from conta import Conta
from endereco import Endereco
from funcionario import Funcionario
from historico import Historico
from login import Login
from principal import DadosCadastros

endereco1 = Endereco('Brasil', 'CE', 'Parambu', '63680-000', 'Vila Nova', 'Avenida nao sei o q', 8)
pessoa1 = Pessoa('Matheus', 'Victor', '098.363.947-33', 'matheus@ufpi.edu.br', '8888888', endereco1)
cliente1 = Cliente(pessoa1)
conta1 = Conta(1, cliente1, 700.50, '12345')

print(conta1.titular.nome)
