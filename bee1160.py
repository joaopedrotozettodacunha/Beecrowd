n_casos = int(input())

for casos in range(n_casos):



    pa, pb, ga, gb = input().split()

    pa, pb = int(pa), int(pb)

    ga, gb = float(ga), float(gb) 

    anos = 0

    while pa <= pb:

        pa = int(pa * (1 + (ga/100)))
        pb = int(pb *(1+(gb/100)))
        anos += 1

        if anos > 100:
            break
    if anos > 100:
        print("Mais de 1 seculo.")

    else: 
        print(f"{anos} anos.")
    






