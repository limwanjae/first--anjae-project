# 파일시스템 1  4:03:25~
# 파일과 폴더를 어떻게 관리하는지 배운다~~
# 파일 기본
import os
# print(os.getcwd())# current working directory :현재 작업중인 디렉토리(공간)

# os.chdir("rpa_basic")# rpa_basic으로 작업공간 이동
# print(os.getcwd())

# os.chdir("..")# 부모 폴더로 이동
# print(os.getcwd())

# os.chdir("../..")# 조부모 폴더로 이동   ../../
# print(os.getcwd())

# os.chdir("c:/")# 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(file_path)

# 파일경로에서 폴더 정보만 가져오기
# print(os.path.dirname(r"C:\Users\lim\Desktop\PythonWorkspace\my_file.txt"))

# 파일 정보 가져오기
# import time
# import datetime

# 파일의 생성(c) 날짜
# ctime = os.path.getctime("rpa_basic/2_desktop/11_file_system.py")
# print(ctime)
# print(ctime)
# 날짜정보를 strftime을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 수정(m) 날짜
# mtime = os.path.getmtime("rpa_basic/2_desktop/11_file_system.py")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 접근(a) 날짜
# atime = os.path.getatime("rpa_basic/2_desktop/11_file_system.py")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기
# size = os.path.getsize("rpa_basic/2_desktop/11_file_system.py")
# print(size)# 바이트 단위로 파일 크기 가져오기

# 파일시스템2  4:16:59~
# 파일 목록 가져오기
# print(os.listdir())# 모든 폴더,파일목록 가져오기
# print(os.listdir("rpa_basic")) #주어진 폴더 밑의 폴더와 파일 목록 가져오기

# # 하위 폴더 모두 포함해서 파일 목록 가져오기
# result = os.walk("rpa_basic")#  "폴더"기준으로 모든 폴더,파일을 가져온다/ 현재 폴더
# #print(result) # -- <generator object _walk at 0x000001CC7A476340>가 출력됨
# # 아래처럼 root,dirs, files 로 프린트 해보면~~
# for root, dirs, files in result:
#     print(root, dirs, files)

# # 하위 폴더 모두 포함해서 파일 목록 가져오기
# result = os.walk(".")#  "현재폴더=pythonworkspace"기준으로 모든 폴더,파일을 가져온다
# #print(result) # -- <generator object _walk at 0x000001CC7A476340>가 출력됨
# # 아래처럼 root,dirs, files 로 프린트 해보면~~
# for root, dirs, files in result:
#     print(root, dirs, files)

# # 만약, 폴더 내에서 특정 파일들을 찾으려면?  4:23:10~
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk(os.getcwd()):# "." : 현재경로에서~~, "os.getcwd()" : 전체경로에서~~
#     if name in files:
#         result.append(os.path.join(root, name))
# print(result)

# 만약, 폴더 내에서 특정패턴을 가진 파일을 찾으려면?  
# *.xlsx , *.txt, 자동화*.png

# import fnmatch
# from typing import Pattern # 파일네임일치여부
# Pattern = "*.py" # .py로 끝나는 모든 파일
# result = []
# for root, dirs, files in os.walk("."):# "." : 현재경로에서~~, "os.getcwd()" : 전체경로에서~~
#     #[a.txt, b.txt, c.txt, 11_file_system.py,...]
#     for name in files:
#         if fnmatch.fnmatch(name, Pattern):# 이름과 패턴이 일치하면
#             result.append(os.path.join(root, name))
# print(result)

# # 파일 시스템3 4:29:33~~
# # 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("rpa_basic"))# rpa_basic은 폴더인가? --> True
# print(os.path.isfile("rpa_basic"))# rpa_basic은 파일인가? --> False

# print(os.path.isdir("run_btn.png"))# False 
# print(os.path.isfile("run_btn.png"))# True

# # 만약에 지정된 경로에 해당하는 파일/폴더 가 없다면?
# print(os.path.isdir("run_btnn.png"))# False
# print(os.path.isfile("run_btnn.png"))# False

# # 주어진 경로가 존재하는지?
# if os.path.exists("rpa_basic"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기 4:33:30 ~
# open("new_file.txt", "a").close()# 빈 파일 생성

# 파일명 변경 하기
# os.rename("new_file.txt", "new_file_rename.txt")# new_file.txt를  new_file_rename.txt로 이름 변경

# 파일 삭제 하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
#os.mkdir("test_folder")# 현재 경로 기준으로 폴더 생성

# 하위폴더를 가지는 폴더 생성하기
# os.mkdir("new_folders/a/b/c") #실패
# os.makedirs("new_folders/a/b/c") # 성공

# 폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folders")# 폴더 안이 비었을 때만 삭제가능

import shutil # shell utilites
# shutil.rmtree("new_folders")# 폴더 안이 비어 있지 않아도 완전 삭제 가능(!!모든 파일이 삭제 될수 있으므로 주의!!!)

# 파일시스템 4:40:58~
# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
#shutil.copy("run_btn.png", "test_folder")#원본 파일 경로, 대상 폴더 경로
# 어떤 파일을 폴더 안에 새로운 파일이름으로 복사하기
#shutil.copy("run_btn.png","test_folder/copied_run_btn.png")# 원본 경로, 대상 경로(변경된 파일명까지)
#shutil.copy("run_btn.png","test_folder/copied_run_btn2.png")

# shutil.copy("run_btn.png", "test_folder/copy.png")
# shutil.copy2("run_btn.png", "test_folder/copy2.png")# 원본 파일 경로, 대상 폴더()

# copy, copyfile : 메타정보 복사 x
# copy2 : 메타정보 복사 ㅇ 

# 폴더 복사
#shutil.copytree("test_folder", "test_folder2")#  원본 폴더 경로, 대상 폴더 경로
# shutil.copytree("test_folder", "test_folder3")


# 폴더 이동
#shutil.move("test_folder", "test_folder3")
#shutil.move("test_folder2", "test_folder3")
shutil.move("test_folder", "test_folder_rename")# 폴더 명이 변경되는 효과

