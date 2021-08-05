# create_account.py

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
