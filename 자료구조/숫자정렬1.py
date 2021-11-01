# 숫자를 받아 정렬하는데 정렬하고 중복되는 숫자는 삭제

nums = list(map(int, input().split()))
arr = list(set(nums))
print(arr)
nums.sort()
print(arr)
