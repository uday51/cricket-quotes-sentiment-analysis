\

# 🏏 Cricket Quotes Sentiment Analyzer
This project scrapes cricket-related quotes from the web, processes them to extract quote-author pairs, and performs sentiment analysis using a pre-trained NLP model from Hugging Face. The final results are saved to a CSV file, including sentiment labels and confidence scores.

# 🚀 Features
Scrapes cricket quotes from url

Extracts quote and author

Performs sentiment analysis using cardiffnlp/twitter-roberta-base-sentiment


pip install requests beautifulsoup4 pandas transformers
# 🧠 Model Used
Sentiment Model: cardiffnlp/twitter-roberta-base-sentiment

Trained specifically for short social media texts

# 📜 How It Works
# 1. Scrape Quotes
Fetches HTML content from the target webpage

Extracts <li> elements containing quotes

Parses and splits quotes and author names

# 2. Sentiment Analysis
Loads the quotes from CSV

Applies the Hugging Face pipeline

Extracts label (e.g., POSITIVE, NEGATIVE, NEUTRAL) and score

# 3. Output
Saves processed data to cricket_quotes_with_sentiment.csv
