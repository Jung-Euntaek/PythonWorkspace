from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") # INBOX : 기본 편지함

# limit : 최대 메일 개수
# reverse : True - 최신 메일
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    # print("참조자", msg.cc)
    # print("숨긴 참조", msg.bcc)
    print("날짜", msg.date) # GMT 시간
    print("본문", msg.text)
    print("HTML 메세지", msg.html)
    print("=" * 100)

    # 첨부 파일
    for att in msg.attachments:
        print("첨부파일", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)

        # 다운로드
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("첨부 파일 {} 다운로드 완료".format(att.filename))

mailbox.logout()