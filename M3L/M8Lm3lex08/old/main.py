from Employee import Employee

iran = Employee("Iran", "Ferreira", 300.42)
ronaldo = Employee("Ronaldo", "Fenômeno", 11276.65)

print(f"Salário anual de {iran.getNome()} {iran.getSobrenome()}: R${iran.getSalarioAnual():.2f}")
print(f"Salário anual de {ronaldo.getNome()} {ronaldo.getSobrenome()}: R${ronaldo.getSalarioAnual():.2f}")

iran.aumentarSalario(10.0)
ronaldo.aumentarSalario(10.0)

print(f"Salário anual de {iran.getNome()} {iran.getSobrenome()} após aumento: R${iran.getSalarioAnual():.2f}")
print(f"Salário anual de {ronaldo.getNome()} {ronaldo.getSobrenome()} após aumento: R${ronaldo.getSalarioAnual():.2f}")