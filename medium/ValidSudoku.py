class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) == 0:
            return False
        length = len(board)
        for i in range(length):
            row_nums = [False] * 10
            col_nums = [False] * 10
            for j in range(length):
                if board[i][j] != '.':
                    index = int(board[i][j])
                    if row_nums[index]:
                        return False
                    else:
                        row_nums[index] = True

                if board[j][i] != '.':
                    if col_nums[int(board[j][i])]:
                        return False
                    col_nums[int(board[j][i])] = True
        for i in range(length // 3):
            for j in range(length // 3):
                cell_nums = [False] * 10
                for m in range(3*i, 3*i+3):
                    for n in range(3*j, 3*j+3):
                        if board[m][n] != '.':
                            if cell_nums[int(board[m][n])]:
                                return False
                            cell_nums[int(board[m][n])] = True
        return True
s = Solution()
board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(board))              