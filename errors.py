#-*- coding: latin1 -*-
class SaldoInsuficienteError(Exception):

    def __str__(self):
        return "Saldo insuficiente!"

class ValorInvalidoError(ValueError):
    def __str__(self):
        return "Valor informado é inválido!"

class ContaExistenteError(Exception):
	def __str__(self):
		return "Conta já cadastrada"

class ContaInvalidaError(TypeError):
	def __str__(self):
		return "Caracteres Inválidos"