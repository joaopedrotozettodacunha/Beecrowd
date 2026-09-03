A, B, C = input().split()

D, E, F = input().split()

B = int(B)
E = int(E)

C = float(C)
F = float(F)

total = (B * C) + (E * F)

print(f"VALOR A PAGAR: R$ {total:.2f}")
