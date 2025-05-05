def nQueen(n):

    #defining recursive function to place queens on board
    def placeQueens(row_index):
        if row_index == n:
            solutions.append(filled_board[:])
            return
        for column_index in range(n):
            if column[column_index] + diagonal[row_index + column_index] + anti_diagonal[n - row_index + column_index] == 0:
                column[column_index] = diagonal[row_index + column_index] = anti_diagonal[n - row_index + column_index] = 1
                filled_board.append(column_index + 1)
                placeQueens(row_index + 1)
                # Backtrack: remove the queen and the constraints
                filled_board.pop()
                column[column_index] = diagonal[row_index + column_index] = anti_diagonal[n - row_index + column_index] = 0

    #solutions list
    solutions = []
    #final board state
    filled_board = []
    #constaints
    column = [0] * n
    diagonal = [0] * (2 * n)
    anti_diagonal = [0] * (2 * n)

    #begin placing queens on board starting from first row
    placeQueens(0)
    if not solutions:
        return "There are no solutions for this value of n"
    return solutions