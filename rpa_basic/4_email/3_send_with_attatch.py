from fileinput import filename
import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS # 발신인
msg["To"] = "gpjet1993@gmail.com" # 수신인
msg.set_content("다운로드 하세요")

# msg.add_attachment()
# MIME 타입
with open("myw3schoolsimage.jpg", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="jpeg", filename=f.name)

with open("테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("sample.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
