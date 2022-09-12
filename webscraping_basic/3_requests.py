import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
# res.raise_for_status() # 문제 생겼을 때 자동으로 프로그램 종료
# print("응답코드 :", res.status_code) # 200이면 정상(HTML 문서 가져올 수 있음)

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)