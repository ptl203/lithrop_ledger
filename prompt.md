Generate a newsletter for today's news titled "Lithrop Ledger".
Current Date: {{date}}

You must return a valid JSON object. Do not include markdown formatting (like ```json).

The JSON object must have this exact structure:
{
  "market_data": "String summary of market data...",
  "sports_check": "String summary of sports check...",
  "sections": [
    {
      "title": "World News",
      "stories": [
        "Story 1...",
        "Story 2..."
      ]
    },
    ... (other sections: US News, Finance News, Technology Business News)
  ],
  "uplifting_news": "String containing the uplifting story..."
}

# Instructions for Content

## Market Data
List the daily percentage change for the S&P 500, NASDAQ, DOW, 10-Year Treasury, and Bitcoin.
If the market is closed, state it.

## Sports Check
Check the following for these teams:

**New York Rangers**:
- **Next Game**: Check if they play today ({{date}}). Reference scheduled time and opponent. If NO game today, list the next game date/time/opponent.
- **Last Game**: Provide the score and opponent of their most recent game.
- **Team News**: Brief summary of any recent major news (injuries, trades, streaks).
- **Standings**: Current position and points in the Metropolitan Division.

**New York Giants**:
- **News**: Recent team news.
- **Game Info**: Next scheduled game or recent result.

**Syracuse University Athletics (Lacrosse, Basketball, Football)**:
- **News**: Recent news updates.
- **Game Times**: Upcoming scheduled games.

## News Sections
For each section below, provide **4-5 stories**. This is a strict requirement.
- **World News**: Startling geopolitical developments. High gravity.
- **US News**: Legislation, elections, major domestic events for an informed voter.
- **Finance News**: Deep dive for executives. Earnings, movers, economic indicators.
- **Technology Business News**: AI, Cloud, Quantum, Enterprise. No consumer gadgets.

**Constraints for News Stories:**
- **CRITICAL**: Use the Google Search tool to ensure ALL stories are from **{{date}}** or yesterday.
- **Quantity**: You MUST provide 4 to 5 distinct stories for each section. Do not stop at 1 or 2.
- **NO LINKS**: Do not include URLs.
- **Detail Level**: 4-6 sentences per story.
- **Specifics Required**: You must include specific names of people/countries involved, specific numbers/stats (if applicable), and a brief mention of the reaction or impact. Avoid vague summaries.

## Uplifting News
A single positive story (animals, nature, local heroes). No politics/finance/tech/public figures. Include specific names and location.

# FORMATTING
- Return RAW JSON.
- No Markdown blocks.
- No "From the desk of..." or other filler.

