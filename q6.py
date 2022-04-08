TotalSegundos = int(input("Informe a duração do evento em Segundos: "))
SegundoControle1 = 0
SegundoControle2 = 0
Minutos = 0
Horas = 0

for i in range(0, TotalSegundos):
    SegundoControle1+=1
    SegundoControle2+=2
    if SegundoControle1 == 60:
        Minutos += 1
        SegundoControle1 = 0
    if SegundoControle2 == 3600: 
        Horas += 1 
        SegundoControle1 = 0
        SegundoControle2 = 0
        Minutos = 0

print(f"A duração do evento foi {Horas} horas, {Minutos} minutos e {SegundoControle1} segundos")