import sys

number = int(sys.argv[1])  # 명령줄에서 입력받은 값을 정수로 변환

# 1부터 입력받은 number까지 반복
for i in range(1, number + 1):
    if number % i == 0:  # i가 number의 약수인지 확인
        print(i, end=" ")  # 약수를 한 줄에 출력

print()  # 줄바꿈
