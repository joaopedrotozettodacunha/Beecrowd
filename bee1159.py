while True: 

    X = int(input())

    soma = 0

    if X == 0:
        break
    if X != 0:

        if X % 2 == 0:

            for numero in range(X, X + 10, 2):
                soma += numero
                
            print(soma)

        elif X % 2 != 0:

            X = X + 1
        
            for numero in range(X, X + 10, 2):
                soma += numero
            print(soma)
                
