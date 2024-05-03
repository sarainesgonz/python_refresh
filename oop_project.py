from bank_accounts import *

Mati = BankAccount(1000, "Mati")
Sara = BankAccount(2000, "Sara")

Mati.getBalance()
Sara.getBalance()

Sara.deposit(500)

Mati.withdraw(5000)
Mati.withdraw(300)

# triggers transfer interrupted error
Mati.transfer(10000, Sara)
# successful transfer
Mati.transfer(100, Sara)
