import os
from dotenv import load_dotenv
import logging
from src.news_fetcher import NewsFetcher
from src.html_formatter import HTMLFormatter
from src.email_dispatcher import EmailDispatcher
from datetime import date

def main():
    """
    Main function to orchestrate the newsletter generation and sending process.
    """
    # Setup logging
    log_file = os.path.join('logs', 'automation.log')
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info("Starting newsletter generation process...")

    # Load environment variables
    load_dotenv(override=True)
    gemini_key = os.getenv("GEMINI_API_KEY")
    app_password = os.getenv("EMAIL_APP_PASSWORD")
    smtp_username = os.getenv("SMTP_USERNAME")
    recipient_email = os.getenv("RECIPIENT_EMAIL")
    test_mode = os.getenv("TEST_MODE")

    if not all([gemini_key, app_password, smtp_username, recipient_email]):
        logging.error("One or more environment variables are not set. Exiting.")
        return

    news_markdown = None
    if test_mode == 'True':
        logging.info("Running in Test Mode. Using mock news.")
        print("Running in Test Mode. Using mock news.")
        try:
            with open('templates/mock_news.md', 'r') as f:
                news_markdown = f.read()
            logging.info("Successfully loaded mock news from templates/mock_news.md.")
        except FileNotFoundError:
            logging.error("mock_news.md not found. Exiting.")
            return
    else:
        # Read the prompt
        try:
            with open('prompt.md', 'r') as f:
                prompt_content = f.read()
            logging.info("Successfully loaded prompt from prompt.md.")
        except FileNotFoundError:
            logging.error("prompt.md not found. Exiting.")
            return

        # Fetch news
        news_fetcher = NewsFetcher(api_key=gemini_key)
        news_markdown = news_fetcher.get_daily_news(prompt=prompt_content)

    if not news_markdown:
        logging.error("Failed to fetch news. Exiting.")
        return
    logging.info("Successfully fetched news.")
    logging.info(f"News content from LLM:\n{news_markdown}")
    print(f"News content from LLM:\n{news_markdown}")

    # Format newsletter
    formatter = HTMLFormatter(template_dir='templates', template_name='newsletter_template.html')
    html_newsletter = formatter.format_newsletter(news_markdown)
    logging.info("Successfully formatted newsletter.")

    # Send email
    today_str = date.today().strftime("%B %d, %Y")
    subject = f"The Lithrop Ledger: {today_str}"
    
    dispatcher = EmailDispatcher(smtp_host='smtp.gmail.com', smtp_port=587, 
                                 username=smtp_username, password=app_password)
    dispatcher.send_email(to_email=recipient_email, subject=subject, html_content=html_newsletter)
    logging.info("Email dispatch process finished.")


if __name__ == '__main__':
    main()
