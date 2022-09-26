class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.matrix = [['.'] * n for _ in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        self.matrix[row][col] = player
        if self.checkRow(row, player):
            return player
        if self.checkCol(col, player):
            return player
        if row == col and self.checkDiag(player):
            return player
        if self.n - row - 1 == col and self.checkAntiDiag(player):
            return player
        return 0
    
    def checkRow(self, row, player):
        for c in range(self.n):
            if self.matrix[row][c] != player:
                return False
            
        return True
    
    def checkCol(self, col, player):
        for row in range(self.n):
            if self.matrix[row][col] != player:
                return False
        return True
    
    def checkDiag(self, player):
        for r in range(self.n):
            if self.matrix[r][r] != player:
                return False
        return True

    def checkAntiDiag(self, player):
        for r in range(self.n):
            if self.matrix[r][self.n - r - 1] != player:
                return False
        return True

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)