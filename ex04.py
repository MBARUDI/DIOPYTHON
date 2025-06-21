# Lista de produtos disponíveis no estoque
estoque = ["Camiseta", "Calça", "Tênis", "Boné", "Jaqueta"]

# Entrada do usuário
produto = input("Digite o nome do produto: ").strip()
print(f"Produto informado: {produto}")

# TODO: Verifique se o produto está no estoque:
if produto in estoque:
    print("Produto disponível")
else:
    print("Produto esgotado")