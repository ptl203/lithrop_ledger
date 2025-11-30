import google.generativeai as genai
import time

class NewsFetcher:
    """
    This module is responsible for all interactions with the Google Gemini API.
    """
    def __init__(self, api_key):
        """
        Initializes the Gemini client with the provided API key.
        """
        genai.configure(api_key=api_key)
        #self.model = genai.GenerativeModel('gemini-3.0-pro')
        self.model = genai.GenerativeModel('gemini-pro-latest')

    def get_daily_news(self, prompt, retries=3, delay=2):
        """
        Sends a precisely engineered prompt to the `gemini-3.0-pro` model.
        Implements a retry mechanism with exponential backoff to handle transient API errors.
        Returns the raw news content, expected to be in Markdown format, upon a successful API response.
        """
        for i in range(retries):
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as e:
                print(f"Error fetching news from Gemini: {e}")
                if i < retries - 1:
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2
                else:
                    print("All retries failed.")
                    return None
