class Cliente:
	def __init__(self, nome, telefone):
		self.nome = nome
		self.telefone = telefone

class Conta:
	def __init__(self, clientes, número, saldo = 0):
		self.clientes = clientes
		self.número = número
		self.saldo = 0
		self.operações = []
		self.depósito(saldo)

	def resumo(self):
		print('CC Nº %s Saldo: %10.2f' %(self.número, self.saldo))

	def saque(self, valor):
		if self.saldo >= valor:
			self.saldo -= valor
			self.operações.append(['Saque', valor])

	def depósito(self, valor):
		self.saldo += valor
		self.operações.append(['Depósito', valor])

	def extrato(self):
		print('Extrato CC Nº %s' %self.número)
		for op in self.operações:
			print('%10s %10.2f' %(op[0], op[1]))
			print('%10s %10.2f\n' %('Saldo', self.saldo))

class ContaEspecial(Conta):
	def __init__(self, clientes, número, saldo = 0, limite = 0):
		Conta.__init__(self, clientes, número, saldo)
		self.limite = limite

	def Saque(self, valor):
		if self.saldo + self.limite >= valor:
			self.saldo -= valor
			self.operações.append(['Saque', valor])
