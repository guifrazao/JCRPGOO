from invoice import Invoice

invoice1 = Invoice("001", "Mouse", 3, 20.0)

    # Exibindo detalhes da fatura
print(f"Invoice Number: {invoice1.get_invoice_number()}")
print(f"Description: {invoice1.get_description()}")
print(f"Quantity: {invoice1.get_quantity()}")
print(f"Price per Item: R$ {invoice1.get_price_per_item():.2f}")
print(f"Total Amount: R$ {invoice1.invoice_calculation():.2f}")

    # Testando condições de quantidade negativa
invoice2 = Invoice("002", "Keyboard", -5, 30.0)
print(f"\nInvoice Number: {invoice2.get_invoice_number()}")
print(f"Description: {invoice2.get_description()}")
print(f"Quantity: {invoice2.get_quantity()}")  # Deve ser 0
print(f"Price per Item: R$ {invoice2.get_price_per_item():.2f}")
print(f"Total Amount: R$ {invoice2.invoice_calculation():.2f}")

    # Testando condições de preço negativo
invoice3 = Invoice("003", "Monitor", 2, -150.0)
print(f"\nInvoice Number: {invoice3.get_invoice_number()}")
print(f"Description: {invoice3.get_description()}")
print(f"Quantity: {invoice3.get_quantity()}")
print(f"Price per Item: R$ {invoice3.get_price_per_item():.2f}")  # Deve ser 0.0
print(f"Total Amount: R$ {invoice3.invoice_calculation():.2f}")