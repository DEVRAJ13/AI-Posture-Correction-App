class PostureAgent:

    def execute(
        self,
        state
    ):

        posture = state["posture"]

        if posture == "bad":
            state["bad_count"] += 1

        else:
            state["bad_count"] = 0

        return state