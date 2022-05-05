


for i in range(1,101):
    fizz = i % 3
    buss = i % 5
    fizz = []
    buss = []
    fizzbuss = []
    # if buss == 0:
    #     busslist.append(i)
    #     print(busslist)

    # if fizz == 0:
    #     fizzlist = []
    #     fizzlist.append(i)
    #     print(fizzlist)
    if buss == 0 and fizz == 0:
        fizzbuss.append(i)
        print(fizzbuss)