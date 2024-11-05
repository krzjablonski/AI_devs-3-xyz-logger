from dotenv import load_dotenv
import os
from services.http_service import HttpService
from services.anthropic_llm_service import AnthropicLLMService

# Load environment variables from .env file
load_dotenv()


def main():
    http_service = HttpService()
    llm_service = AnthropicLLMService()

    # Get question text from the webpage
    question_text = http_service.get_question_text(os.getenv('API_URL'))

    if question_text is None:
        print("Nie znaleziono pytania na stronie")
        return

    # Get answer from Claude
    try:
        answer = llm_service.get_answer(question_text)

    except Exception as e:
        print(f"Error getting answer from Claude: {str(e)}")
        return

    try:
        form_data = {
            "username": os.getenv('XYZ_LOGIN'),
            "password": os.getenv('XYZ_PASSWORD'),
            "answer": answer
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = http_service.post_data(
            os.getenv('API_URL'), form_data, headers=headers)

        # Print response regardless of type
        print(f"Server response: {response}")

    except Exception as e:
        print(f"Error posting data to API: {str(e)}")


if __name__ == "__main__":
    main()
