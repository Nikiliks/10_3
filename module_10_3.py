import threading
from random import randint
from threading import Lock, Thread
from time import sleep



class Bank:
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            popolnenie = randint(50, 500)
            self.balance += popolnenie
            print(f'Пополнение:{popolnenie}. Баланс:{self.balance}' + '\n')
            sleep(0.001)

    def take(self):
        for i in range(100):
            snaytie = randint(50, 500)
            print(f'Запрос на случайное число {snaytie}')
            if snaytie <= self.balance:
                self.balance -= snaytie
                print(f'Снятие: {snaytie}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bank = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bank,))
th2 = threading.Thread(target=Bank.take, args=(bank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bank.balance}')
