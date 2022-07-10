def task(array):
    for i,k in enumerate(array):
        if int(k) == 0:
            return i

def task1(array):
    return array.find('0')


print(task("111111111111000000000000000"))
print(task1("111111111111000000000000000"))



