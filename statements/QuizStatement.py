from statements.Statement import Statement

class QuizStatement(Statement):
    def __init__(self, id, trueStatement, falseStatement, description, chosenStatement = "", rightAnswer = False):
        super().__init__(id, trueStatement, falseStatement, description)
        self.chosenStatement = chosenStatement
        self.rightAnswer = rightAnswer
        self.playerChoice = False

    def __repr__(self):
        return f"QuizStatement(id={self.id}, TrueStatement='{self.trueStatement}', FalseStatement='{self.falseStatement}', Description='{self.description}', ChosenStatement='{self.chosen_statement}', RightAnswer={self.rightAnswer}, PlayerChoice={self.playerChoice})"