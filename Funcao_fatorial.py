def fatorial(x):

    fat = 1

    for i in range(1, x):
        fat = fat * x
        x -= 1
    print(fat)
