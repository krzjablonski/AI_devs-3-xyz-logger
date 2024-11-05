from anthropic import Anthropic
import os


class AnthropicLLMService:
    """
    Service class for interacting with Anthropic's Claude AI model.
    Handles the generation of concise answers to questions.
    """

    def __init__(self):
        """
        Initialize the Anthropic client using the API key from environment variables.
        """
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    def get_answer(self, question_text: str) -> str:
        """
        Get a concise answer from Claude AI for the given question.

        Args:
            question_text (str): The question to be answered

        Returns:
            str: The AI-generated answer, formatted as a concise response

        Note:
            The system prompt instructs Claude to provide minimal, direct answers
            without explanations or additional context.
        """
        message = self.client.messages.create(
            model="claude-3-sonnet-20240229",  # Using the latest Claude 3 Sonnet model
            max_tokens=1000,  # Limit response length
            system="Provide only the essential information in your response. Give the shortest possible answer without any explanation or additional context. For example, if asked 'When was Facebook established?', respond only with '2004'.",
            messages=[
                {
                    "role": "user",
                    "content": question_text
                }
            ]
        )
        return message.content[0].text
