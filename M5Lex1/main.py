from virtualstore import VirtualStore

# Criar uma instância da loja virtual
store = VirtualStore()

# Registrar alguns produtos
store.register_products("Camiseta", 50.00, "Camiseta 100% algodão", 10)
store.register_products("Calça", 100.00, "Calça jeans", 5)
store.register_products("Tênis", 200.00, "Tênis esportivo", 8)

# Exibir produtos disponíveis
print("Produtos disponíveis:")
store.display_products()

# Adicionar produtos ao carrinho
store.add_cart("Camiseta", 10)
store.add_cart("Calça", 1)
store.view_cart()
# Exibir total antes do desconto
print("-" * 30)
print(f"Total antes do desconto: R$ {store.calculate_total():.2f}")

# Aplicar desconto percentual de 10%
store.apply_discount('percentual', 10)

# Exibir total após aplicar desconto
print(f"Total após aplicar desconto: R$ {store.calculate_total():.2f}")

# Remover um item do carrinho
store.remove_cart("Camiseta", 1)

# Exibir total após remover item
print(f"Total após remover item: R$ {store.calculate_total():.2f}")
print("-" * 30)


# Exibir produtos disponíveis novamente
store.display_products()