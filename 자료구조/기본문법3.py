def Hello(name, address, phone):  # 콜론 꼭 사용
    print(f'제이름은 {name} 이고 주소는 {address} 입니다.'
          f'제 전화번호는 {phone}에요')
# 파이썬에서는 들여쓰기가 중요하다.


# 출력하기
Hello("임동현", "대구 서구", "010-2797-3907")


def Singer(a, b, c):
    print(f"제가 좋아하는 가수는 첫번째 {a}, 두번째 {b}, 세번째 {c}")


a = str(input("a = "))
b = str(input("b = "))
c = str(input("c = "))

Singer(a, b, c)
