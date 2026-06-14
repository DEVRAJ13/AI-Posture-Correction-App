from llm.ollama_client import OllamaCoach

coach = OllamaCoach()

class CoachAgent:

    def execute(
        self,
        state
    ):

        if state["bad_count"] > 60:

            advice = coach.generate_advice(
                state["bad_count"]
            )

            state["advice"] = advice

        return state