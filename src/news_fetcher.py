from google import genai
from google.genai import types
import time

class NewsFetcher:
    """
    This module is responsible for all interactions with the Google Gemini API.
    """
    def __init__(self, api_key):
        """
        Initializes the Gemini client with the provided API key.
        """
        self.client = genai.Client(api_key=api_key)

    def get_daily_news(self, prompt, retries=3, delay=2):
        """
        Sends a precisely engineered prompt to the model.
        Implements a retry mechanism with exponential backoff to handle transient API errors.
        Returns the raw news content, expected to be in Markdown format, upon a successful API response.
        """
        grounding_tool = types.Tool(
            google_search=types.GoogleSearch()
        )
        config = types.GenerateContentConfig(
            tools=[grounding_tool]
        )

        for i in range(retries):
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config=config
                )
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
