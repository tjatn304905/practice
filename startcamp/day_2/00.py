# 숫자
number = 3
print(type(number))


# 문자
string = '문자열'
print(type(string))

# boolean
boolean = True
print(type(boolean))

# 형변환
string_number = '3'
# print(string_number + 5)
print(int(string_number) + 5)
# 문자열 안의 내용이 정수형이어야만 가능하다

# f-string / string interpolation
name = '홍길동'
print(f'{name}입니다. 반갑습니다.')
