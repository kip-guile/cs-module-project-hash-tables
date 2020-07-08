'''
exps(x, y, z) =
     if x <= 0: y + z
     if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)
'''
# Your code here
final = {}


def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        return y + z
    else:
        if (x-1, y+1, z) in final:
            first = final[(x-1, y+1, z)]
        else:
            first = expensive_seq(x-1, y+1, z)
            final[(x-1, y+1, z)] = first

        if (x-2, y+2, z*2) in final:
            second = final[(x-2, y+2, z*2)]
        else:
            second = expensive_seq(x-2, y+2, z*2)
            final[(x-2, y+2, z*2)] = second

        if (x-3, y+3, z*3) in final:
            third = final[(x-3, y+3, z*3)]
        else:
            third = expensive_seq(x-3, y+3, z*3)
            final[(x-3, y+3, z*3)] = third

        res = first + second + third
        final[(x, y, z)] = res

        return res


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
