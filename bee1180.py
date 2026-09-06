tamanho_vetor = int(input())
numeros = (input().split())

vetor = []

for n in range(tamanho_vetor):
    vetor.append(int(numeros[n]))


menor = vetor[0]
posicao = 0

for i, numero in enumerate(vetor):
    if numero < menor:
        menor = numero
        posicao = i

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
