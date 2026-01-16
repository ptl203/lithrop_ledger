from google import genai
from google.genai import types
import time
import datetime

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
        Returns the raw news content in JSON format.
        """
        grounding_tool = types.Tool(
            google_search=types.GoogleSearch()
        )
        
        # Inject today's date for context
        today = datetime.datetime.now().strftime("%B %d, %Y")
        prompt_with_date = prompt.replace("{{date}}", today)

        config = types.GenerateContentConfig(
            tools=[grounding_tool],
            response_mime_type="application/json"
        )

        for i in range(retries):
            try:
                response = self.client.models.generate_content(
                    model="gemini-3-pro-preview", # Flash is faster and good for structured data
                    contents=prompt_with_date,
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
