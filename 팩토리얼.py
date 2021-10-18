# def fact(n):
#     if n <= 1:
#         return 1
#     else:
#         return n* fact(n-1)

# print(fact(10))

#쉬운 버전
def fact(n):
    r = 1
    for i in range(1,n+1):
        r=r*i
    return r


print(fact(5))
