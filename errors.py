#-*- coding: latin1 -*-
class SaldoInsuficienteError(Exception):

    def __str__(self):
        return "Saldo insuficiente!"

class ValorInvalidoError(Exception):
    def __str__(self):
        return "Valor informado é inválido!"

class ContaExistenteError(Exception):
	def __str__(self):
		return "Conta já cadastrada"

class ContaInvalidaError(Exception):
	def __str__(self):
		return "Caracteres Inválidos"