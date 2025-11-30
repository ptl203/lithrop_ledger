from jinja2 import Environment, FileSystemLoader
from premailer import transform
import markdown2
import re

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

    def _parse_news_data(self, markdown_content):
        """
        Parses the Markdown content into a structured Python object (a dictionary of news sections).
        """
        if not markdown_content:
            return {}

        news_data = {}
        # The regex looks for sections starting with a markdown header (##)
        sections = re.split(r'\n## ', markdown_content)
        
        # Process the intro section (everything before the first ##)
        if sections:
            intro_content = sections.pop(0)
            
            # Find the start of the sports check
            sports_check_start = intro_content.find('**Sports Check**')
            
            # Everything before sports check (that's not the main title) is market data
            market_data_raw = intro_content[:sports_check_start if sports_check_start != -1 else len(intro_content)].strip()
            # Remove the "# **Lithrop Ledger**" title
            market_data = re.sub(r'^#\s*\*?Lithrop Ledger\*?\s*\n*', '', market_data_raw, flags=re.IGNORECASE).strip()
            if market_data:
                news_data['Market Update'] = market_data

            # Everything from sports check onwards is sports data
            if sports_check_start != -1:
                sports_data_raw = intro_content[sports_check_start:]
                # Remove the title
                sports_data = sports_data_raw.replace('**Sports Check**', '').strip()
                news_data['Sports Check'] = sports_data

        # Process the rest of the sections
        for section_content in sections:
            # The section title is the first line
            title_match = re.match(r'(.+)', section_content)
            if title_match:
                title = title_match.group(1).strip().replace('*', '')
                # The content is everything after the title
                content = section_content[len(title_match.group(1)):].strip()
                news_data[title] = content
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
