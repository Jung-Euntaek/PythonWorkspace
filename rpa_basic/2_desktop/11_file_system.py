# 파일 기본
import os
# print(os.getcwd()) # 현재 작업공간
# os.chdir("rpa_basic") # 작업공간 추가
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir('../..') # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("C:/") # 절대경로로 이동
# print(os.getcwd())

# 파일 경로
# file_path = os.path.join(os.getcwd(), "my_file.text") # 절대경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# path = os.path.dirname(r"C:\Users\은택\Desktop\PythonWorkspace\my_file.text")
# print(path)

# 파일 정보 가져오기
# import time
# import datetime

# 파일의 생성 날짜
# ctime = os.path.getctime("scores.xlsx")
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 수정 날짜
# mtime = os.path.getmtime("scores.xlsx")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 마지막 접근 날짜
# atime = os.path.getatime("scores.xlsx")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기
# size = os.path.getsize("scores.xlsx") # 바이트 단위로 가져옴
# print(size)

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 가져오기
# print(os.listdir("rpa_basic")) # 해당 경로 바로 밑의 하위 폴더 가져오기
# result = os.walk("rpa_basic") # 주어진 폴더 밑의 모든 폴더, 파일
# result = os.walk(".") # 현재 위치

# for root, dirs, files in result:
#     print(root, dirs, files) # 루트 폴더, 디렉토리 ,파일

# 폴더 내에서 파일 찾기
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# 특정 확장자 파일 찾기
# import fnmatch
# pattern = "*.py"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))

# print(result)

# 주어진 경로가 폴더인지 파일인지(없으면 False)
# print(os.path.isdir("rpa_basic")) # 폴더인가?
# print(os.path.isfile("rpa_basic")) # 파일인가?

# # 주어진 경로 존재하는지?
# if os.path.exists("rpa_basic"):
#     print("존재")
# else:
#     print("nope")

# 파일 만들기
# open("new_file.txt", "a").close() # 빈 파일 생성

# 파일명 변경
# os.rename("new_file.txt", "new_file_rename.txt")

# 파일 삭제
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성
# os.mkdir("C:/Users/은택") # 절대경로 기준

# os.makedirs("new_folders/a/b/c") # 하위 폴더 생성

# 폴더명 변경
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folder_rename") # 폴더 안이 비었을 때만 삭제 가능

import shutil
# shutil.rmtree("new_folders") # 폴더 내용 있어도 삭제 가능

# 파일 복사하기
# shutil.copy("scores.xlsx", "test_folder") # 원본 경로, 대상 경로
# shutil.copy("scores.xlsx", "test_folder/copied_scores.xlsx") # 원본 경로, 대상 경로, 변경 파일명

# shutil.copyfile("scores.xlsx", "test_folder/copied_scores2.xlsx") # 대상경로를 파일명(폴더명 X)으로 적어야 함
# shutil.copy2("scores.xlsx", "test_folder/copied_scores3.xlsx")
# copy, copyfile : 메타 정보 복사 X
# copy2 : 메타 정보 복사(원본 파일 날짜까지 복사)

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2") # 원본, 대상 경로

# 폴더 이동
# shutil.move("test_folder", "test_folder2") # 이동할 폴더, 대상 폴더