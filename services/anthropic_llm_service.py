from anthropic import Anthropic
import os


class AnthropicLLMService:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    def get_answer(self, question_text: str) -> str:
        message = self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            system="Provide only the essential information in your response. Give the shortest possible answer without any explanation or additional context. For example, if asked 'When was Facebook established?', respond only with '2004'.",
            messages=[
                {
                    "role": "user",
                    "content": question_text
                }
            ]
        )
        return message.content[0].text
