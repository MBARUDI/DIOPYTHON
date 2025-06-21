class Pedido:
    def __init__(self):
        self.itens = []  
    
    def adicionar_item(self, preco):
        self.itens.append(preco)
        
    def calcular_total(self):
        return sum(self.itens)

# Valores de teste
entradas = [
    "Coxinha 5.50",
    "Refrigerante 4.00",
    "Brigadeiro 2.50"
]

pedido = Pedido()

for entrada in entradas:
    nome, preco_str = entrada.rsplit(" ", 1) 
    preco = float(preco_str)
    pedido.adicionar_item(preco)

print(f"{pedido.calcular_total():.2f}")