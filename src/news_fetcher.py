from google import genai
from google.genai import types
import time
import datetime
import re
import json

class NewsFetcher:
    """
    This module is responsible for all interactions with the Google Gemini API.
    """
    def __init__(self, api_key):
        """
        Initializes the Gemini client with the provided API key.
        Sets up a persistent chat session with Google Search enabled.
        """
        self.client = genai.Client(api_key=api_key)
        
        # Configure the tool
        grounding_tool = types.Tool(
            google_search=types.GoogleSearch()
        )
        
        # Initialize chat with tool config
        # Using gemini-pro-latest as requested
        # Note: Removed response_mime_type="application/json" as it is incompatible with tools in this model
        self.chat = self.client.chats.create(
            model="gemini-pro-latest",
            config=types.GenerateContentConfig(
                tools=[grounding_tool]
            )
        )

    def get_daily_news(self, prompt, retries=3, delay=2):
        """
        Sends a precisely engineered prompt to the persistent chat session.
        Implements a retry mechanism with exponential backoff to handle transient API errors.
        Returns the raw news content in JSON format.
        """
        # Inject today's date for context
        today = datetime.datetime.now().strftime("%B %d, %Y")
        prompt_with_date = prompt.replace("{{date}}", today)

        for i in range(retries):
            try:
                # Use the persistent chat session
                response = self.chat.send_message(prompt_with_date)
                text = response.text
                
                # Attempt to extract JSON if wrapped in markdown or mixed with text
                # Look for JSON block
                json_match = re.search(r'\{.*\}', text, re.DOTALL)
                if json_match:
                    json_str = json_match.group(0)
                else:
                    json_str = text # fallback to raw text if no braces found
                
                # Verify it is valid JSON (optional but good for debugging)
                try:
                    json.loads(json_str)
                    return json_str
                except json.JSONDecodeError:
                    print(f"Warning: Response might not be valid JSON. Raw text: {text[:100]}...")
                    # If extraction failed, maybe return the raw text and let the formatter handle error or try again?
                    # But the formatter expects JSON.
                    # We'll return the extracted string anyway, or the raw text if no match.
                    return json_str

            except Exception as e:
                print(f"Error fetching news from Gemini: {e}")
                if i < retries - 1:
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2
                else:
                    print("All retries failed.")
                    return None
