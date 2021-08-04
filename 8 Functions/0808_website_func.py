# 0808_website_func.py

'''사용자 계정을 만들고 사용자를 로그인하는 프로그램입니다.

사용자 계정을 만듭니다(while 루프).
1. 사용자 이름을 생성합니다(입력 -> 변수).
2. 비밀번호 길이 > 8인 경우 비밀번호를 생성합니다(입력 -> 변수).
3. 계정 생성 메시지를 인쇄합니다.

로그인(while 루프).
1. 입력 == 사용자 이름인 경우 암호를 계속 진행합니다.
2. 입력 == 비밀번호를 입력하면 로그인합니다(for 루프, 3번).
3. 성공 메시지를 인쇄합니다.
'''

def run():
         username = ''
         password = ''
         
         while True:
                  print('인스타그램에 오신 것을 환영합니다!')
                  choice = int(input('0 = 취소. 1 = 계정 생성. 2 = 로그인\n'))

                  if choice == 0: # 취소
                           cancel()
                           break
                  if choice == 1: # 사용자 계정
                           username, password = create_account()
                  if choice == 2: # 로그인
                           login(username, password)

def create_account():
         # 사용자 계정
         # 1. 사용자 계정 생성
         print('인스타그램 계정을 만드세요.')

         # 1-1. 사용자 이름
         username = input('사용자 이름을 입력하세요.\n') 
         while len(username) < 5:
                  username = input('사용자 이름이 너무 짧아요. \n\
                                    사용자 이름을 입력하세요.\n')
                  if 'quit' == username:
                           break
                           
         print('사용자 이름은 {}입니다.'.format(username))

         # 1-2. 사용자 비밀번호
         password = input('사용자 비밀번호를 입력하세요.\n') 
         while len(password) < 8:
                  password = input('사용자 비밀번호가 너무 짧아요. \n\
                                    사용자 비밀번호를 입력하세요.\n')
                  if 'password' == password:
                           print('더 강력한 비밀번호를 선택하세요!')
                  if 'quit' == password:
                           break
                           
         print('사용자 비밀번호는 {}입니다.'.format('*'*len(password)))
         print('축하세요. 계정이 생성되었습니다!\n\n\n')

         return username, password

def login(uname, pword):
         # 로그인
         # 2. 로그인
         print('인스타그램에 로그인하세요.')
         un = input('사용자 이름 입력하세요: ')

         while un != uname:
                  print('그 사용자 이름이 없습니다.')
                  un = input('사용자 이름 입력하세요: ')

         pw = input('사용자 비밀번호를 입력하세요: ')

         for i in range(0,5):
                  if pw != pword:
                           print('비밀번호는 틀려요.')
                           pw = input('사용자 비밀번호를 입력하세요: ')
                  else:
                           break
         else:
                  print('비밀버호가 5개 틀렸어 죽었다.')
                  #continue

         print('\n인스타그램에서 환영 하세요, {}!\n\n'.format(uname))
         #break

def cancel():
         # 0: 취소
         print('취소했습니다.')

run()















