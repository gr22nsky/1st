import random

random_number = random.randint(1, 100)

num = int(input("숫자를 입력하세요 : "))
while num < 1 or num > 10:
    print("유효한 범위 내의 숫자를 입력하세요")
    num = int(input("숫자를 입력하세요 : "))

i = 1
while num != random_number:

    if num < 1 or num > 100:
        print("유효한 범위 내의 숫자를 입력하세요")
        num = int(input("숫자를 입력하세요 : "))

    elif num < random_number:
        print("업")
        i += 1
        num = int(input("숫자를 입력하세요 : "))

    elif num > random_number:
        print("다운")
        i += 1
        num = int(input("숫자를 입력하세요 : "))

    else:
        break
print("맞았습니다")
print("시도한 횟수 :", i)