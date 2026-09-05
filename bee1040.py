N1, N2, N3, N4 = map(float, input().split())





media = float(((2*N1) + (3*N2) + (4*N3) +(1*N4))/10)


print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5 <= media <= 6.9:
    print("Aluno em exame.")
    Nexame = float(input())
    

    print(f"Nota do exame: {Nexame:.1f}")

    media_final = (media + Nexame)/2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {media_final}")




