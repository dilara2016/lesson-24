theBoard =  {'7': '' ,'8': '' ,'9': '' ,'4': '' ,'5': '' ,'6': '' , '1': '' , '2': '' , '3': '' }
board_keys = []
for key in theBoard:
   board_keys.append(key) 
   def printBoard(board):
       print(board['7'] + '|' + board['8'] + '|' + board['9'])
       print('-+-+-')
       print(board['4'] + '|' + board['5'] + '|' + board['6'])
       print('-+-+-')
       print(board['1'] + '|' + board['2'] + '|' + board['3'])
def game():

    turn = 'x'
    count = 0
    for i in range(10):
     printBoard[theBoard]
     print("its youre turn," + turn + ".move to wich place?")
     move = input()
     if theBoard[move] =='':
        theBoard[move] = turn
        count+=1
        else:
print("that place is already filled")