# my_369.py

def test_369(i):
    if str(i)[-1] == '3' or str(i)[-1] == '6' or str(i)[-1] == '9':
        return True
    else:
        return False
    
# "String" [-1]
for i in range(1,200):
    # if i % 3 == 0: # math
    if test_369(i):
        print("clap")
    else:
        continue
        print(i)