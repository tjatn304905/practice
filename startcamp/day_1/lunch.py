import random

# list[리스트] (다른 언어에서는 array) - pythonic
stores = ['새마을식당', '리춘시장', '스타벅스']
print(stores)
print(stores[1])

# random 모듈 및 sample 함수 사용
pick = random.sample(stores, 2)
print(pick)
