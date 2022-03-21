def gen_fibon(n):

    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output

seq_size = int(input("How big of a squence dou you want ?: "))
for number in gen_fibon(seq_size):
    print(number)