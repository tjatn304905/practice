# Dictionary(딕셔너리)

my_home = {
    'location': 'seoul',
    'a': 'b'
}

# 딕셔너리 원소 접근
# 1
print(my_home['location'])
# print(my_home['name'])
# 2
print(my_home.get('location'))
print(my_home.get('name'))  # Nones
