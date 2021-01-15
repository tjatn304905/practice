# 변수(variable) 사용
# 저장

greeting = '안녕하세요!'

print(greeting)
print(greeting)
print(greeting)
print(greeting)
print(greeting)

# 반복문 사용
# while
# False가 될때까지 반복
count = 0
while count < 5:
    print(greeting)
    print(count)
    count = count + 1
print('while문 종료')  # while문 블록에 포함되지 않음(들여쓰기 중요)

# for

# for i in [1, 1, 2, 2, 3]:
#     print(greeting)

for _ in range(5):
    # print(i)
    print(greeting)
# for문 내부에서 i가 쓰이지 않을경우 통상적으로 _로 대체한다
