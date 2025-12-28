# Lithrop Ledger: Automated AI-Powered Newsletter

## Project Status

This project is complete. The application is fully functional and meets all the requirements outlined in the initial design.

## Project Overview

The Lithrop Ledger is a Python-based application that automates the generation and distribution of a daily news-summary email. It leverages a Large Language Model (LLM) to generate up-to-date content on a variety of topics, formats it into a professional HTML newsletter, and dispatches it to a recipient list. This project demonstrates skills in API integration, text processing, email automation, and modular application design.

## How it Works

The application operates in a simple, linear workflow:

1.  **Initialization:** The `main.py` script is executed. It loads environment variables from the `.env` file, including API keys and email credentials.
2.  **Content Fetching:**
    *   If `TEST_MODE` is `False`, the `NewsFetcher` module sends a detailed prompt from `prompt.md` to the Google Gemini API. The API returns a news summary in Markdown format.
    *   If `TEST_MODE` is `True`, the application skips the API call and uses mock data from `templates/mock_news.md`.
3.  **HTML Formatting:** The `HTMLFormatter` module takes the Markdown content, parses it into a structured dictionary, and injects it into the `newsletter_template.html` Jinja2 template. The `premailer` library is then used to inline all CSS for maximum email client compatibility.
4.  **Email Dispatch:** The `EmailDispatcher` module establishes a secure connection to an SMTP server and sends the final HTML newsletter to the configured recipient.

## Features

*   **Dynamic Content Generation:** Utilizes the Google Gemini API to generate news content based on a detailed and customizable prompt file (`prompt.md`).
*   **Multi-Section Newsletter:** The generated content includes several distinct sections:
    *   Daily Market Update (S&P 500, NASDAQ, etc.)
    *   Sports News
    *   World News
    *   US News
    *   Finance News
    *   Technology Business News
    *   An "Uplifting" News story
*   **Markdown to HTML Conversion:** The LLM's markdown output is parsed and converted into a structured HTML document.
*   **HTML Templating:** Uses the Jinja2 templating engine to inject the generated content into a polished HTML email template.
*   **Email-Compatible Styling:** The `premailer` library is used to convert CSS styles into inline `style` attributes, ensuring maximum compatibility across various email clients.
*   **Email Dispatch:** Sends the final HTML newsletter via an SMTP server (configured for Gmail in the current implementation).
*   **Configuration Management:** Securely manages API keys and other configuration variables using an `.env` file.
*   **Test Mode:** Includes a test mode that uses local mock data (`templates/mock_news.md`) instead of making live API calls, allowing for rapid development and testing of the formatting and email-sending logic.

## Technologies Used

*   **Python 3**
*   **Google Generative AI SDK (`google-generativeai`):** For interacting with the Gemini LLM.
*   **Jinja2:** For HTML templating.
*   **`markdown2`:** For converting markdown text to HTML.
*   **`premailer`:** To inline CSS for email clients.
*   **`python-dotenv`:** For managing environment variables.
*   **`smtplib`:** Python's built-in library for sending emails via SMTP.

## Setup and Usage

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd lithrop-ledger
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    python3 -m venv LL_env
    source LL_env/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a file named `.env` in the root of the project and add the following variables.

    ```ini
    # .env
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    EMAIL_APP_PASSWORD="YOUR_EMAIL_APP_PASSWORD"
    SMTP_USERNAME="your.email@gmail.com"
    RECIPIENT_EMAIL="recipient.email@example.com"
    TEST_MODE=False
    ```
    *   `GEMINI_API_KEY`: Your API key for the Google Gemini service.
    *   `EMAIL_APP_PASSWORD`: An application-specific password for your email account if using 2-Factor Authentication (e.g., for Gmail).
    *   `SMTP_USERNAME`: The email address you are sending from.
    *   `RECIPIENT_EMAIL`: The email address(es) you are sending to. Multiple recipients can be specified by separating them with commas (e.g., "recipient1@example.com,recipient2@example.com").

5.  **Run the Application**
    ```bash
    python3 main.py
    ```
    The script will execute, generate the newsletter, and send the email. Logs are stored in the `logs/` directory.

## Customization

### Prompt Engineering

The heart of the content generation lies in the `prompt.md` file. This file contains a detailed set of instructions that the Gemini LLM uses to generate the newsletter. You can customize the following aspects:

*   **Topics:** Add, remove, or change the news topics.
*   **Tone and Style:** Modify the instructions to change the writing style (e.g., more formal, more casual).
*   **Content:** Change the number of stories per topic, the length of the stories, etc.

### Testing

To test the application without using the Gemini API, you can enable test mode. This is useful for testing changes to the HTML template or the email sending logic.

To enable test mode, set the `TEST_MODE` variable in your `.env` file to `True`:

```ini
# .env
TEST_MODE=True
```

When test mode is enabled, the application will use the content from `templates/mock_news.md` instead of calling the Gemini API.

## Future Improvements

*   **Add more news sources:** The current implementation uses the Gemini API's knowledge base. Future versions could integrate with other news APIs to provide a wider range of sources.
*   **User-specific content:** The newsletter could be customized for each recipient based on their interests.
*   **Web interface:** A web interface could be built to allow users to subscribe, unsubscribe, and manage their preferences.
*   **More sophisticated scheduling:** The application could be integrated with a more robust scheduling system like Celery or APScheduler.

## Project Structure

```
.
├── .env                  # Environment variables (API keys, etc.) - Not versioned
├── .gitignore            # Files and directories to be ignored by Git
├── main.py               # Main application entry point
├── prompt.md             # The master prompt for the Gemini LLM
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── src/                  # Source code directory
│   ├── email_dispatcher.py # Handles sending the email via SMTP
│   ├── html_formatter.py   # Parses markdown and formats the HTML newsletter
│   └── news_fetcher.py     # Fetches content from the Gemini API
├── templates/            # Template files
│   ├── mock_news.md        # Mock news content for testing
│   └── newsletter_template.html # HTML template for the email
└── logs/                 # Log files - Not versioned
```
