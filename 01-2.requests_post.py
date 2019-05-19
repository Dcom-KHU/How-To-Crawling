import requests

request_data = {'locgbn': 'K1', 'sch_date': '', 'fo_gbn': 'stu'}
res_post = requests.post('https://dorm2.khu.ac.kr/dorm2/food/getWeeklyMenu.kmc', request_data)  # POST 방식
dish = {}

json_res = res_post.json()['root'][0]['WEEKLYMENU'][0]  # WEEKLYMENU 추출

del json_res['locgbn']
del json_res['fo_gbn']
del json_res['seq']
del json_res['today']

for i in range(1,8):
    del json_res['fo_date' + str(i)]

for key in json_res:
    temp_list = json_res[key].split(',')
    for item in temp_list:
        if item.startswith('선수단-') or item.startswith('한정수량-') or item.startswith('선수식-'):
            index = item.find('-')
            item = item[index + 1:]
        if item in dish:
            dish[item] += 1
        else:
            dish[item] = 1

print(dish)
