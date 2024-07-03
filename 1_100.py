import random

random_number = random.randint(1, 10)
i = 0
while True:
    num = int(input("숫자를 입력하세요 : "))
    if num < 1 or num > 10:
        print("유효한 범위 내의 숫자를 입력하세요")

    elif num < random_number:
        i += 1
        print("업")

    elif num > random_number:
        i += 1
        print("다운")

    elif num == random_number:
        i += 1
        print("맞았습니다!")
        print("시도한 횟수 :", i)
        break
