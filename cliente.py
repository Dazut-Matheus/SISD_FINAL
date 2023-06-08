from xmlrpc.client import ServerProxy, Error


def enviar_pedido(departamento, pedido):
    try:
        portas = {
            'sanduíches': 8001,
            'pratos prontos': 8002,
            'bebidas': 8003,
            'sobremesas': 8004
        }
        if departamento in portas:
            server = ServerProxy(f'http://localhost:{portas[departamento]}')
            response = server.adicionar_pedido(departamento, pedido)
            print(response)
        else:
            print("Departamento inválido.")
    except Error as e:
        print(f"Erro ao se conectar ao servidor RPC: {e}")

def listar_pedidos(departamento):
    try:
        if departamento in portas:
            server = ServerProxy(f'http://localhost:{portas[departamento]}')
            response = server.listar_pedidos(departamento)
            print(f"Pedidos do departamento {departamento}:")
            for pedido in response:
                print(pedido)
        else:
            print("Departamento inválido.")
    except Error as e:
        print(f"Erro ao se conectar ao servidor RPC: {e}")
        
if __name__ == '__main__':
    portas = {
        'sanduíches': 8001,
        'pratos prontos': 8002,
        'bebidas': 8003,
        'sobremesas': 8004
    }

    departamentos = list(portas.keys())

    while True:
        print("Opções:")
        print("1. Enviar pedido")
        print("2. Listar pedidos")
        print("3. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            print("Departamentos válidos:")
            for i, departamento in enumerate(departamentos):
                print(f"{i+1}. {departamento}")
            
            departamento_escolha = input("Digite o número ou nome do departamento: ")
            
            if departamento_escolha.isdigit():
                departamento_numero = int(departamento_escolha) - 1
                
                if departamento_numero < 0 or departamento_numero >= len(departamentos):
                    print("Departamento inválido.")
                    continue
                
                departamento = departamentos[departamento_numero]
            else:
                departamento = departamento_escolha.lower()
                
                if departamento not in departamentos:
                    print("Departamento inválido.")
                    continue
                
            item = input("Digite o item: ")
            enviar_pedido(departamento, item)
        elif opcao == '2':
            print("Departamentos válidos:")
            for i, departamento in enumerate(departamentos):
                print(f"{i+1}. {departamento}")
            
            departamento_escolha = input("Digite o número ou nome do departamento: ")
            
            if departamento_escolha.isdigit():
                departamento_numero = int(departamento_escolha) - 1
                
                if departamento_numero < 0 or departamento_numero >= len(departamentos):
                    print("Departamento inválido.")
                    continue
                
                departamento = departamentos[departamento_numero]
            else:
                departamento = departamento_escolha.lower()
                
                if departamento not in departamentos:
                    print("Departamento inválido.")
                    continue
                
            listar_pedidos(departamento)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
    portas = {
        'Sanduíches': 8001,
        'Pratos prontos': 8002,
        'Bebidas': 8003,
        'Sobremesas': 8004
    }

    while True:
        departamentos = list(portas.keys())
        print("Opções:")
        print("1. Enviar pedido")
        print("2. Listar pedidos")
        print("3. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            print("Departamentos válidos:")
            for i, departamento in enumerate(departamentos):
                print(f"{i+1}. {departamento}")
            
            departamento_numero = input("Digite o número do departamento: ")
            departamento_numero = int(departamento_numero) - 1
            
            if departamento_numero < 0 or departamento_numero >= len(departamentos):
                print("Departamento inválido.")
                continue
            
            departamento = departamentos[departamento_numero]
            item = input("Digite o item: ")
            enviar_pedido(departamento, item)
        elif opcao == '2':
            departamento = input("Digite o departamento: ")
            listar_pedidos(departamento)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")