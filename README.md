# Lithrop Ledger: Automated AI-Powered Newsletter

## Project Overview

The Lithrop Ledger is a Python-based application that automates the generation and distribution of a daily news-summary email. It leverages a Large Language Model (LLM) to generate up-to-date content on a variety of topics, formats it into a professional HTML newsletter, and dispatches it to a recipient list. This project demonstrates skills in API integration, text processing, email automation, and modular application design.

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
    *   `RECIPIENT_EMAIL`: The email address you are sending to.
    *   `TEST_MODE`: Set to `True` to use mock data, or `False` to generate live news.

5.  **Customize the Prompt (Optional)**
    Edit the `prompt.md` file to change the instructions for the content, tone, and structure of the generated newsletter.

6.  **Run the Application**
    ```bash
    python3 main.py
    ```
    The script will execute, generate the newsletter, and send the email. Logs are stored in the `logs/` directory.

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