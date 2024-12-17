# bank_transaction.py

import threading
import time
from lamport_clock import LamportClock

# Cuenta bancaria compartida
bank_account = {"balance": 1000}
lock = threading.Lock()

# Reloj de Lamport
lamport_clock = LamportClock()

# Función que simula una transacción bancaria (depósito o retiro)
def transaction(id, amount, operation):
    global bank_account

    lamport_clock.increment()  # Incrementa el reloj
    print(f"Proceso {id} intentando realizar {operation} de {amount} con marca de tiempo {lamport_clock.get_time()}")

    # Sincroniza el acceso a la cuenta bancaria
    with lock:
        lamport_clock.increment()
        print(f"Proceso {id} accediendo a la cuenta con marca de tiempo {lamport_clock.get_time()}")
        
        # Realiza la operación bancaria
        if operation == "deposit" or (operation == "withdraw" and bank_account["balance"] >= amount):
            if operation == "deposit":
                bank_account["balance"] += amount
                print(f"Depósito de {amount} realizado. Saldo actual: {bank_account['balance']}")
            else:
                bank_account["balance"] -= amount
                print(f"Retiro de {amount} realizado. Saldo actual: {bank_account['balance']}")
        else:
            print(f"Operación {operation} fallida. Saldo insuficiente para retiro de {amount}. Saldo actual: {bank_account['balance']}")

# Función principal que ejecuta las transacciones
def main():
    # Crear múltiples hilos (procesos) para simular transacciones
    threads = []
    threads.append(threading.Thread(target=transaction, args=(1, 500, "deposit")))
    threads.append(threading.Thread(target=transaction, args=(2, 300, "withdraw")))
    threads.append(threading.Thread(target=transaction, args=(3, 200, "withdraw")))

    # Iniciar las transacciones
    for t in threads:
        t.start()

    # Esperar a que todas las transacciones terminen
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
