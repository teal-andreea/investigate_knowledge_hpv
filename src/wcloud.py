import matplotlib.pyplot as plt

from wordcloud import WordCloud

if __name__ == '__main__':
  # Load the text data from the provided file
  file_path = './data/raw/interviews.txt'
  with open(file_path, 'r', encoding='utf-8') as file:
      interview_text = file.read()

  # Preprocess the text data
  # Remove common stopwords and punctuation
  stopwords = set(WordCloud().stopwords)
  additional_stopwords = {
    "interviewer", "participant", "yes", "no", "know", "think", "say", "told", "tells", "well", "one", "two", "three", "like", "doctor", "now", "go",
    "test", "HPV", "mean", "year", "time", "tell", "done", "first", "come", "said", "thing", "years", "will", "OK", "came", "years"
  }
  stopwords.update(additional_stopwords)

  # Generate the word cloud
  wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords, collocations=False).generate(interview_text)

  # Display the word cloud
  plt.figure(figsize=(10, 5))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.title('Word Cloud of Interviews on Cervical Cancer Screening in Romania')
  plt.show()
