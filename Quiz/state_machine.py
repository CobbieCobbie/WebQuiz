from statemachine import StateMachine, State, Event


class QuizStateMachine(StateMachine):
    "A quiz state machine that manages the quiz states."
    welcome = State(name = "welcome", initial=True)
    quiz_start = State(name = "quiz_start")
    quiz_eval = State(name = "quiz_eval")
    result = State(name = "result")

    start = Event(
            welcome.to(quiz_start),
            name="Start the quiz and initialize the statements"
    )

    eval = Event(
        quiz_start.to(quiz_eval),
        name="Evaluate the user statement choice"
    )

    end = Event(
        quiz_eval.to(result),
        name="Show the overall results and end the quiz"
    )

    reset = Event(
        result.to(welcome)
        | quiz_start.to(welcome)
        | quiz_eval.to(welcome),
        name="Reset the quiz to the initial state"
    )

    cycle = Event(
        welcome.to(quiz_start, event=start) 
        | quiz_start.to(quiz_eval, event=eval)
        | quiz_eval.to(result, event=end)
        | result.to(welcome, event=reset),
        name="Cycle through the states"
    )

def on_transition(self, event_data, event: Event):
        # The `event` parameter can be declared as `str` or `Event`, since `Event` is a subclass of `str`
        # Note also that in this example, we're using `on_transition` instead of `on_cycle`, as this
        # binds the action to run for every transition instead of a specific event ID.
        assert event_data.event == event
        return (
            f"Running {event.name} from {event_data.transition.source.id} to "
            f"{event_data.transition.target.id}"
        )
