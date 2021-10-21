li = []
li.append('BTS')
li.append('Black Pink')
print(li)
print(li[1])

for _ in range(0, 3, 1):
    li.append(input("가수 이름을 쓰세요 : "))

print('-' * 20)
print(li)
print(len(li))
