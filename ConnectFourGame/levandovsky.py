import ConnectFour
import numpy as np

class levandovsky(ConnectFour.Player):
    def __init__(self):
        #any initiization you want to perform
        pass

    def taketurn(self,board,player):
        #board is a 2d numpy array with size of (ROWCOUNT,COLUMNCOUNT)
        # [[0,0,1,0,0,0],
        # [0,0,1,0,0,0],
        # [0,0,1,0,2,0],
        # [0,0,1,0,0,0],
        # [0,0,1,0,0,0].
        # return a number between 0-(n-1) where n is the number or columns

        # moves = np.array([i for i in range(ConnectFour.COLUMN_COUNT)])

        # #if column is full... then its not possible
        # filter = np.min(board.T,axis=1) == 0

        # filteredMoves = moves[filter]
        # return np.random.choice(filteredMoves)

        maxMove = 0
        maxEval = -100
        maxDepth = 5





        possibleMoves, moveList = self.expandMoves(board,player)

        i = 0
        for childBoard in possibleMoves:
            otherPlayer = (player%2)+1

            #now start minmax of the expanded moves
            eval = self.expandMinMax(childBoard,maxDepth - 1,False,otherPlayer)
            
            if eval > maxEval:
                maxEval = eval
                maxMove = moveList[i]

            i+=1

        return maxMove
                

    def expandMinMax(self, board, depth, isMaximizing, player):
        
        otherPlayer = (player%2) + 1

        didIWin = self.winning_move(board)
        
        if depth == 0 or didIWin:
            
            if didIWin == True and isMaximizing == True:
                return -1
            elif didIWin == True and isMaximizing == False:
                return 1
            else:
                return 0

        

        if isMaximizing:
            maxEval = -100

            possibleMoves, moveList = self.expandMoves(board,player)

            for childBoard in possibleMoves:
                eval = self.expandMinMax(childBoard,depth-1,False,otherPlayer)
                maxEval = max(maxEval,eval)

            return maxEval

        elif isMaximizing == False:
            minEval = 100

            

            possibleMoves, moveList = self.expandMoves(board,player)

            for childBoard in possibleMoves:
                eval = self.expandMinMax(childBoard,depth-1,True,otherPlayer)
                minEval = min(minEval,eval)

            return minEval



        pass


    def expandMoves(self, board, player):
        moves = np.array([i for i in range(ConnectFour.COLUMN_COUNT)])

        #if column is full... then its not possible
        filter = np.min(board.T,axis=1) == 0

        possibleMoves = moves[filter] #an array with values between 0 and 6


        arrayOfNewBoardStates = []
        for col in possibleMoves:
            row = self.get_next_open_row(board,col)  # return the board upsidedown

            newBoard = self.drop_piece(board,row,col,player)

            arrayOfNewBoardStates.append(newBoard)


        return arrayOfNewBoardStates, possibleMoves



    def drop_piece(self,board, row, col, piece):
        newBoard = np.copy(board)
        newBoard[row][col] = piece
        return newBoard
    
    
    def get_next_open_row(self,board, col):
        for r in range(ConnectFour.ROW_COUNT):
            if board[r][col] == 0:
                return r

    def winning_move(self,board):
        # Check horizontal locations for win
        for c in range(ConnectFour.COLUMN_COUNT-3):
            for r in range(ConnectFour.ROW_COUNT):
                if board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1:
                    return True
                if board[r][c] == 2 and board[r][c+1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2:
                    return True
    
        # Check vertical locations for win
        for c in range(ConnectFour.COLUMN_COUNT):
            for r in range(ConnectFour.ROW_COUNT-3):
                if board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c] == 1:
                    return True
                if board[r][c] == 2 and board[r+1][c] == 2 and board[r+2][c] == 2 and board[r+3][c] == 2:
                    return True
    
        # Check positively sloped diaganols
        for c in range(ConnectFour.COLUMN_COUNT-3):
            for r in range(ConnectFour.ROW_COUNT-3):
                if board[r][c] == 1 and board[r+1][c+1] == 1 and board[r+2][c+2] == 1 and board[r+3][c+3] == 1:
                    return True
                if board[r][c] == 2 and board[r+1][c+1] == 2 and board[r+2][c+2] == 2 and board[r+3][c+3] == 2:
                    return True
    
        # Check negatively sloped diaganols
        for c in range(ConnectFour.COLUMN_COUNT-3):
            for r in range(3, ConnectFour.ROW_COUNT):
                if board[r][c] == 1 and board[r-1][c+1] == 1 and board[r-2][c+2] == 1 and board[r-3][c+3] == 1:
                    return True
                if board[r][c] == 2 and board[r-1][c+1] == 2 and board[r-2][c+2] == 2 and board[r-3][c+3] == 2:
                    return True

        return False


if __name__ == "__main__":
    #we need to run __main__.py, if that is the case this is ingored
    #but if we run levandovsky.py this is not ignored
    myPlayer = levandovsky()
    myBoard = ConnectFour.ConnectFour(False).create_board()
    
    myBoard[0][0] = 2
    myBoard[0][1] = 2
    myBoard[0][2] = 2

    myPlayer.taketurn(myBoard,1)


    pass


