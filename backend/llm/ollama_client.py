from langchain_ollama import OllamaLLM

class OllamaCoach:

    def __init__(self):

        self.llm = OllamaLLM(
            model="gemma3:1b"
        )

    def generate_advice(
        self,
        duration
    ):

        prompt = f"""
        User posture has been poor
        for {duration} seconds.

        Give short advice.
        """

        return self.llm.invoke(prompt)