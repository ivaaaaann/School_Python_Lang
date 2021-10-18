# a = 5
# if a > 3:
#     print("3보다 큼")
# elif a > 1:
#     print("1보다 큼")
# else:
#     print("1보다 작음")

# n1, n2 = map(int, input().split())
# if(n1 > n2):
#     print(n1)
# else:
#     print(n2)

n1 = int(input())

if(n1 >= 70):
    print("최우수")

elif(n1 >= 50):
    print("우수")

elif(n1 >= 20):
    print("보통")

else:
    print("노력 필요")
