# from audioop import reverse
from imap_tools import MailBox
from account import *

# 로그인 필요 없음
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # 전체 메일 가져오기
    # for msg in mailbox.fetch():
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 읽지 않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM gpjet1993@gmail.com)', limit=3, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 내용 포함 메일(제목, 본문)
    # for msg in mailbox.fetch('(TEXT "test mail")'):
    #     print("[{}] {}".format(msg.from_, msg.subject)) # "(TEXT 'test mail')"로 입력 시 오류

    # 특정 내용 포함 메일(제목), 한글 오류
    # for msg in mailbox.fetch('(SUBJECT "test mail")'):
        # print("[{}] {}".format(msg.from_, msg.subject))

    # 한글 포함 메일 필터링
    # for msg in mailbox.fetch(limit=3, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-Mar-2019)', reverse=True, limit=3):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜의 메일
    # for msg in mailbox.fetch('(ON 07-Mar-2019)', reverse=True, limit=3): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상 조건 만족하는 메일
    # for msg in mailbox.fetch('(ON 07-Mar-2019 SUBJECT "test mail")', reverse=True, limit=3):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 둘 중 하나라도 만족하는 메일
    for msg in mailbox.fetch('(OR ON 07-Mar-2019 SUBJECT "test mail")', reverse=True, limit=3):
        print("[{}] {}".format(msg.from_, msg.subject))