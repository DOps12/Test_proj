def common_ele(l,n):
    e = []
    for i in l:
        if i in n:
                e.append(i)
    return e

n = [1,2,3,4,5]
l = [1,3,4,6]
print(common_ele(l,n))