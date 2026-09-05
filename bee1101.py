while True:

    M, N = map(int, input().split())

    soma = 0


    if M <= 0 or N <= 0:
    
            break
    
    elif M > N:
        for numero in range(N, M + 1):
            print(numero, end = " ")
            soma += numero
        print(f"Sum={soma}")

    elif M < N:
        for numero in range(M, N + 1):
            print(numero, end = " ") #end = " " faz com que sejam impressos na mesma linha sem quebrar linha pois por padrao end = "\n"
            soma += numero

        print(f"Sum={soma}")

        
    


