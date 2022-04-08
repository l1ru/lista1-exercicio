dias = int(input("Insira quantos dias:"))

anos = int(dias / 365)
meses = int((dias % 365)/30)
dias = int((dias % 365)%30)

print(f"Sua idade em anos {anos}, em meses {meses}, em dias {dias}")