valor = int(float(input()) * 100)

# notas
cem = int(valor / 10000)

cincuenta = int((valor % 10000) / 5000)

vinte = int(((valor % 10000) % 5000) / 2000)

dez = int((((valor % 10000) % 5000) % 2000) / 1000)

cinco = int(((((valor % 10000) % 5000) % 2000) % 1000) / 500)

dois = int((((((valor % 10000) % 5000) % 2000) % 1000) % 500) / 200)


# moedas
um = int(((((((valor % 10000) % 5000) % 2000) % 1000) % 500) % 200) / 100)

zero_cincu = int((((((((valor % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100) / 50)

zero_vinte_cincu = int(((((((((valor % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) / 25)

zero_dez = int((((((((((valor % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 25) / 10)

zero_zero_cincu = int(((((((((((valor % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 25) % 10) / 5)

zero_zero_um = int((((((((((((valor % 10000) % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 25) % 10) % 5) / 1)


print("NOTAS:")
print(f"{cem} nota(s) de R$ 100.00")
print(f"{cincuenta} nota(s) de R$ 50.00")
print(f"{vinte} nota(s) de R$ 20.00")
print(f"{dez} nota(s) de R$ 10.00")
print(f"{cinco} nota(s) de R$ 5.00")
print(f"{dois} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{um} moeda(s) de R$ 1.00")
print(f"{zero_cincu} moeda(s) de R$ 0.50")
print(f"{zero_vinte_cincu} moeda(s) de R$ 0.25")
print(f"{zero_dez} moeda(s) de R$ 0.10")
print(f"{zero_zero_cincu} moeda(s) de R$ 0.05")
print(f"{zero_zero_um} moeda(s) de R$ 0.01")
