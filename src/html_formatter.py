from jinja2 import Environment, FileSystemLoader
from premailer import transform
import markdown2
import re
import json

class HTMLFormatter:
    """
    This module transforms the raw Markdown from NewsFetcher into a polished HTML email with inline CSS.
    """
    def __init__(self, template_dir, template_name):
        """
        Loads a Jinja2 HTML template from the specified path.
        """
        self.env = Environment(loader=FileSystemLoader(template_dir))
        
        # The markdown2 library is used via a Jinja2 filter
        def markdown_filter(s):
            return markdown2.markdown(s, extras=["cuddled-lists", "tables", "fenced-code-blocks"])

        self.env.filters['markdown'] = markdown_filter

        self.template = self.env.get_template(template_name)

    def _parse_news_data(self, json_content):
        """
        Parses the JSON content into a structured Python object.
        """
        if not json_content:
            return {}

        try:
            data = json.loads(json_content)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}

        news_data = {}
        
        # Map JSON fields to human-readable titles for the template
        if 'market_data' in data:
            news_data['Market Update'] = data['market_data']
        
        if 'sports_check' in data:
            news_data['Sports Check'] = data['sports_check']

        if 'sections' in data:
            for section in data['sections']:
                title = section.get('title', 'News')
                # Join stories with newlines for markdown processing in the template
                stories = section.get('stories', [])
                # Create a markdown list
                content = "\n".join([f"* {story}" for story in stories])
                news_data[title] = content

        if 'uplifting_news' in data:
            news_data['Uplifting News'] = data['uplifting_news']
            
        return news_data


    def format_newsletter(self, news_data_markdown):
        """
        Parses the Markdown content into a structured Python object (e.g., a dictionary of news sections).
        Renders the Jinja2 template, injecting the structured news content.
        Utilizes the `premailer` library to convert all CSS `<style>` blocks and linked stylesheets into inline `style` attributes on each HTML element, ensuring maximum compatibility with email clients.
        Returns the final, fully-formatted HTML string.
        """
        news_data = self._parse_news_data(news_data_markdown)
        
        html_content = self.template.render(news_data=news_data)
        inlined_html = transform(html_content)
        return inlined_html
