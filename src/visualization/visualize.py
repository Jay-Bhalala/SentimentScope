
import matplotlib.pyplot as plt
import numpy as np

def plot_sentiment_distribution(sentiments):
    ''' Function to plot the sentiment distribution '''
    plt.hist(sentiments, bins=20, color='blue', edgecolor='black')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    sentiments = np.random.uniform(-1, 1, 1000)
    plot_sentiment_distribution(sentiments)
