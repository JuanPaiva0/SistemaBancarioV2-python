menu = """
==== MENU ====

  [u] Criar Usuario
  [c] Criar conta corrente
  [d] Depositar
  [s] Sacar 
  [e] Extrato
  [lc] Listar Contas
  [q] Sair

==============
"""
LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

def deposito(valor_deposito):
  global extrato
  global saldo
  if valor_deposito < 0: 
      print("Valor inválido")
  else:
      saldo += valor_deposito
      extrato += f"""
Deposito: R${valor_deposito}
Saldo: R${saldo}\n
"""
      print(f"Depósito de R$ {valor_deposito} realizado com sucesso!")
  return saldo

def saque(valor_saque):
  global saldo
  global limite
  global numero_saques
  global extrato

  if valor_saque > limite:
      print("Valor do saque maior que o limite")
  elif valor_saque > saldo:
      print("Saldo insuficiente")
  elif valor_saque < 0:
      print("Valor inválido")
  else:
      saldo -= valor_saque
      numero_saques += 1
      extrato += f"""
Saque: R${valor_saque}
Saldo: R${saldo}\n
"""
      print(f"Saque de R$ {valor_saque} realizado com sucesso!")
  return saldo

def mostrar_extrato():
  global extrato
  if extrato == "":
      print("Não foram feitas movimentações")
  else:
      print("\n============ EXTRATO ============")
      print(extrato)
      print(f"Saldo: {saldo:.2f}")
      print("==================================")

def criar_usuario():
  global usuarios
  cpf = input("Informe seu CPF (somente os números): ")
  filtro_usuario = filtrar_usuario(cpf)
  if filtro_usuario:
      print("CPF já cadastrado")
  else:
      nome = input("Informe seu nome: ")
      data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
      endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

      usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
      print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf):
  usuario_encontrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuario_encontrados[0] if usuario_encontrados else None

def criar_conta():
  global contas
  agencia = AGENCIA
  numero_conta = len(contas) + 1
  cpf = input("Informe seu CPF (somente os números): ")
  filtro_usuario = filtrar_usuario(cpf)

  if filtro_usuario:
      print("Conta criada com sucesso")
      return {"agencia": agencia, "conta": numero_conta, "usuario": filtro_usuario}
  else: 
      print("Usuário não cadastrado")
      return None

def mostrar_contas():
  global contas
  if not contas:
      print("Não há contas cadastradas")
  else:
      for conta in contas:
          print(f"""\
    Agencia:\t{conta['agencia']}
    C/C:\t\t{conta['conta']}
    Titular:\t{conta['usuario']['nome']}  
    """)

while True:
  opcao = input(menu + "\nEscolha uma opção: ")

  if opcao == "u":
      criar_usuario()

  elif opcao == "c":
      conta = criar_conta()

      if conta:
          contas.append(conta)

  elif opcao == "d":
      valor_deposito = float(input("Informe o valor do deposito: "))
      deposito(valor_deposito)
      
  elif opcao == "s":
      if numero_saques == LIMITE_SAQUES:
          print("Limites de saques atingido")
      else:
          valor_saque = float(input("Informe o valor do saque: "))
          saque(valor_saque)

  elif opcao == "e":
      mostrar_extrato()

  elif opcao == "lc":
      mostrar_contas()

  elif opcao == "q":
      break

  else: 
      print("Opção invalida, por favor selecione a opção desejada!")