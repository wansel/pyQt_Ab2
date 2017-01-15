#-*- coding: latin1 -*-
from errors import ValorInvalidoError
from errors import SaldoInsuficienteError

from conta import Conta

contas = {}

def menu():
    print("1) Cadastro")
    print("2) Saldo")
    print("3) Saque")
    print("4) Depósito")
    print("0) Sair")
    return int(input("Opção: "))

def saque(conta):
    try :
        valor = input("Digite o valor desejado: R$ ")
        conta.op_saque(valor)
        print("Saque realizado com sucesso!")
    except NameError as vie:
        SaldoInsuficienteError(vie)
    except SaldoInsuficienteError as sie:
        print(sie)

def deposito(conta):
    try :
        valor = input("Digite o valor desejado: R$ ")
    except ValorInvalidoError as vie:
        print(vie)
    conta.op_deposito(valor)
    print("Deposito realizado com sucesso!")
    #except ValorInvalidoError as vie:
    #    print(vie)

while True:
    opc = menu()
    if (opc == 0) :
        break
    elif (opc == 1) : # saldo
        numero = raw_input("Digite o número da conta: ")
        if contas.has_key(numero) :
            print("Já existe uma conta cadastrada com este número!")
        else :
            conta = Conta(numero)
            contas[numero] = conta
            print("Conta cadastrada com sucesso!")
    elif (opc == 2) : # saldo
        numero = raw_input("Digite o número da conta: ")
        if contas.has_key(numero) :
            print(contas[numero])
    elif (opc == 3) : # saque
        numero = raw_input("Digite o número da conta: ")
        if contas.has_key(numero) :
            saque(contas[numero])
    elif (opc == 4) : # deposito
        if contas.has_key(numero) :
            deposito(contas[numero])


