import random

# 1. 1~45까지의 수
# numbers = [1, 2, 3, ...]
numbers = range(1, 46)

# 2. 6개를 무작위로 추첨
pick = random.sample(numbers, 6)
print(pick)

# string-interpolation (string사이에 값을 삽입)
# f-string
print(f'오늘의 로또 번호는 {pick} 입니다.')
