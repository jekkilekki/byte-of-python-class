# 1202_robots.py

class Robot:

         pop = 0 # 인구

         def __init__(self, name):
                  self.name = name
                  print('{} 만드는 중'.format(self.name))
                  Robot.pop += 1

         def die(self):
                  print('{} 꺼지고 있어요.'.format(self.name))
                  Robot.pop -= 1

                  if Robot.pop == 0:
                           print('{} 마지막이다.'.format(self.name))
                  else:
                           print('로봇 {:d}개 남아요.'.format(Robot.pop))

         def say_hi(self):
                  print('안녕하세요. 내 이름은 {}입니다.'.format(self.name))

         @classmethod
         def how_many(cls):
                  print('로봇 {:d}개 남아요.'.format(Robot.pop))

robot1 = Robot('R2-D2')
robot1.say_hi()
Robot.how_many()

robot2 = Robot('C-3PO')
robot2.say_hi()
Robot.how_many()

print('로봇들은 지금 일 하고있다.')
print('일이 다 끝났다.')

robot1.die()
robot2.die()
Robot.how_many()



         
         
