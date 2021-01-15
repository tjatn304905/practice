# 함수
# 특정 역할을 하는 코드의 집합
# 하나의 함수는 하나의 역할만 해아한다.

# 함수 정의
def sum(a, b):
    result = a + b
    return result # -> return 따로 해주지 않으면 none을 리턴함 
    
    apple = a * b
    ... # 첫 return 이후의 코드는 동작하지 않는다.
    # 리턴값이 두 개 이상일 수 있다.(if문 사용 등)

# 함수 실행(호출)
a = sum(1, 2) # 함수의 가장 큰 목적은 코드의 재사용성
print(sum(1, 2))

# 미니 실습) 주어진 양수 n
print(help(len))