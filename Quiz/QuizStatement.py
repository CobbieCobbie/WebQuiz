from Quiz.Statement import Statement

class QuizStatement(Statement):
    def __init__(self, id, trueStatement, falseStatement, description, right_answer = False):
        super().__init__(id, trueStatement, falseStatement, description)
        self.right_answer = right_answer
        self.player_choice = False

    def __repr__(self):
        return f"QuizStatement(id={self.id}, TrueStatement='{self.trueStatement}', FalseStatement='{self.falseStatement}', Description='{self.description}', RightAnswer={self.right_answer}, PlayerChoice={self.player_choice})"