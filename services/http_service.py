import requests
from bs4 import BeautifulSoup
import re


class HttpService:
    def __init__(self):
        pass

    def get_data(self, url: str) -> dict:
        response = requests.get(url)
        return response.json()

    def get_question_text(self, url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        question_tag = soup.find('p', id='human-question')
        if question_tag:
            return question_tag.text.strip()
        return None

    def _extract_flag(self, text: str) -> str:
        """
        Extract flag from text in format {{FLG:NAME_OF_THE_FLAG}}

        Args:
            text (str): Text containing the flag

        Returns:
            str: Extracted flag or None if not found
        """
        flag_pattern = r'\{\{FLG:(.*?)\}\}'
        match = re.search(flag_pattern, text)
        return match.group(1) if match else None

    def post_data(self, url: str, data: dict, headers: dict = None) -> str:
        """
        Send a POST request with form data to the specified URL.

        Args:
            url (str): The URL to send the POST request to
            data (dict): The data to be sent as form data
            headers (dict, optional): Additional headers for the request

        Returns:
            str: The extracted flag from the response or None if not found
        """
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        response_text = response.text
        return self._extract_flag(response_text)
