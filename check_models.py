import google.generativeai as genai
import os
from dotenv import load_dotenv

def check_models():
    """
    Lists the available Gemini models that support content generation.
    """
    try:
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            print("Error: GEMINI_API_KEY not found in your .env file.")
            return

        genai.configure(api_key=api_key)

        print("Checking for available models that support 'generateContent'...")
        models_found = False
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
                models_found = True
        
        if not models_found:
            print("No models supporting 'generateContent' were found for your API key.")
            print("Please check that the Gemini API is enabled in your Google Cloud project and that billing is set up.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("This could be due to an invalid API key or a problem with your Google Cloud project setup.")

if __name__ == "__main__":
    check_models()
