import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS # 발신인
msg["To"] = "gpjet1993@gmail.com" # 수신인

# 여러 명에게 메일 보낼 때
# msg["To"] = "gpjet@naver.com", "gpjet@hanmail.net"
# to_list = ["gpjet@naver.com", "gpjet@hanmail.net"]
# msg["To"] = ", ".join(to_list)

# # 참조
# msg["Cc"] = "gpjet1993@gmail.com"

# # 비밀참조
# msg["Bcc"] = "gpjet1993@gmail.com"

msg.set_content("테스트 본문입니다") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)