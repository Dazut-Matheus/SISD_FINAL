from xmlrpc.server import SimpleXMLRPCServer
import threading

class Server:
    def __init__(self):
        self.departamentos = {
            'sanduíches': [],
            'pratos prontos': [],
            'bebidas': [],
            'sobremesas': []
        }

    def adicionar_pedido(self, departamento, pedido):
        try:
            if departamento in self.departamentos:
                self.departamentos[departamento].append(pedido)
                print(f"Pedido recebido para o departamento de {departamento}: {pedido}")
                return "Pedido adicionado com sucesso."
            else:
                return f"Departamento inválido: {departamento}"
        except Exception as e:
            print(f"Erro ao processar o pedido: {e}")
            return "Erro ao processar o pedido. Por favor, tente novamente."

    def listar_pedidos(self, departamento):
        if departamento in self.departamentos:
            return self.departamentos[departamento]
        else:
            return f"Departamento inválido: {departamento}"

    def departamento_sanduiches(self):
        server_sanduiches = SimpleXMLRPCServer(('localhost', 8001), allow_none=True)
        server_sanduiches.register_function(self.adicionar_pedido, 'adicionar_pedido')
        server_sanduiches.register_function(self.listar_pedidos, 'listar_pedidos')
        server_sanduiches.serve_forever()

    def departamento_pratos_prontos(self):
        server_pratos_prontos = SimpleXMLRPCServer(('localhost', 8002), allow_none=True)
        server_pratos_prontos.register_function(self.adicionar_pedido, 'adicionar_pedido')
        server_pratos_prontos.register_function(self.listar_pedidos, 'listar_pedidos')
        server_pratos_prontos.serve_forever()

    def departamento_bebidas(self):
        server_bebidas = SimpleXMLRPCServer(('localhost', 8003), allow_none=True)
        server_bebidas.register_function(self.adicionar_pedido, 'adicionar_pedido')
        server_bebidas.register_function(self.listar_pedidos, 'listar_pedidos')
        server_bebidas.serve_forever()

    def departamento_sobremesas(self):
        server_sobremesas = SimpleXMLRPCServer(('localhost', 8004), allow_none=True)
        server_sobremesas.register_function(self.adicionar_pedido, 'adicionar_pedido')
        server_sobremesas.register_function(self.listar_pedidos, 'listar_pedidos')
        server_sobremesas.serve_forever()

    def iniciar_servidor(self):
        thread_sanduiches = threading.Thread(target=self.departamento_sanduiches)
        thread_pratos_prontos = threading.Thread(target=self.departamento_pratos_prontos)
        thread_bebidas = threading.Thread(target=self.departamento_bebidas)
        thread_sobremesas = threading.Thread(target=self.departamento_sobremesas)

        thread_sanduiches.start()
        thread_pratos_prontos.start()
        thread_bebidas.start()
        thread_sobremesas.start()

        thread_sanduiches.join()
        thread_pratos_prontos.join()
        thread_bebidas.join()
        thread_sobremesas.join()

if __name__ == '__main__':
    server = Server()
    server.iniciar_servidor()
