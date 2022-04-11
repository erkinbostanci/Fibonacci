from re import S

def gen_fibon(n):

    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return print(int(output[-1]))

seq_size = int(input("How big of a squence dou you want ?: "))
gen_fibon(seq_size)
