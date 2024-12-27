thehomework =  {'7': '' ,'8': '' ,'9': '' ,'4': '' ,'5': '' ,'6': '' , '1': '' , '2': '' , '3': '' }
homework_keys = []
for key in thehomework:
   homework_keys.append(key) 
   def printBoard(homework):
       print(homework['7'] + '|' + homework['8'] + '|' + homework['9'])
       print('-+-+-')
       print(homework['4'] + '|' + homework['5'] + '|' + homework['6'])
       print('-+-+-')
       print(homework['1'] + '|' + hommework['2'] + '|' + homework['3'])
def game():

    turn = 'x'
    count = 0
    for i in range(10):
     print homework[thehomework]
     print("its youre turn," + turn + ".move to wich place?")
     move = input()
     if thehomework[move] =='':
        thehomework[move] = turn
        count+=1
        else:
print("that place is already filled")
