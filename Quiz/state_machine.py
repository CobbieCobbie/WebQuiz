from statemachine import StateMachine, State


class QuizStateMachine(StateMachine):
    "A quiz state machine that manages the quiz states."
    welcome = State(initial=True)
    mark = State()
    eval = State()
    end = State()

    cycle = (
        welcome.to(mark) 
        | mark.to(eval)
        | eval.to(end)
        | end.to(welcome)
    )

    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
        message = ". " + message if message else ""
        return f"Due to {event} from state {source.id} to state {target.id}{message}"
    
    def on_welcome(self):
        print("Welcome state entered.")
        return self.before_cycle("on_welcome", self.welcome, self.mark, "Welcome to the quiz.")
    
    def on_mark(self):
        print("Mark state entered.")
        return self.before_cycle("on_mark", self.mark, self.eval, "Marking the statements.")
    
    def on_eval(self):
        print("Eval state entered.")
        return self.before_cycle("on_eval", self.eval, self.end, "Evaluating the user statement choice.")
    
    def on_end(self):
        print("End state entered.")
        return self.before_cycle("on_end", self.end, self.welcome, "End of the quiz. Thanks for playing!")
