Notas = list()

for contador in range(0,3):
    Notas.append(float(input(f"Digite nota {contador+1}: ")))

print(Notas)

media = ((Notas[0]*2) + (Notas[1]*3) + (Notas[2]*5))/10
print(f"A media foi: {media}")