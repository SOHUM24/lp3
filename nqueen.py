class NQBacktracking:
    def __init__(self, N, x_, y_):
        self.N = N
        self.x = x_
        self.y = y_
        self.ld = [0] * (2 * N - 1)
        self.rd = [0] * (2 * N - 1)
        self.cl = [0] * N

    def printSolution(self, board):
        print("N Queen Backtracking Solution:\nGiven initial position of 1st queen at row:",
              self.x, "column:", self.y, "\n")
        for line in board:
            print(" ".join(map(str, line)))

    def solveNQUtil(self, board, col):
        if col >= self.N:
            return True
        if col == self.y:
            return self.solveNQUtil(board, col + 1)
        for i in range(self.N):
            if i == self.x:
                continue
            if (self.ld[i - col + self.N - 1] != 1 and self.rd[i + col] != 1) and self.cl[i] != 1:
                board[i][col] = 1
                self.ld[i - col + self.N -
                        1] = self.rd[i + col] = self.cl[i] = 1
                if self.solveNQUtil(board, col + 1):
                    return True
                board[i][col] = 0
                self.ld[i - col + self.N -
                        1] = self.rd[i + col] = self.cl[i] = 0
        return False

    def solveNQ(self):
        board = [[0 for _ in range(self.N)] for _ in range(self.N)]
        board[self.x][self.y] = 1
        self.ld[self.x - self.y + self.N -
                1] = self.rd[self.x + self.y] = self.cl[self.x] = 1
        if not self.solveNQUtil(board, 0):
            print("Solution does not exist")
            return False
        self.printSolution(board)
        return True


if __name__ == "__main__":
    while True:
        print("\nN-Queen Backtracking Solver Menu:")
        print("1. Solve N-Queens")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            N = int(input("Enter the size of the chessboard (N): "))
            x = int(
                input("Enter the row for the initial position of the 1st queen: "))
            y = int(
                input("Enter the column for the initial position of the 1st queen: "))
            if x < 0 or x >= N or y < 0 or y >= N:
                print("Invalid initial queen position. Try again.")
            else:
                NQBt = NQBacktracking(N, x, y)
                NQBt.solveNQ()

        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")
