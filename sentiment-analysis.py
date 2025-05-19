import pandas as pd
from transformers import pipeline



df = pd.read_csv('cricket_quotes.csv', header=None, names=['quote', 'player'])

# Step 4: Load the Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Step 5: Apply sentiment analysis to each quote
results = df['quote'].apply(lambda x: sentiment_pipeline(x)[0])
df['sentiment'] = results.apply(lambda x: x['label'])
df['confidence_score'] = results.apply(lambda x: x['score'])

# Step 6: Save the result to a new CSV file
df.to_csv('cricket_quotes_with_sentiment.csv', index=False)

print("Sentiment analysis complete! File saved as: cricket_quotes_with_sentiment.csv")
