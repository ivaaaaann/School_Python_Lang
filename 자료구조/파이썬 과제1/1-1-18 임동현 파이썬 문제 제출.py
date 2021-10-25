# 영희는 숫자를 거꾸러 읽는 버릇이 있다. 어느날 400 이상숫자 찾기 문제를 풀고 있던
# 영희는 그 문제를 풀다가 버릇이 발동 되었다고 한다.
# 문제 알려주는 값이 364, 872, 345, 641, 488, 712 이였다면 영희가 적었던
# 닶이 무엇인지 알아내는 프로그램을 만들어라

arr = [364, 872, 345, 641, 488, 712]


def solution(length, list):
    result = []
    for i in range(0, length):
        n = str(list[i])
        result.append(int(n[::-1]))
    return result


nums = solution(len(arr), arr)
result = list(filter(lambda n: n >= 400, nums))
print(result)
