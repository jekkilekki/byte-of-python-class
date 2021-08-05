# login.py

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
