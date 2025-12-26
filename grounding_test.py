import logging
import os
from google import genai
from google.genai import types

#import google.generativeai as genai
#from google.generativeai import types

from dotenv import load_dotenv

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
log_file = os.path.join('logs', 'grounding_test.log')
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting grounding_test.py script.")

load_dotenv(override=True)
logging.info("Loaded environment variables.")

try:
    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        logging.error("GEMINI_API_KEY not found in environment variables.")
        raise ValueError("GEMINI_API_KEY not found")

    client = genai.Client(api_key=gemini_key)
    logging.info("Successfully created genai.Client.")

    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )
    logging.info("Created grounding tool.")

    config = types.GenerateContentConfig(
        tools=[grounding_tool]
    )
    logging.info("Created GenerateContentConfig.")

    logging.info("Generating content...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="What is todays date?",
        config=config,
    )
    logging.info("Successfully generated content.")

    print(response.text)
    logging.info(f"Response text: {response.text}")

except Exception as e:
    logging.error(f"An error occurred: {e}", exc_info=True)

logging.info("grounding_test.py script finished.")
