import requests

res = requests.get('http://example.com/')  # http://example.com에 GET 방식으로 요청을 보내고 응답을 객체로 저장
print(res.text)  # 응답 받은 객체의 text를 출력
print(res.status_code)  # 응답 받은 객체의 응답 코드
