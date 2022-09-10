import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결 확인
    smtp.starttls() # 모든 내용 암호화 후 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    subject = "test mail" # 메일 제목(한글은 오류)
    body = "mail body" # 본문

    msg = f"Subject: {subject}\n{body}"

    # 발신자, 수신자, 정해진 형식의 메세지
    smtp.sendmail(EMAIL_ADDRESS, "gpjet1993@gmail.com", msg)