from lesson8.Task4.models.Store import Store
from lesson8.Task4.models.Xerox import Xerox
from lesson8.Task4.models.Printer import Printer
from lesson8.Task4.models.Scanner import Scanner
from time import sleep


store = Store('Store#1')
print(f"Welcome to {store.name}")
sleep(1)

scanner = Scanner("Scanner HZ", 10.2)
printer = Printer("Printer HP", 982)
xerox = Xerox("Xerox Canon", 555, True)

print(f"Put to store 3 {scanner.title}")
store.put(scanner, 3)
sleep(1)

print(f"Put to store 15 {xerox.title}")
store.put(xerox, 15)
sleep(1)

print("Store: ")
print(store)
sleep(3)

print(f"Try get 3 {xerox.title}")
store.get(xerox, 3)
sleep(2)

print(f"Put to store 20 {printer.title}")
store.put(printer, 20)
sleep(2)

print(f"Try get 4 {scanner.title}")
store.get(scanner, 4)
sleep(2)

print(f"Try get 3 {scanner.title}")
store.get(scanner, 3)
sleep(2)

print(f"Store: {store}")
