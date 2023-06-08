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

if __name__ == '__main__':
    while True:
        departamento = input("Digite o departamento: ")
        item = input("Digite o item: ")
        enviar_pedido(departamento, item)
