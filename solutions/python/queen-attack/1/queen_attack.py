class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        #rows = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.queen = (row, column)

    def can_attack(self, another_queen):
        if self.queen == another_queen.queen:
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.queen[0] == another_queen.queen[0] or self.queen[1] == another_queen.queen[1]:
            return True
        return abs(self.queen[0] - another_queen.queen[0]) == abs(self.queen[1] - another_queen.queen[1])