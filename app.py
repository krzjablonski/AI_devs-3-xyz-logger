from dotenv import load_dotenv
import os
from services.http_service import HttpService
from services.anthropic_llm_service import AnthropicLLMService

# Load environment variables from .env file to access configuration settings
load_dotenv()


def main():
    """
    Main function that orchestrates the process of:
    1. Fetching a question from a webpage
    2. Getting an answer from Claude AI
    3. Posting the answer back to the API and extracting the flag
    """
    # Initialize service objects for HTTP requests and LLM interactions
    http_service = HttpService()
    llm_service = AnthropicLLMService()

    # Fetch the question text from the specified API endpoint
    question_text = http_service.get_question_text(os.getenv('API_URL'))

    if question_text is None:
        # "Question not found on the page"
        print("Nie znaleziono pytania na stronie")
        return

    # Get answer from Claude AI model
    try:
        answer = llm_service.get_answer(question_text)

    except Exception as e:
        print(f"Error getting answer from Claude: {str(e)}")
        return

    # Post the answer back to the API and get the flag
    try:
        # Prepare form data with credentials and the answer
        form_data = {
            "username": os.getenv('XYZ_LOGIN'),
            "password": os.getenv('XYZ_PASSWORD'),
            "answer": answer
        }

        # Set headers for form submission
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Send POST request with the answer and get the flag
        response = http_service.post_data(
            os.getenv('API_URL'), form_data, headers=headers)

        # Log the server's response (containing the flag)
        print(f"Server response: {response}")

    except Exception as e:
        print(f"Error posting data to API: {str(e)}")


# Execute main function only if script is run directly (not imported)
if __name__ == "__main__":
    main()
