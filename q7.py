import os 
os.system("cls")

PD = 0.28
PI = 0.45
CF = float(input("Insira o valor do custeamento da fabrica: "))
CC = ((CF*PD)+(CF*PI))+CF

print(f"O custo ao consumidor é a: {CC}")
print(f"O custo ao fabricante é a: {CF}")
print(f"Sem custo do fabricante, o consumidor pagaria: {CC - CF}")
