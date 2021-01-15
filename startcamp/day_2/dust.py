import requests
from pprint import pprint

key = '5a81NyUX2XpAQzfBDpGyKAHbaoYehmEinUE7x9Gq%2FNhzx%2BToKCn%2BhlhuJpuFZriS2DzSfoUrRplDhMlPoKU%2BxQ%3D%3D'
return_type = 'json'
num_of_rows = '5'
page_no = '1'
sido_name = '서울'
ver = '1.0'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_name}&ver={ver}'

response = requests.get(url).json()

# print(type(response))
# pprint(response)

# stationName의 미세먼지 농도는 pm10value입니다. 라는 메세지를 출력하시오.
station_name = response['response']['body']['items'][0]['stationName']
dust = response['response']['body']['items'][0]['pm10Value']
print(f'{station_name}의 미세먼지 농도는 {dust}입니다.')
