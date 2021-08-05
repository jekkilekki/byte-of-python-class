# insta.py

import cancel
import create_account
import login

def run():
         username = ''
         password = ''
         
         while True:
                  print('인스타그램에 오신 것을 환영합니다!')
                  choice = int(input('0 = 취소. 1 = 계정 생성. 2 = 로그인\n'))

                  if choice == 0: # 취소
                           cancel.cancel()
                           break
                  if choice == 1: # 사용자 계정
                           username, password = create_account.create_account()
                  if choice == 2: # 로그인
                           login.login(username, password)

run()
