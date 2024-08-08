# SentimentScope

SentimentScope is a sophisticated machine learning tool that performs sentiment analysis on social media posts and comments. This project leverages Python, TensorFlow, NLTK/SpaCy, and Tweepy to help brands monitor public opinion and identify market trends through the analysis of large-scale Twitter data.

## Key Features

- **Real-time Sentiment Tracking**: Implements a system to analyze sentiments from social media posts every 5 minutes, focusing on trending topics.
- **Large-scale Data Analysis**: Processed and analyzed over 1 million posts, providing actionable insights for brand monitoring.
- **Insightful Reporting for Brands**: Offers detailed analytics and trends across various brand monitoring use cases.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation

Follow these steps to set up your local development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/Jay-Bhalala/SentimentScope.git

2. Navigate to the project directory & install the required packages:
   ```bash
   cd SentimentScope
   pip install -r requirements.txt

### Configuration

Configure the necessary API keys for accessing Twitter data in `src/config.py`:

```python
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'
```

### Usage

To start collecting data and analyzing sentiment, run the following scripts:

```
python src/data_collection/twitter_stream.py
python src/model/predict.py
```

### Running Tests

To run tests, use the following command:

```
python -m unittest discover -s tests
```
