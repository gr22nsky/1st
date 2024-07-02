import random

hands = ["가위", "바위", "보"]
w = 0
l = 0
c = 0

while True:
    com_hand = random.choice(hands)
    your_hand = input("가위, 바위, 보 중 하나를 선택하세요: ")

    if your_hand == com_hand:
        c += 1
        print("무승부입니다")
    elif (your_hand == "가위" and com_hand == "보") or (your_hand == "바위" and com_hand == "가위") or (your_hand == "보" and com_hand == "바위"):
        w += 1
        print("사용자 승리!")
    else:
        l += 1
        print("컴퓨터 승리!")
    restart = input("다시 하시겠습니까?(y/n):")
    if restart == "y":
        continue
    else:
        print(f"승:{w} 패:{l} 무승부:{c}")